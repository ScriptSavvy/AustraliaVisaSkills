"""Discover published skills from release ZIP names and public skill folders.

No per-skill registration. The only fixed entries below preserve existing
presentation, not discovery, identity, paths, tags or eligibility.
"""
import re
from pathlib import Path

ASSET = re.compile(r'([a-z0-9]+(?:-[a-z0-9]+)*)-v([0-9]+\.[0-9]+\.[0-9]+)\.zip')
# Optional historical wording only. Unknown skills use generated labels.
PRESENTATION = {
    'student-500-preparation': ('Student 500', 'Student — Subclass 500'),
    'visitor-600-preparation': ('Visitor 600', 'Visitor — Subclass 600'),
    'partner-801-preparation': ('Partner 801', 'Partner — Subclass 801'),
    'gsm-points-preparation': ('GSM Points', 'GSM points — Subclasses 189, 190 and 491'),
    'temporary-graduate-485-preparation': ('Temporary Graduate 485', 'Temporary Graduate — Subclass 485'),
    'student-guardian-590-preparation': ('Student Guardian 590', 'Student Guardian — Subclass 590'),
}


def read_identity(instructions):
    """Accept the project's root-version and direct metadata.version layouts."""
    lines = instructions.split('\n')
    if lines[0] != '---' or '---' not in lines[1:]:
        raise ValueError('Missing skill frontmatter')
    header = '\n'.join(lines[1:lines.index('---', 1)])

    def exact_scalar(value, pattern):
        value = value.strip()
        if value[:1] in ('"', "\'") and value[-1:] == value[:1]:
            value = value[1:-1]
        return value if re.fullmatch(pattern, value) else None

    versions, names, parents = [], [], []
    metadata_count = 0
    for line in header.split('\n'):
        if not line.strip() or line.lstrip().startswith('#'):
            continue
        indent = len(line) - len(line.lstrip(' '))
        if line[indent:][:1] == '\t':
            raise ValueError('Ambiguous skill frontmatter indentation')
        while parents and parents[-1][0] >= indent:
            parents.pop()
        field = re.fullmatch(r'([^:]+):[ \t]*(.*)', line[indent:])
        if field:
            key, value = field.groups()
            key = key.strip()
            normalized_key = key.strip('\"\'')
            if normalized_key in ('name', 'version', 'metadata', '<<') and key != normalized_key:
                raise ValueError('Unsupported quoted identity key')
            if key == '<<':
                raise ValueError('Ambiguous merged skill frontmatter')
            if key == 'metadata' and indent == 0:
                metadata_count += 1
                if metadata_count > 1 or (value.strip() and not value.lstrip().startswith('#')):
                    raise ValueError('Ambiguous skill metadata mapping')
            if key == 'version':
                if not (indent == 0 or parents == [(0, 'metadata')]):
                    raise ValueError('Unsupported skill version scope')
                versions.append(exact_scalar(value, r'[0-9]+\.[0-9]+\.[0-9]+'))
            if key == 'name':
                if indent != 0:
                    raise ValueError('Unsupported skill name scope')
                names.append(exact_scalar(value, r'[a-z0-9]+(?:-[a-z0-9]+)*'))
            parents.append((indent, key))
        else:
            parents.append((indent, None))
    if len(names) != 1 or len(versions) != 1 or names[0] is None or versions[0] is None:
        raise ValueError('Invalid or ambiguous skill name/version')
    return names[0], versions[0]


def checked_file(root, path):
    """Keep source and guide lookups inside real public directories."""
    root, path = Path(root), Path(path)
    try:
        relative = path.relative_to(root)
    except ValueError as error:
        raise ValueError('Source path outside public root') from error
    current = root
    for part in relative.parts:
        current = current / part
        if current.is_symlink():
            raise ValueError('Symlink source or guide is not supported')
    if not path.is_file():
        raise ValueError('Missing public skill source or guide')
    return path


def discover_skills(root, releases):
    """One stable release and uploaded versioned ZIP per applicant skill.

    Scan all published releases, not a registry. Match each activation name to
    exactly one <wrapper>/<activation-name>/SKILL.md. Unmatched or ambiguous
    published material blocks the refresh rather than silently omitting a row.
    Drafts/prereleases and unpublished local folders are not advertised.
    """
    root = Path(root)
    if not isinstance(releases, list) or not releases:
        raise ValueError('Expected nonempty complete release inventory')
    skills, seen_tags, seen_names = [], set(), set()
    readme = root.joinpath('README.md').read_text(encoding='utf-8') if root.joinpath('README.md').is_file() else ''
    for release in releases:
        if release['draft'] or release.get('prerelease', False):
            continue
        tag = release['tag_name']
        # Preserve exact case/spelling. Restrict unsafe URL/Markdown characters.
        if not isinstance(tag, str) or not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9._-]*', tag):
            raise ValueError('Unsupported stable tag syntax')
        if tag in seen_tags:
            raise ValueError('Duplicate published tag')
        seen_tags.add(tag)
        assets = [a for a in release['assets'] if a.get('state') == 'uploaded' and ASSET.fullmatch(a['name'])]
        zips = [a for a in release['assets'] if a['name'].lower().endswith('.zip')]
        if len(assets) != 1 or len(zips) != 1:
            raise ValueError('Expected exactly one uploaded versioned skill ZIP per stable release')
        asset_match = ASSET.fullmatch(assets[0]['name'])
        if asset_match is None:
            raise ValueError('Invalid versioned skill ZIP name')
        name, version = asset_match.groups()
        if name in seen_names:
            raise ValueError('Same skill published under multiple stable tags')
        seen_names.add(name)
        matches = list(root.glob('*/'+name+'/SKILL.md'))
        if len(matches) != 1:
            raise ValueError('Published skill needs exactly one matching public source folder')
        instructions = checked_file(root, matches[0])
        base = instructions.parent
        wrapper = base.parent.name
        if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_-]*', wrapper):
            raise ValueError('Unsupported public wrapper name')
        source_name, _ = read_identity(instructions.read_text(encoding='utf-8'))
        if source_name != name:
            raise ValueError('Public folder and skill activation name differ')
        for guide in ('README.md', 'INSTALL.md', 'USAGE.md'):
            checked_file(root, base / guide)
        title = name.removesuffix('-preparation').replace('-', ' ').title()
        label, display = PRESENTATION.get(name, (title, title))
        relative = base.relative_to(root).as_posix()
        skills.append(dict(name=name, path=relative, tag=tag, label=label,
                           display=display, version=version))
    if not skills:
        raise ValueError('No published stable skills; refusing to erase catalogues')
    # Retain existing rows' order; append new entries deterministically.
    def order(skill):
        position = readme.find(']('+skill['path']+'/README.md)')
        return (0, position, '') if position >= 0 else (1, 0, skill['path'])
    return tuple(sorted(skills, key=order))

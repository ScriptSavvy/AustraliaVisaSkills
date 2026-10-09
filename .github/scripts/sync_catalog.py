"""Synchronise root catalogues from published ZIPs; no packaging or release writes."""
import hashlib
import io
import json
import os
import subprocess
import re
import tempfile
import zipfile
from pathlib import Path, PurePosixPath
from contextlib import contextmanager
from changelog_catalog import SKILLS, build
from readme_catalog import build_readme


def download(url):
    if not (url.startswith('https://api.github.com/repos/ScriptSavvy/AustraliaVisaSkills/releases?')
            or url.startswith('https://github.com/ScriptSavvy/AustraliaVisaSkills/releases/download/')):
        raise ValueError('Unexpected download origin')
    config = ''
    token = os.environ.get('GITHUB_TOKEN')
    if token and url.startswith('https://api.github.com/'):
        if '\n' in token or '\r' in token:
            raise ValueError('Invalid token configuration')
        config = 'header = '+json.dumps('Authorization: Bearer '+token)+'\n'
    process = subprocess.run(['curl', '--fail', '--silent', '--show-error', '--location',
        '--proto', '=https', '--proto-redir', '=https', '--max-filesize', '5000000',
        '--connect-timeout', '15', '--max-time', '90', '--retry', '2',
        '--config', '-', url], input=config.encode(), capture_output=True, timeout=300)
    if process.returncode:
        raise ValueError('GitHub retrieval failed; leaving catalogues unchanged')
    if len(process.stdout) > 5_000_000:
        raise ValueError('Download exceeds size limit')
    return process.stdout


def get_releases(fetch=download):
    result = []
    seen = set()
    for page in range(1, 101):
        data = json.loads(fetch('https://api.github.com/repos/ScriptSavvy/AustraliaVisaSkills/releases?per_page=100&page='+str(page)))
        if not isinstance(data, list):
            raise ValueError('Expected GitHub release list')
        for release in data:
            tag = release['tag_name']
            if tag in seen:
                raise ValueError('Duplicate release tag in paginated response')
            seen.add(tag)
            result.append(release)
        if len(data) < 100:
            return result
    raise ValueError('Release pagination exceeded safe limit')


@contextmanager
def checked_archive(data, skill):
    try:
        with zipfile.ZipFile(io.BytesIO(data)) as archive:
            entries = archive.infolist()
            names = [e.filename for e in entries]
            if len(names) != len(set(names)) or len(names) > 500 or sum(e.file_size for e in entries) > 10_000_000:
                raise ValueError('Duplicate or oversized ZIP entries')
            for entry in entries:
                path = PurePosixPath(entry.filename)
                if (path.is_absolute() or '..' in path.parts or '\\' in entry.filename
                        or not path.parts or path.parts[0] != skill['name']
                        or entry.file_size > 2_000_000 or entry.flag_bits & 1
                        or (entry.external_attr >> 16) & 0o170000 == 0o120000):
                    raise ValueError('Unsafe or oversized ZIP member')
            if archive.testzip() is not None:
                raise ValueError('ZIP integrity check failed')
            yield archive
    except (zipfile.BadZipFile, KeyError, UnicodeError, RuntimeError, IndexError) as error:
        raise ValueError('Invalid published ZIP') from error


def render(root, releases, fetch, baselines):
    root = Path(root)
    with tempfile.TemporaryDirectory() as temporary:
        source_root = Path(temporary)
        for skill in SKILLS:
            matching = [r for r in releases if r['tag_name'] == skill['tag'] and not r['draft'] and not r.get('prerelease', False)]
            if not matching:
                continue
            if len(matching) != 1:
                raise ValueError('Duplicate published tag: '+skill['tag'])
            pattern = re.escape(skill['name'])+r'-v(\d+\.\d+\.\d+)\.zip'
            assets = [a for a in matching[0]['assets'] if re.fullmatch(pattern, a['name']) and a.get('state') == 'uploaded']
            if len(assets) != 1:
                raise ValueError('Expected one matching ZIP: '+skill['tag'])
            asset = assets[0]
            version_match = re.fullmatch(pattern, asset['name'])
            if version_match is None:
                raise ValueError('Invalid asset name')
            version = version_match.group(1)
            expected_url = 'https://github.com/ScriptSavvy/AustraliaVisaSkills/releases/download/'+skill['tag']+'/'+asset['name']
            if asset['browser_download_url'] != expected_url or not 0 < asset['size'] <= 5_000_000:
                raise ValueError('Unexpected asset URL or size')
            data = fetch(asset['browser_download_url'])
            if len(data) != asset['size'] or asset.get('digest') != 'sha256:'+hashlib.sha256(data).hexdigest():
                raise ValueError('ZIP size/digest mismatch: '+asset['name'])
            with checked_archive(data, skill) as archive:
                name = skill['name']+'/SKILL.md'
                instructions = archive.read(name).decode('utf-8')
                lines = instructions.split('\n')
                if lines[0] != '---' or '---' not in lines[1:]:
                    raise ValueError('Missing skill frontmatter')
                header = '\n'.join(lines[1:lines.index('---', 1)])
                def exact_scalar(value, pattern):
                    value = value.strip()
                    if value[:1] in ('"', "'") and value[-1:] == value[:1]:
                        value = value[1:-1]
                    return value if re.fullmatch(pattern, value) else None

                versions, names = [], []
                parents = []
                metadata_count = 0
                # Deliberately validate only a restricted block-mapping subset:
                # never infer identity from unrelated or deeper nested fields.
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
                            names.append(exact_scalar(value, r'[a-z0-9-]+'))
                        parents.append((indent, key))
                    else:
                        # Non-mapping lines cannot establish a metadata parent.
                        parents.append((indent, None))
                if versions != [version] or names != [skill['name']]:
                    raise ValueError('ZIP skill name/version mismatch')
                history_name = skill['name']+'/CHANGELOG.md'
                if history_name in archive.namelist():
                    history = archive.read(history_name).decode('utf-8')
                else:
                    baseline = baselines.get(skill['tag'], {})
                    local = (root / skill['path'] / 'CHANGELOG.md').read_bytes()
                    if (baseline.get('version') != version or baseline.get('asset_digest') != asset['digest']
                            or baseline.get('changelog_sha256') != hashlib.sha256(local).hexdigest()):
                        raise ValueError('Missing bundled changelog without exact reviewed migration baseline: '+skill['tag'])
                    history = local.decode('utf-8')
            target = source_root / skill['path'] / 'CHANGELOG.md'
            target.parent.mkdir(parents=True)
            target.write_text(history, encoding='utf-8')
        changelog = build(source_root, releases)
        readme = build_readme(root, root.joinpath('README.md').read_text(encoding='utf-8'), releases)
        return {'README.md': readme, 'CHANGELOG.md': changelog}


if __name__ == '__main__':
    import argparse
    import sys

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path('.'))
    parser.add_argument('--releases', type=Path, help='Complete API snapshot for offline validation')
    parser.add_argument('--assets-dir', type=Path, help='Downloaded ZIP cache for offline validation')
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--write', action='store_true')
    mode.add_argument('--check', action='store_true')
    args = parser.parse_args()
    staged = []
    try:
        if bool(args.releases) != bool(args.assets_dir):
            raise ValueError('Offline validation requires both releases and assets-dir')
        releases = json.loads(args.releases.read_text(encoding='utf-8')) if args.releases else get_releases()
        if not isinstance(releases, list) or not releases:
            raise ValueError('Empty or invalid release inventory; refusing to erase catalogues')
        baseline_path = Path(__file__).with_name('migration-baselines.json')
        baselines = json.loads(baseline_path.read_text(encoding='utf-8')) if baseline_path.exists() else {}
        if args.assets_dir:
            def fetch(url):
                return (args.assets_dir / url.rsplit('/', 1)[1]).read_bytes()
        else:
            fetch = download
        outputs = render(args.root, releases, fetch, baselines)
        changes = []
        for name, content in outputs.items():
            target = args.root / name
            if target.is_symlink():
                raise ValueError('Refusing symlink output')
            if not target.exists() or target.read_text(encoding='utf-8') != content:
                changes.append((target, content))
        if args.check and changes:
            raise ValueError('Catalogues need regeneration: '+', '.join(p.name for p, _ in changes))
        if args.check:
            print('PASS: README and changelog match verified published ZIPs and reviewed migration baselines')
        elif not changes:
            print('No change: catalogues already current')
        else:
            for target, content in changes:
                with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', dir=args.root, prefix='.catalogue-', delete=False) as handle:
                    pending = Path(handle.name)
                    staged.append((pending, target))
                    handle.write(content)
            for pending, target in staged:
                os.replace(pending, target)
                print('Updated '+str(target))
    except (ValueError, OSError, KeyError, TypeError, subprocess.TimeoutExpired) as error:
        print('ERROR: '+str(error), file=sys.stderr)
        sys.exit(1)
    finally:
        for pending, _ in staged:
            pending.unlink(missing_ok=True)

"""Refresh only the root README skill table; never package or publish."""
import re
from pathlib import Path
from changelog_catalog import SKILLS

DISPLAY = {
    'Subclass500': 'Student — Subclass 500',
    'subclass600': 'Visitor — Subclass 600',
    'subclass801': 'Partner — Subclass 801',
    'gsm-points': 'GSM points — Subclasses 189, 190 and 491',
}


def build_readme(root, text, releases):
    rows = ['| Visa | Skill | Guides | Release page |', '| --- | --- | --- | --- |']
    for s in SKILLS:
        matches = [r for r in releases if r['tag_name'] == s['tag'] and not r['draft'] and not r.get('prerelease', False)]
        if not matches:
            continue
        if len(matches) != 1:
            raise ValueError('Duplicate published tag: '+s['tag'])
        pattern = re.escape(s['name']) + r'-v(\d+\.\d+\.\d+)\.zip'
        assets = [a for a in matches[0]['assets'] if re.fullmatch(pattern, a['name']) and a.get('state') == 'uploaded']
        if len(assets) != 1:
            raise ValueError('Expected one uploaded versioned ZIP: '+s['tag'])
        version_match = re.fullmatch(pattern, assets[0]['name'])
        if version_match is None:
            raise ValueError('Invalid asset version')
        version = version_match.group(1)
        base = s['path']
        for guide in ('README.md', 'INSTALL.md', 'USAGE.md'):
            if not (Path(root) / base / guide).is_file():
                raise ValueError('Missing linked guide: '+base+'/'+guide)
        rows.append(f'| {DISPLAY[s["tag"]]} | [{s["name"]}]({base}/README.md), v{version} | [Install]({base}/INSTALL.md) · [Use]({base}/USAGE.md) | [v{version}](https://github.com/ScriptSavvy/AustraliaVisaSkills/releases/tag/{s["tag"]}) |')
    if len(rows) == 2:
        raise ValueError('No supported published releases; refusing to erase table')
    pattern = r'(?m)(^## Choose your skill\n)(?:\|[^\n]*\n)+'
    if len(re.findall(r'(?m)^## Choose your skill$', text)) != 1 or len(re.findall(pattern, text)) != 1:
        raise ValueError('Expected exactly one Choose your skill heading with a table')
    return re.sub(pattern, lambda m: m.group(1)+'\n'.join(rows)+'\n', text)


if __name__ == '__main__':
    import argparse
    import json
    import os
    import sys
    import tempfile

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', required=True, type=Path)
    parser.add_argument('--releases', required=True, type=Path)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--write', action='store_true')
    mode.add_argument('--check', action='store_true')
    args = parser.parse_args()
    try:
        releases = json.loads(args.releases.read_text(encoding='utf-8'))
        if not isinstance(releases, list):
            raise ValueError('Expected a GitHub releases list')
        target = args.root / 'README.md'
        if target.is_symlink():
            raise ValueError('Refusing symlink output')
        existing = target.read_text(encoding='utf-8')
        content = build_readme(args.root, existing, releases)
        if args.check:
            if existing != content:
                raise ValueError('README skill table needs regeneration')
            print('PASS: README table matches published release ZIP versions')
        elif existing == content:
            print('No change: README table already matches published releases')
        else:
            with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', dir=args.root, prefix='.readme-', delete=False) as handle:
                pending = Path(handle.name)
                handle.write(content)
            try:
                os.replace(pending, target)
            finally:
                pending.unlink(missing_ok=True)
            print('Updated '+str(target))
    except (ValueError, OSError, KeyError, TypeError) as error:
        print('ERROR: '+str(error), file=sys.stderr)
        sys.exit(1)

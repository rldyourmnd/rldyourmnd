#!/usr/bin/env python3
"""Read-only, offline checks for profile content and reproducible drawings."""
from __future__ import annotations

import argparse
from html.parser import HTMLParser
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET

from render_profile import ROOT, expected_assets

SVG_NS = 'http://www.w3.org/2000/svg'
ALLOWED_SVG = {'svg', 'title', 'desc', 'defs', 'pattern', 'marker', 'path',
               'rect', 'g', 'text', 'style'}
PROJECTS = ('NDDev-OpenNetwork/github-device-sync', 'ai-engineers-guild/ai-stp',
            'NDDev-OpenNetwork/codex-setup-system')
CONTACTS = ('mailto:danil@nddev.it.com', 'https://t.me/Danil_Silantyev')


class Markup(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.refs: list[str] = []
        self.errors: list[str] = []
        self.details = 0
        self.pictures = 0
        self.images = 0
        self.visible: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if tag not in {'a', 'picture', 'source', 'img', 'details', 'summary'}:
            self.errors.append(f'Unsupported README HTML: {tag}')
        if any(k.startswith('on') or k in {'style', 'class', 'id'} for k in values):
            self.errors.append('Nonportable README HTML attributes')
        if tag == 'details':
            self.details += 1
            if 'open' in values:
                self.errors.append('Language navigation must be collapsed')
        elif tag == 'picture':
            self.pictures += 1
        elif tag == 'img':
            self.images += 1
            if not values.get('alt', '').strip():
                self.errors.append('Missing image alternative')
            if not values.get('src'):
                self.errors.append('Missing image source')
            else:
                self.refs.append(values['src'])
        elif tag == 'source':
            if not values.get('media') or not values.get('srcset'):
                self.errors.append('Incomplete picture source')
            else:
                self.refs.append(values['srcset'])
        if values.get('href'):
            self.refs.append(values['href'])

    def handle_endtag(self, tag: str) -> None:
        if tag == 'details':
            self.details -= 1
        elif tag == 'picture':
            self.pictures -= 1
        if self.details < 0 or self.pictures < 0:
            self.errors.append('Unbalanced README HTML')

    def handle_data(self, data: str) -> None:
        if not self.details:
            self.visible.append(data)


def validate(root: Path) -> list[str]:
    root = root.resolve()
    errors: list[str] = []
    expected = expected_assets()
    folder = root/'assets/profile'
    observed = {p.name for p in folder.glob('*.svg')}
    for name, data in expected.items():
        file = folder/name
        if not file.is_file() or file.read_bytes() != data.encode('utf-8'):
            errors.append(f'Generated SVG missing or changed: {name}')
    for name in sorted(observed - expected.keys()):
        errors.append(f'Unexpected SVG: {name}')

    for name in ('README.md', 'README.ru.md'):
        file = root/name
        if not file.is_file():
            errors.append(f'Missing {name}')
            continue
        text = file.read_text(encoding='utf-8')
        if len(text.encode('utf-8')) > 20_000:
            errors.append(f'{name}: README exceeds 20 KB')
        parser = Markup()
        parser.feed(text)
        errors.extend(f'{name}: {error}' for error in parser.errors)
        if parser.details or parser.pictures:
            errors.append(f'{name}: unclosed HTML')
        if parser.images != 4:
            errors.append(f'{name}: expected four image alternatives')
        if name == 'README.md' and re.search('[\u0400-\u04ff]', ''.join(parser.visible)):
            errors.append('README.md: Russian is visible outside collapsed navigation')
        if name == 'README.md' and '[Русский](README.ru.md)' not in text:
            errors.append('README.md: missing Russian navigation')
        if name == 'README.ru.md' and '[English](README.md)' not in text:
            errors.append('README.ru.md: missing English navigation')
        if '\u2014' in text or '\u2013' in text:
            errors.append(f'{name}: long dash')
        for value in PROJECTS + CONTACTS:
            if value not in text:
                errors.append(f'{name}: missing project or contact: {value}')
        for value in ('nddev-knowledge-graph', '/server-', '/client-', 'PRIVATE KEY',
                      'img.shields.io', 'readme-stats', 'NDDev-Archive', 'Curestry', 'My Attention'):
            if value.casefold() in text.casefold():
                errors.append(f'{name}: unexpected profile content: {value}')
        refs = parser.refs + re.findall(r'\]\(([^)]+)\)', text)
        for ref in refs:
            parts = urlsplit(ref)
            if parts.scheme:
                if parts.scheme not in {'https', 'mailto'}:
                    errors.append(f'{name}: unsupported link scheme: {ref}')
                continue
            if parts.netloc:
                errors.append(f'{name}: scheme-relative URL: {ref}')
                continue
            if not parts.path:
                continue
            local = (root/unquote(parts.path)).resolve()
            if not local.is_relative_to(root):
                errors.append(f'{name}: path escapes repository: {ref}')
            elif not local.is_file():
                errors.append(f'{name}: missing local target: {ref}')
        # Images may not depend on third-party services, even if a link may.
        for ref in re.findall(r'(?:src|srcset)="([^"]+)"', text):
            if urlsplit(ref).scheme or not ref.startswith('assets/profile/'):
                errors.append(f'{name}: image must be repository-local: {ref}')

    total = 0
    for file in sorted(folder.glob('*.svg')):
        data = file.read_text(encoding='utf-8')
        size = len(data.encode('utf-8'))
        total += size
        if size > 12_000:
            errors.append(f'{file.name}: SVG exceeds 12 KB')
        if re.search(r'<!DOCTYPE|<!ENTITY', data, re.I):
            errors.append(f'{file.name}: XML declarations are not allowed')
            continue
        try:
            tree = ET.fromstring(data)
        except ET.ParseError as exc:
            errors.append(f'{file.name}: invalid XML: {exc}')
            continue
        if tree.tag != f'{{{SVG_NS}}}svg':
            errors.append(f'{file.name}: invalid SVG root')
        if tree.find(f'{{{SVG_NS}}}title') is None or tree.find(f'{{{SVG_NS}}}desc') is None:
            errors.append(f'{file.name}: missing accessible SVG description')
        ids = [e.attrib['id'] for e in tree.iter() if 'id' in e.attrib]
        if len(ids) != len(set(ids)):
            errors.append(f'{file.name}: duplicate IDs')
        for element in tree.iter():
            tag = element.tag.rsplit('}', 1)[-1]
            if tag not in ALLOWED_SVG:
                errors.append(f'{file.name}: unsupported SVG element: {tag}')
            for key, value in element.attrib.items():
                key = key.rsplit('}', 1)[-1]
                if key.lower().startswith('on') or key in {'href', 'src'}:
                    errors.append(f'{file.name}: active or linked SVG content')
                if 'url(' in value and not re.fullmatch(r'url\(#[A-Za-z0-9_-]+\)', value):
                    errors.append(f'{file.name}: nonlocal SVG URL')
        for target in re.findall(r'url\(#([A-Za-z0-9_-]+)\)', data):
            if target not in ids:
                errors.append(f'{file.name}: unresolved SVG reference: {target}')
        if re.search(r'@import|@font-face|\binfinite\b|javascript:|data:', data, re.I):
            errors.append(f'{file.name}: nonpassive or unbounded content')
        if 'animation:' in data and 'prefers-reduced-motion:reduce' not in data:
            errors.append(f'{file.name}: missing reduced-motion rule')
    if total > 128_000:
        errors.append('SVG collection exceeds 128 KB')
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    args = parser.parse_args()
    errors = validate(args.root)
    if errors:
        print('\n'.join(f'FAIL: {error}' for error in errors), file=sys.stderr)
        return 1
    print('PASS: both READMEs, local references, 19 reproducible SVGs, passive content and size budgets.')
    print('Not measured here: remote URLs, GitHub rendering, account settings, product runtime or GDS bundle validity.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

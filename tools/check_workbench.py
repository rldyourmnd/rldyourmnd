#!/usr/bin/env python3
"""Check the owner's visible stack and names-only client section, offline."""
from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
import re

HARNESSES = ('Claude Code', 'Codex', 'Grok Build', 'Pi', 'OpenCode', 'Cursor', 'Antigravity')
LANGUAGES = ('Rust', 'Python', 'Go', 'C / C++', 'TypeScript', 'Dart (Flutter)')
TOOLS = ('CLIProxyAPI', 'Impeccable', 'Ponytail', 'ctx', 'Serena', 'Context7',
         'DeepWiki', 'MCP', 'LSP', 'GitHub', 'Figma', 'shadcn', 'Dart/Flutter',
         'Chrome DevTools', 'Playwright CLI', 'skills', 'hooks', 'subagents', 'plugins')
UPSTREAMS = {
    'CLIProxyAPI': 'https://github.com/router-for-me/CLIProxyAPI',
    'Impeccable': 'https://github.com/pbakaus/impeccable',
    'Ponytail': 'https://github.com/DietrichGebert/ponytail',
}
SECTIONS = {
    'README.md': ('Languages', 'Seven coding harnesses', 'Selected open-source work',
                  'Selected client work', 'Almaty Customs · Almaty City Libraries'),
    'README.ru.md': ('Языки', 'Семь кодинг-харнессов', 'Избранные open-source проекты',
                     'Клиентские проекты', 'Таможня Алматы · Библиотеки Алматы'),
}


class VisibleText(HTMLParser):
    """Ignore attributes, comments and collapsed details, not just CSS styling."""
    def __init__(self) -> None:
        super().__init__()
        self.depth = 0
        self.parts: list[str] = []

    def handle_starttag(self, tag, attrs):
        if tag == 'details':
            self.depth += 1

    def handle_endtag(self, tag):
        if tag == 'details':
            self.depth = max(0, self.depth - 1)

    def handle_data(self, data):
        if not self.depth:
            self.parts.append(data)


def visible_text(text: str) -> str:
    parser = VisibleText()
    parser.feed(text)
    text = ''.join(parser.parts)
    # A URL, alt attribute or hidden language link does not prove visible copy.
    return re.sub(r'!?\[([^\]]*)\]\([^)]+\)', r'\1', text)


def section(text: str, heading: str) -> str | None:
    match = re.search(r'(?m)^#{1,6} ' + re.escape(heading) + r'\s*\n', text)
    if not match:
        return None
    tail = text[match.end():]
    next_heading = re.search(r'(?m)^#{1,6} ', tail)
    return tail[:next_heading.start()] if next_heading else tail


def contains(text: str, word: str) -> bool:
    return bool(re.search(r'(?<!\w)' + re.escape(word) + r'(?!\w)', text, re.I))


def validate_workbench(root: Path) -> list[str]:
    errors: list[str] = []
    for name, (language_heading, harness_heading, work_heading, client_heading, names) in SECTIONS.items():
        path = root/name
        if not path.is_file():
            errors.append(f'{name}: missing workbench document')
            continue
        raw = path.read_text(encoding='utf-8')
        visible = visible_text(raw)
        work = re.search(r'(?m)^## ' + re.escape(work_heading) + r'\s*$', visible)
        if work is None:
            errors.append(f'{name}: missing selected-work heading')
        lead = visible[:work.start()] if work else ''
        languages = section(lead, language_heading) or ''
        for value in LANGUAGES:
            if not contains(languages, value):
                errors.append(f'{name}: language not visible before projects: {value}')
        harness_section = section(lead, harness_heading) or ''
        first_line = next((line.strip('* ') for line in harness_section.splitlines() if line.strip()), '')
        actual = [item.strip() for item in first_line.split('·')]
        if len(actual) != len(HARNESSES) or set(actual) != set(HARNESSES):
            errors.append(f'{name}: expected exactly the seven named harnesses before projects')
        for value in TOOLS:
            if not contains(lead, value):
                errors.append(f'{name}: tool not visible before projects: {value}')
        for label, url in UPSTREAMS.items():
            if f'[{label}]({url})' not in raw:
                errors.append(f'{name}: missing verified upstream link: {label}')
        # This narrow rule guards the agreed client section, not arbitrary secrets.
        client_copy = section(raw, client_heading)
        if client_copy is None or client_copy.strip() != names:
            errors.append(f'{name}: client section must contain only approved plain-text names')
        for client_name in names.split(' · '):
            if raw.count(client_name) != 1:
                errors.append(f'{name}: client name repeated outside the names-only section')
        if '[ctx](' in raw or '[`ctx`](' in raw:
            errors.append(f'{name}: ctx must stay unlinked until its upstream is identified')
    return errors

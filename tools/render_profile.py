#!/usr/bin/env python3
"""Generate isometric profile SVGs. Python 3.10+, standard library only."""
from __future__ import annotations
import argparse
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
THEMES = {
    'light': dict(bg='#faf8f4', ink='#252a2c', muted='#60645f', line='#ccc9c1', top='#f0ede6', side='#d6d2c9', front='#e3dfd6', accent='#b54a1c', grid='#e8e5de'),
    'dark': dict(bg='#14191d', ink='#f0ece4', muted='#b3b5af', line='#42494c', top='#313a3e', side='#1e272b', front='#263035', accent='#f39364', grid='#232b2f'),
}
TITLES = {'gds': 'GDS', 'ai-stp': 'ai-stp', 'setup': 'Setup systems'}
SUBTITLES = {'gds': 'Repository control plane', 'ai-stp': 'Versioned agent setups', 'setup': 'Seven native harnesses'}
DESCRIPTIONS = {
    'gds': 'Canonical source is compiled into an immutable policy and context bundle, then projected into repositories. Identity is independent of checkout paths.',
    'ai-stp': 'The CLI assembles a versioned setup bundle; the harness provider writes native state. A project of AI Engineers Guild.',
    'setup': 'Back up the explicit target before applying a setup, then verify. Restore can return a saved backup to the target.',
}

class Drawing:
    def __init__(self, width, height, theme, title, desc, motion=False):
        self.w, self.h, self.c = width, height, THEMES[theme]
        c = self.c
        self.parts = [
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
            f'<title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}</desc>',
            '<!-- GENERATED FILE. Edit-source: tools/render_profile.py; regenerate with python3 tools/render_profile.py. -->',
            f'<defs><pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse"><path d="M32 0H0V32" fill="none" stroke="{c["grid"]}" stroke-width=".6"/></pattern>',
            f'<marker id="arrow" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="m1 1 4 2-4 2" fill="none" stroke="{c["accent"]}" stroke-width="1"/></marker></defs>',
            f'<rect width="{width}" height="{height}" rx="12" fill="{c["bg"]}"/>',
            f'<rect x="1" y="1" width="{width-2}" height="{height-2}" rx="11" fill="url(#grid)" stroke="{c["line"]}"/>',
        ]
        if motion:
            # Six bounded cycles. All meaning is visible even with animation disabled.
            self.parts.append('<style>@keyframes lift{0%,100%{transform:translateY(0)}45%,55%{transform:translateY(-9px)}}@keyframes signal{0%,100%{stroke-dashoffset:40;opacity:0}20%,80%{opacity:1}90%{stroke-dashoffset:0;opacity:0}}.lift{animation:lift 8s ease-in-out 6}.signal{animation:signal 8s ease-in-out 6;stroke-dasharray:3 17;opacity:0}@media(prefers-reduced-motion:reduce){.lift,.signal{animation:none}.signal{display:none}}</style>')

    def text(self, x, y, value, size=20, color='ink', weight=400, anchor='start', mono=False):
        font = 'ui-monospace, monospace' if mono else 'Arial, Helvetica, sans-serif'
        self.parts.append(f'<text x="{x}" y="{y}" fill="{self.c[color]}" font-family="{font}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}">{escape(value)}</text>')

    def path(self, d, color='line', width=1.5, arrow=False, extra=''):
        marker = ' marker-end="url(#arrow)"' if arrow else ''
        self.parts.append(f'<path d="{d}" fill="none" stroke="{self.c[color]}" stroke-width="{width}" stroke-linejoin="round" stroke-linecap="round"{marker}{extra}/>')

    def plate(self, cx, cy, w=84, depth=10, accent=False, floating=False):
        """Three closed faces form one isometric sheet."""
        h = w * .39
        self.parts.append(f'<g transform="translate({cx} {cy})">')
        if floating:
            self.parts.append('<g class="lift">')
        faces = [(f'M{-w} 0 0 {h}V{h+depth}L{-w} {depth}Z', 'front'),
                 (f'M0 {h} {w} 0V{depth}L0 {h+depth}Z', 'side'),
                 (f'M{-w} 0 0 {-h} {w} 0 0 {h}Z', 'top')]
        for d, fill in faces:
            self.parts.append(f'<path d="{d}" fill="{self.c[fill]}" stroke="{self.c["line"]}" stroke-width="1.1" stroke-linejoin="round"/>')
        self.path(f'M{-w} 0 0 {h} {w} 0', 'accent' if accent else 'line', 2)
        self.path(f'M{-w*.4} -2 -4 {w*.14}M{-w*.23} {-w*.09} {w*.26} {w*.1}', 'muted', 1.2)
        if floating:
            self.parts.append('</g>')
        self.parts.append('</g>')

    def finish(self):
        return '\n'.join(self.parts + ['</svg>\n'])


def render(kind, theme, mobile=False, motion=False):
    w, h = (420, 304) if mobile else (960, 224)
    s = Drawing(w, h, theme, TITLES[kind], DESCRIPTIONS[kind], motion)
    number = list(TITLES).index(kind) + 1
    s.text(24, 35, f'0{number} / OPEN SOURCE', 12, 'muted', mono=True)
    s.text(24, 78, TITLES[kind], 32 if mobile else 36, weight=600)
    s.text(24, 107, SUBTITLES[kind], 18, 'muted')
    if not mobile:
        s.path('M318 24V200', width=1)
    centers = (76, 210, 344) if mobile else (423, 635, 847)
    baseline = 214 if mobile else 139
    pw = 46 if mobile else 68
    for i, cx in enumerate(centers):
        s.path(f'M{cx-pw} {baseline+30}h{pw*2}', 'line', .7)
        if i < 2:
            start, end = cx+pw+5, centers[i+1]-pw-5
            s.path(f'M{start} {baseline-3}H{end}', 'accent', 1.5, arrow=True)
            if motion:
                s.path(f'M{start} {baseline-3}H{end}', 'ink', 2.5, extra=' class="signal"')
    if kind == 'gds':
        s.plate(centers[0], baseline-7, pw, accent=True)
        s.plate(centers[1], baseline+5, pw)
        s.plate(centers[1], baseline-15, pw, accent=True, floating=motion)
        for off in (12, -4, -20):
            s.plate(centers[2], baseline+off, pw, 6, accent=off == -20)
        labels, note = ('Source', 'Compile', 'Repositories'), 'Identity independent of paths'
    elif kind == 'ai-stp':
        for off in (10, -7, -24):
            s.plate(centers[0], baseline+off, pw, 6, accent=off == -24)
        s.plate(centers[1], baseline+7, pw)
        s.plate(centers[1], baseline-15, pw, accent=True, floating=motion)
        s.plate(centers[2], baseline-5, pw, 15, accent=True)
        labels, note = ('Select', 'Bundle', 'Provider'), 'CLI assembles · provider writes'
    else:
        s.plate(centers[0], baseline+5, pw)
        s.plate(centers[0], baseline-15, pw, accent=True, floating=motion)
        s.plate(centers[1], baseline-5, pw, 15, accent=True)
        s.plate(centers[2], baseline-5, pw, 15)
        s.path(f'M{centers[2]-12} {baseline-8}l8 7 17-14', 'accent', 3)
        labels, note = ('Back up', 'Apply', 'Verify'), 'Saved backups · explicit targets'
    for cx, label in zip(centers, labels):
        s.text(cx, baseline+61, label, 19, anchor='middle')
    s.text(24, 139 if mobile else 186, note, 14 if mobile else 15, 'muted')
    return s.finish()


def social():
    s = Drawing(1280, 640, 'dark', 'Danil Silantyev', 'AI Staff-level Engineer. CEO NDDev. AI systems, agent tooling and open source.')
    s.text(64, 90, 'RLDYOURMND / NDDEV', 22, 'accent', mono=True)
    s.text(64, 208, 'Danil', 78, weight=600)
    s.text(64, 299, 'Silantyev', 78, weight=600)
    s.text(64, 377, 'AI Staff-level Engineer', 30)
    s.text(64, 424, 'CEO NDDev', 28, 'muted')
    s.text(64, 565, 'GDS / ai-stp / Setup systems', 22, 'accent')
    for cy in (384, 302, 220):
        s.plate(966, cy, 210, 24, accent=cy == 220)
    return s.finish()


def expected_assets():
    assets = {}
    for kind in TITLES:
        for theme in THEMES:
            for mobile in (False, True):
                suffix = '-mobile' if mobile else ''
                assets[f'{kind}-{theme}{suffix}.svg'] = render(kind, theme, mobile)
            assets[f'{kind}-{theme}-motion.svg'] = render(kind, theme, motion=True)
    assets['social-preview.svg'] = social()
    return assets


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    parser.add_argument('--output', type=Path, default=ROOT/'assets/profile')
    args = parser.parse_args()
    assets = expected_assets()
    if args.check:
        changed = [name for name, data in assets.items()
                   if not (args.output/name).is_file() or (args.output/name).read_bytes() != data.encode()]
        changed += sorted(p.name for p in args.output.glob('*.svg') if p.name not in assets)
        if changed:
            print('SVG drift: ' + ', '.join(changed))
            return 1
        print(f'PASS: {len(assets)} SVG assets reproduce byte-for-byte.')
    else:
        args.output.mkdir(parents=True, exist_ok=True)
        for path in args.output.glob('*.svg'):
            if path.name not in assets and 'Generated by tools/render_profile.py' in path.read_text():
                path.unlink()
        for name, data in assets.items():
            (args.output/name).write_bytes(data.encode())
        print(f'Wrote {len(assets)} SVG assets.')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())

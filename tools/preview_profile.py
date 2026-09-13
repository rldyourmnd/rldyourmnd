#!/usr/bin/env python3
"""Preview the current READMEs using GitHub's Markdown API. Needs authenticated gh."""
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import argparse
import base64
import json
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
CSS_REPO = 'repos/sindresorhus/github-markdown-css/contents/github-markdown.css'
FRAME_CSS = '''body{margin:0;background:#fff}.frame{max-width:900px;margin:32px auto;padding:24px;border:1px solid #d1d9e0;border-radius:6px}.markdown-body{font-size:16px}.markdown-body img{height:auto}.review{font:12px monospace;margin-bottom:24px;color:#656d76}@media(max-width:767px){.frame{margin:0;padding:16px;border:0}}@media(prefers-color-scheme: dark){body{background:#0d1117}.frame{border-color:#3d444d}}'''


def gh(endpoint, data=None):
    command = ['gh', 'api', endpoint]
    if data is not None:
        command += ['--input', '-']
    return subprocess.run(command, input=json.dumps(data) if data is not None else None,
                          capture_output=True, text=True, check=True).stdout


def render(folder):
    folder.mkdir(parents=True, exist_ok=True)
    asset_link = folder/'assets'
    if not asset_link.exists():
        asset_link.symlink_to(ROOT/'assets', target_is_directory=True)
    css = base64.b64decode(json.loads(gh(CSS_REPO))['content']).decode()
    (folder/'github-markdown.css').write_text(css)
    for theme in ('light', 'dark'):
        themed = css.replace('(prefers-color-scheme: dark)', '(min-width:0px)' if theme == 'dark' else '(max-width:0px)')
        themed = themed.replace('(prefers-color-scheme: light)', '(min-width:0px)' if theme == 'light' else '(max-width:0px)')
        (folder/f'github-markdown-{theme}.css').write_text(themed)
    for name, lang in (('README.md', 'en'), ('README.ru.md', 'ru')):
        body = gh('markdown', dict(text=(ROOT/name).read_text(), mode='gfm', context='rldyourmnd/rldyourmnd'))
        body = body.replace('href="README.ru.md"', 'href="ru.html"').replace('href="README.md"', 'href="en.html"')
        page = f'<!doctype html><html lang="{lang}"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>NDDev profile review / {lang}</title><link rel="stylesheet" href="github-markdown.css"><style>{FRAME_CSS}</style><div class="frame"><div class="review">LOCAL PREVIEW / GitHub Markdown API / {lang.upper()}</div><article class="markdown-body">{body}</article></div></html>'
        (folder/f'{lang}.html').write_text(page)
        # Fixture overrides let the browser inspect every picture selection without changing account settings.
        for theme in ('light', 'dark'):
            themed = page.replace('(prefers-color-scheme: dark)', '(min-width:0px)' if theme == 'dark' else '(max-width:0px)')
            themed = themed.replace('href="github-markdown.css"', f'href="github-markdown-{theme}.css"')
            (folder/f'{lang}-{theme}.html').write_text(themed)
            for motion in ('reduce', 'no-preference'):
                variant = themed.replace('(prefers-reduced-motion: no-preference)', '(max-width:0px)' if motion == 'reduce' else '(min-width:0px)')
                (folder/f'{lang}-{theme}-{motion}.html').write_text(variant)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--port', type=int, default=8765)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--render-only', action='store_true')
    args = parser.parse_args()
    folder = args.output or Path(tempfile.mkdtemp(prefix='nddev-profile-'))
    render(folder)
    print(f'Preview files: {folder}', flush=True)
    if not args.render_only:
        print(f'http://127.0.0.1:{args.port}/en.html', flush=True)
        server = ThreadingHTTPServer(('127.0.0.1', args.port), partial(SimpleHTTPRequestHandler, directory=str(folder)))
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass
        finally:
            server.server_close()

if __name__ == '__main__':
    main()

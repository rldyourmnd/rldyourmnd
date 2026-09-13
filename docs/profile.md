# Maintaining this profile

Edit `README.md` and `README.ru.md` together. English is primary; language
navigation is visible beside the contact links. The owner's current positioning
is **AI Staff-level Engineer · CEO NDDev**. The audience is engineers, partners
and prospective employers. The page should lead to a conversation, the notes
channel, or the source of a useful project.

## Content

Keep the six primary languages and seven harnesses visible before the projects.
The agent workbench is plain Markdown, including CLIProxyAPI, skills, MCP, LSP,
Impeccable, Ponytail and `ctx`. The owner identifies `ctx` as an agent session
viewer; an upstream link remains unknown. Application technologies follow the
three main projects so the project links appear sooner.

GDS, ai-stp and setup systems are the selected work. ai-stp belongs to AI
Engineers Guild. nremote retains attribution as a RustDesk fork. Third-party
tools link to their own authors and are not presented as NDDev products.

The organization table describes GitHub ownership, not equity or sole authorship.
My Attention AI is listed as a separate organization; the owner's role there is
omitted at their request. NDDev Archive is a clearly labelled archive.

Client work is limited to exactly two names in each language. No links,
descriptions, architecture, screenshots, domains or metrics belong in that
section. This rule also applies to image prompts and alternative text.

## Artwork and motion

Four generated PNGs form one illustration family: light and dark panoramas,
plus separate compact compositions for phones. The originals retain their
metadata. Only the matching image loads on initial page display; each PNG is
under 2 MiB. Prompts and generation provenance are in [illustrations.md](illustrations.md).

Three isometric SVG diagrams have light/dark, mobile and desktop motion variants.
The full generated set contains 19 SVGs including the social-preview master.
SVG text is selectable when opened separately; all essential project identity
and links are also available in Markdown. The mobile breakpoint is 767 px.

Desktop motion uses six slow, eight-second cycles of a 9 px layer lift and a
signal moving along existing connectors. It finishes after 48 seconds. Mobile
and reduced-motion readers get static files. The motion SVGs also check the
system's reduced-motion preference internally. No JavaScript or remote images
are required by the published README. The artwork is a software metaphor, not
a hardware specification or an exhaustive product execution trace.

## Local checks

Python 3.10+, standard library only:

```sh
python3 tools/render_profile.py --check
python3 tools/check_profile.py
python3 -m unittest discover -s tests -v
```

To change a diagram, edit `tools/render_profile.py`, regenerate by running it
without `--check`, and run the checks. The renderer removes only obsolete assets
bearing its own previous generation marker. Do not hand-edit generated SVGs.

Checks cover reproducibility, references, passive SVG content, size budgets,
visible tools, organization links, attribution and the agreed client section.
They are not a general secret scanner or evidence of tool installation health.

The existing GDS files remain unchanged. The repository's GDS verification
command is undeclared: **NOT_PROVEN**. Passing these profile-specific checks
does not validate the GDS bundle or repair its pre-existing provenance drift.

## Browser review

The optional preview uses authenticated `gh`, GitHub's Markdown API and
[github-markdown-css](https://github.com/sindresorhus/github-markdown-css).
It sends only the two public README drafts to GitHub, writes preview files
outside the repository, and binds its local server to 127.0.0.1.

```sh
python3 tools/preview_profile.py
```

Open the printed URL. Use `en.html` and `ru.html` for the browser's real media
preferences. Files such as `en-dark-reduce.html` override media queries in the
local fixture to exercise source selection; they do not change browser or
account settings. They are not proof of an actual OS preference change.

Check 320/390/768/1440 px, both languages, both themes, motion/static selection,
image loading, table overflow and SVG labels. A local preview uses GitHub's
Markdown sanitizer but is not the hosted profile. Review the final branch on
GitHub too. Profile display on the main account changes only after merge.

## Account fields outside the PR

Prepared values, not applied account settings:

- Bio: `AI Staff-level Engineer · CEO @NDDev-it-com. AI systems, agent tooling and infrastructure. I design the architecture and write the code.`
- Repository description: `Danil Silantyev · AI Staff-level Engineer · CEO NDDev. AI systems, agent tooling and open-source projects.`
- Website: `https://nddev.it.com`
- Contact: `danil@nddev.it.com`
- Notes channel: `https://t.me/rldyourmnd`

Suggested pin order: `NDDev-OpenNetwork/github-device-sync`,
`ai-engineers-guild/ai-stp`, `NDDev-OpenNetwork/codex-setup-system`,
`NDDev-OpenNetwork/ci-workflows`, `NDDev-OpenNetwork/agent-runtime`,
`NDDev-OpenNetwork/nremote`. Check eligibility in the profile UI; organizational
ownership alone does not establish eligibility. Avoid seven near-identical pins.

`assets/profile/social-preview.svg` is the editable 1280 × 640 master.
`assets/profile/social-preview.png` is its ready-to-upload raster export. Neither
has been applied to account settings. To export again:

```sh
uv run --with cairosvg python -c 'import cairosvg; cairosvg.svg2png(url="assets/profile/social-preview.svg",write_to="assets/profile/social-preview.png")'
```

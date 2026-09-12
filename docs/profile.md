# Maintaining this profile

The public page is `README.md`. `README.ru.md` is its parallel translation,
linked inside collapsed navigation on the English page. Edit both together.

## Content order

Identity and contacts come first. The visible workbench follows: languages,
seven coding harnesses, agent tooling and the application stack. Then come
GDS, ai-stp, setup systems, NDDev, the names-only client section and contact.
Do not remove the stack or move it into images, comments or collapsed details
in pursuit of a shorter README. The tools are part of the owner's identity.

Keep tools used separate from projects authored. CLIProxyAPI, Impeccable and
Ponytail link to their upstream authors; they are not presented as NDDev work.
ai-stp is attributed to AI Engineers Guild. The named harnesses describe the
owner's working set, not equal support for every extension on every harness.

Client projects have a strict presentation boundary. The English section is
exactly two plain-text names; the Russian version contains their translations.
Do not add implementation notes, links, domains, screenshots, metrics, client
contacts or operational details. General stack information belongs in the
workbench and is not attributed to either client project.

See [content sources](content-sources.md) for provenance and the unresolved
`ctx` identifier. Do not guess its expansion or upstream URL.

## Design

Four code-drawn SVG plates cover GDS, ai-stp, configuration recovery and NDDev's
six divisions. Each has light/dark versions and a separate mobile composition.
The `<picture>` breakpoint is 640 CSS pixels. All 19 assets, including motion
variants and the social-preview master, remain unchanged by the stack revision.

Project descriptions, stack names and contact links are ordinary Markdown.
No essential content is available only inside an image. Images have alternative
text plus an SVG title and description. No generated photos, external fonts,
image services, tracking pixels or live counters are used.

Desktop GDS connectors have a single 3.6-second accent animation. Existing
paths remain visible; mobile and reduced-motion visitors receive static files.
The motion SVG also contains a CSS preference check. A renderer that ignores
animation still displays the complete diagram.

GitHub sanitizes README HTML. Styling belongs in image files, not README
`style`, `script`, `iframe` or inline SVG elements. Keep relative image paths
so a branch previews its own assets. The workbench uses native Markdown tables.

References:
- [GitHub's image theme pattern](https://github.blog/developer-skills/github/how-to-make-your-images-in-markdown-on-github-adjust-for-dark-mode-and-light-mode/)
- [GitHub Markup rendering pipeline](https://github.com/github/markup#github-markup)
- [SVG image-context restrictions](https://developer.mozilla.org/en-US/docs/Web/SVG/Guides/SVG_as_an_image)

## Change and verify

Python 3.10 or newer. Standard library only, with no installation or network step.

```sh
python3 tools/render_profile.py --check
python3 tools/check_profile.py
python3 -m unittest discover -s tests -v
```

To change a drawing, edit `tools/render_profile.py`, run it without `--check`,
then run the commands above. Generated SVGs must reproduce byte-for-byte.

`check_profile.py` covers local links, image alternatives, passive SVG content,
size budgets and hidden Russian navigation. It calls `check_workbench.py` for
visible language/tool coverage, exactly seven named harnesses, verified upstream
link spelling and the names-only client section. The regression tests exercise
both languages, including missing or hidden tools and accidental case details.

These are editorial regression checks, not a general secret scanner, a proof of
NDA compliance, a live installation inventory or product-runtime tests. When the
owner changes the working set, update its explicit expectations rather than
freezing an obsolete list. Checks stay local; no scheduled generation or new
Actions workflow is added.

Existing GDS-managed `AGENTS.md` and `.gds/` files are intentionally unchanged.
These profile checks do not validate or replace the GDS bundle contract.

## Browser review

Review the branch on GitHub as well as locally. Check light/dark modes,
320/390/768/1440 CSS pixel widths, reduced motion, both languages, image-disabled
readability and the collapsed language link. Verify that the tables fit without
horizontal scrolling and that the correct image variant is selected.

A local Markdown preview does not prove GitHub's current sanitizer or a signed-in
user's theme settings. The latest local QA was repeated for the stack revision;
no previous execution result should be treated as a test of a changed file.

## Account fields outside the PR

README changes do not update account settings or pinned repositories.
Prepared values, not claims that they have been applied:

**Name:** Danil Silantyev

**Bio:**

> AI Staff Engineer · Systems & AI Architect. OSS developer & contributor. CEO @NDDev-it-com. Rust, Python, Go, C/C++, TypeScript, Dart.

**Repository description:**

> Danil Silantyev: AI systems, agent tooling, engineering stack and open-source work.

**Website:** `https://nddev.it.com`

**Contact:** `danil@nddev.it.com`

**Pin order:** `NDDev-OpenNetwork/github-device-sync`,
`ai-engineers-guild/ai-stp`, `NDDev-OpenNetwork/codex-setup-system`.
Pin eligibility must be checked in the account UI. Do not fill every slot with
near-identical providers.

`assets/profile/social-preview.svg` is the editable 1280 x 640 master, not an
applied repository setting. Export to PNG before the social-preview upload.
See [GitHub's upload requirements](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/customizing-your-repositorys-social-media-preview).

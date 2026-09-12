# Maintaining this profile

The public page is `README.md`. `README.ru.md` is a parallel translation, linked
only inside a collapsed section on the English page. Edit both together.

## Design

Four original, code-drawn SVG plates explain four subjects: GDS, ai-stp,
configuration recovery and NDDev's six divisions. There are no generated photos,
stock icons, invented logos, external fonts, tracking pixels or live counters.
Project descriptions and contact links remain ordinary Markdown; no essential
information exists only inside an image.

Each drawing has a light and a dark version and a separate mobile composition.
The `<picture>` breakpoint is 640 CSS pixels. This is art direction, not a
shrunk desktop screenshot. Essential diagram labels are large; small numbers
are decorative. All images have alternative text and SVG title/description.

On desktop, the GDS connectors carry one 3.6-second accent animation, then stop.
Existing paths stay visible throughout. Mobile and reduced-motion visitors get
a different, strictly static file selected by `<picture>`. The animation also
contains a CSS motion preference as a secondary safeguard, not the primary
control. No scripts are embedded. Renderers that ignore animation still get
the complete static drawing.

GitHub sanitizes README HTML. Keep styling in the image files, not in README
`style`, `script`, `iframe` or inline SVG elements. Use local relative image
paths so branches preview their own assets.

References:
- [GitHub's image theme pattern](https://github.blog/developer-skills/github/how-to-make-your-images-in-markdown-on-github-adjust-for-dark-mode-and-light-mode/)
- [GitHub Markup rendering pipeline](https://github.com/github/markup#github-markup)
- [SVG image-context restrictions](https://developer.mozilla.org/en-US/docs/Web/SVG/Guides/SVG_as_an_image)

## Change and verify

Python 3.10 or newer, standard library only. No install step or network access.

```sh
python3 tools/render_profile.py
python3 tools/check_profile.py
python3 -m unittest discover -s tests -v
```

`render_profile.py` is the drawing source. Its `--check` option compares all
expected SVG bytes without writing anything and rejects extra SVG files.
`check_profile.py` also checks links, image alternatives, passive SVG content,
asset budgets and the hidden Russian navigation. It is not a runtime test of
the featured projects and makes no availability claim about remote links.

No scheduled regeneration or new Actions workflow is needed. Change the profile
when the work changes. Do not auto-publish an activity feed, commit counts,
unverified metrics or a version copied from a moving release page.

The existing GDS-managed `AGENTS.md` and `.gds/` files are intentionally left
unchanged. These local profile checks do not claim GDS bundle validation and
do not replace its canonical verification contract.

## Browser review

Review the branch README on GitHub, not just a local Markdown renderer.
Check desktop and mobile widths, light/dark modes, reduced motion, keyboard
navigation and image-disabled readability. A local preview is not proof of
GitHub's current HTML sanitization or an authenticated user's theme settings.

`assets/profile/social-preview.svg` is the editable 1280 x 640 master. Export it
to PNG for the repository's social preview. GitHub's Settings upload accepts
PNG/JPG/GIF under 1 MB; committing the SVG does not set that account option.
See [GitHub's social-preview documentation](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/customizing-your-repositorys-social-media-preview).

## Account fields outside this PR

A README commit does not change profile settings or pinned repositories.
Prepared values, not claims that these settings have already been applied:

**Name:** Danil Silantyev

**Bio:**

> AI Staff Engineer · Systems & AI Architect. OSS developer & contributor. CEO @NDDev-it-com. Building AI systems and developer tools.

**Repository description:**

> Danil Silantyev: AI systems, developer tools and open-source work.

**Website:** `https://nddev.it.com`

**Primary contact:** `danil@nddev.it.com`

**Pin order:** GDS (`NDDev-OpenNetwork/github-device-sync`), ai-stp
(`ai-engineers-guild/ai-stp`), then `NDDev-OpenNetwork/codex-setup-system`.
Do not fill every slot with near-identical providers. GitHub pin eligibility
must be checked in the account UI; a recommendation is not an applied setting.

## Content provenance

Editorial review: 2026-09-12. Roles, personal contribution to ai-stp, project
selection and public contact details were confirmed by the profile owner.
Descriptions are deliberately narrower than marketing claims or roadmap goals.
No team counts, runtime guarantees, awards or career-duration counters are used.

The following public source files were read. Blob hashes identify the content
reviewed; the links lead to the projects' current documentation.

| Subject | Source | README blob SHA |
| --- | --- | --- |
| GDS's canonical source, compiler, bundle and local projections | [README](https://github.com/NDDev-OpenNetwork/github-device-sync/blob/main/README.md), `Canonical model` | `4e46fd750780a1c0aac13c69653abae175fc0581` |
| ai-stp CLI/provider boundary and exact versions | [README](https://github.com/ai-engineers-guild/ai-stp/blob/main/README.md), `CLI assembles, the provider writes` | `f154f9b7f2a171864ef55dc5cd462d43cdeb0194` |
| Explicit targets, pre-change backup and restoration | [README](https://github.com/NDDev-OpenNetwork/codex-setup-system/blob/main/README.md), `Using it` / `Four setups` | `0c8e7e839e1a2f2c2467e97527e3153ad158497f` |

The setup drawing is a relationship diagram, not a trace of every execution
step. Backup branches from the target; restore points back to it. It does not
invent a second protocol or claim every verification automatically restores.

ai-stp is attributed to AI Engineers Guild, not presented as an NDDev asset.
Client source code, private repository coordinates and operational material
are not part of this public profile.

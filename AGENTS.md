<!--
GENERATED FILE — DO NOT EDIT DIRECTLY
generator: gds
bundle: 0.1.0-dev
source-commit: 96c240d6750a912a1c7b516fd474c051d247e8c3
input-digest: sha256:9930ef5cea6dd5be14463a1ae3ef8c727e0c4919166c7e487a43377e55173919
output-digest: sha256:342d720647dd051899bcf1b22c8762aed9fc13c97d34a363252d7c97f25e39b1
edit-source:
  - .gds/repository.yaml
  - policies/base/repository-default.yaml
  - policies/owners/personal-default.yaml
  - templates/agents/repository.md.tmpl
  - templates/github-actions/go.yml.tmpl
  - templates/harnesses/claude.md.tmpl
-->
# GDS repository contract

## Scope

- Repository ID: `repo_01KX8PR8BJEJWWKWFVBAV50C74`.
- Roles: `docs`.
- Canonical repository facts: `.gds/repository.yaml`.
- Applied bundle: `.gds/bundle.lock.yaml` (`0.1.0-dev`).
- Compiled policy: `.gds/compiled-policy.json`.

## Boundaries

- This Git repository is one independent mutation boundary.
- Preserve unrelated branches, worktrees, submodules, and dirty changes.
- Resolve cross-repository work with `gds context --json` before acting.
- Generated files are projections; change their canonical inputs and regenerate.

## Safety

- External writes require explicit approval: `true`.
- Generated projection edits: `forbidden`.
- Private parent context persistence: `forbidden`.
- Visibility contract: `public`; data classification: `public`.

## Development

- No repository-owned verification command is declared; report it as `NOT_PROVEN`.

## Agent routing

- Active skill profiles: `core`.
- Use on-demand skills for procedures; do not duplicate them here.
- Treat docs and memories as derived evidence, not mutation authority.

## Done

- Required verification is complete or explicitly `NOT_PROVEN`.
- Git state and every affected repository boundary are classified.
- No private data, secret, or unapproved generated drift is introduced.

<!--
GENERATED FILE - DO NOT EDIT DIRECTLY
generator: gds
bundle: 0.1.0-dev
source-commit: 5912c2259c99ac300eaea6b6d7b982eefd90a854
input-digest: sha256:49608a980f1c64716a6f594a6ef130e03fa54a0a201c78ff6bc01dcc909934c5
output-digest: sha256:331c08df824341aabc6201a2c0936a3652fc60eedd12f87dbeb2d79233714fd6
edit-source:
  - .gds/repository.yaml
  - policies/base/repository-default.yaml
  - policies/owners/personal-default.yaml
  - templates/agents/repository.md.tmpl
  - templates/github-actions/go.yml.tmpl
  - templates/harnesses/claude.md.tmpl
-->
# Claude Code repository contract

## Scope

- GDS repository ID: `repo_01KX8PR8BJEJWWKWFVBAV50C74`.
- Roles: `docs`.
- Canonical repository facts: `.gds/repository.yaml`.
- Applied policy bundle: `.gds/bundle.lock.yaml` (`0.1.0-dev`).
- This is a first-class Claude Code projection compiled from the same typed
  inputs as `AGENTS.md`; neither projection is a manual policy source.

## Repository boundaries

- Treat this Git repository as one independent mutation boundary.
- Preserve unrelated dirty changes, branches, worktrees, and submodules.
- Run `gds context --json` before work crosses repository boundaries.
- Do not edit generated projections; change the declared canonical input and
  regenerate.

## Safety

- External writes require explicit approval: `true`.
- Generated projection edits: `forbidden`.
- Private parent context persistence: `forbidden`.
- Visibility: `public`; data: `public`.

## Verification commands

- No repository-owned verification command is declared; report it as
  `NOT_PROVEN`.

## Claude workflow routing

- Start here: run `gds-orient` (or `gds context --json`) to resolve scope before
  any cross-repository work.
- Active skill profiles: `core`. Five profiles exist in total
  (`core`, `estate-admin`, `module`, `device`, `portfolio`); only the listed ones
  are active for this repository. The catalog is `skills/registry.yaml`, and each
  skill lives under `skills/canonical/<name>/SKILL.md`.
- Load procedural detail from the applicable installed GDS skill projection or
  plugin only when the task matches it.
- Destructive workflows remain explicit-only and still require their concrete
  plan and approval gates.
- Treat documentation and Serena memories as derived evidence, never mutation
  authority.

## Done

- Required checks pass or are explicitly reported `NOT_PROVEN`.
- Every affected Git boundary and remote result is classified.
- No secret, private-context leak, unrelated change, or unapproved projection
  drift is introduced.

<!--
GENERATED FILE - DO NOT EDIT DIRECTLY
generator: gds
bundle: 0.1.0-dev
source-commit: bb9865d7d52e72787ad8f95ab7e70a0869d784aa
input-digest: sha256:f530d3e6e8edf694431d177e303f864a924e1d5d4b29bfd908bcea03726c4217
output-digest: sha256:d33939063be58f5db2507f5f9c0687f4ce90b80cd2ba50e90d026df713976823
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

- Active skill profiles: `core`.
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

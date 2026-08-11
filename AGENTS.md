<!--
GENERATED FILE - DO NOT EDIT DIRECTLY
generator: gds
bundle: 0.4.0-dev
source-tree-digest: sha256:9875a1ff737c3fb6740d1a1aadc1ab9f4cd31e0f7dbc561f47c784b99676da33
input-digest: sha256:f9ded39b047ca4f5ede0849f696d1093fa3dda3e373430f5d4df0b41a9e9905c
output-digest: sha256:6093de7df79e1a1e7eaf5b07467c12016ad3bb5e63e4078a846a1dc33b7a6fc5
edit-source:
  - .gds/repository.yaml
  - policies/base/repository-default.yaml
  - policies/owners/personal-default.yaml
  - templates/agents/repository.md.tmpl
  - templates/github-actions/go.yml.tmpl
  - templates/harnesses/claude.md.tmpl
-->
# Repository brief

## How to verify

- No repository-owned verification command is declared; report `NOT_PROVEN`.

## Working here

- Generated files carry a `GENERATED FILE` header. Change the canonical input
  named in `edit-source` and regenerate; editing the output detaches it from
  `.gds/bundle.lock.yaml`.
- One Git repository is one mutation boundary. Work that crosses repositories
  starts with `gds context --json`; work inside this one does not need it.
- Provider writes go through plan → approve → apply and are journaled.
- Task-specific procedures live in `skills/canonical/<name>/SKILL.md`; the
  profiles active here are `core`. Load one when the task
  matches it.

## Facts

- Repository `repo_01KX8PR8BJEJWWKWFVBAV50C74`, roles `docs`, bundle `0.4.0-dev`.
- Canonical inputs: `.gds/repository.yaml`; compiled result: `.gds/compiled-policy.json`.
- Visibility `public`, data `public`.

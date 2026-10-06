<!--
GENERATED FILE - DO NOT EDIT DIRECTLY
generator: gds
bundle: 0.9.24
source-tree-digest: sha256:921ee3191bc61d3ef99c7c0bd7a6b893a6df35610c65c3be10e979aef20cff73
input-digest: sha256:1c49543e78a0cc71b3d2e32faddc1f62d636bec600216ec82b51fd3b9d0459f3
output-digest: sha256:b4118bc9b15a7fd6c6a4ddfabc451b04da64520523b06f18537bf38abdda66ad
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

- Repository `repo_01KX8PR8BJEJWWKWFVBAV50C74`, roles `docs`, bundle `0.9.24`.
- Canonical inputs: `.gds/repository.yaml`; compiled result: `.gds/compiled-policy.json`.
- Visibility `public`, data `public`.

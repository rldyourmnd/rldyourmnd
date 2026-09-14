<!--
GENERATED FILE - DO NOT EDIT DIRECTLY
generator: gds
bundle: 0.9.4-dev
source-tree-digest: sha256:b1c334df899c661304dc45ef29898df24ff4a6ddffd2a6ca4d6f1f795d585189
input-digest: sha256:cf9b754bbb38ad3d3ac29b2b47da56166ed6da15519867f6d317d8b39661dde4
output-digest: sha256:127c3730d1032edd2677b696ff83678b95986bfc6e81797ac1f7cda4459e926e
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
  profiles active here are `core, drakkars`. Load one when the task
  matches it.

## Facts

- Repository `repo_01KX8PR8BJEJWWKWFVBAV50C74`, roles `docs`, bundle `0.9.4-dev`.
- Canonical inputs: `.gds/repository.yaml`; compiled result: `.gds/compiled-policy.json`.
- Visibility `public`, data `public`.

<!--
GENERATED FILE - DO NOT EDIT DIRECTLY
generator: gds
bundle: 0.9.7-dev
source-tree-digest: sha256:6944618359758df76e230e0ba2edc12f342944d25479d445884231d4a3fc8cb1
input-digest: sha256:00e36b02ab2c89758bf9320f548b893ef9cffcb02a3d136fbb9edeb55da2a425
output-digest: sha256:0d0e7dc0616248b315907cd6897c0aa2209c2a366fea010f56fcc4d029bb0451
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

- Repository `repo_01KX8PR8BJEJWWKWFVBAV50C74`, roles `docs`, bundle `0.9.7-dev`.
- Canonical inputs: `.gds/repository.yaml`; compiled result: `.gds/compiled-policy.json`.
- Visibility `public`, data `public`.

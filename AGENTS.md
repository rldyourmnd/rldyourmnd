<!--
GENERATED FILE - DO NOT EDIT DIRECTLY
generator: gds
bundle: 0.9.4-dev
source-tree-digest: sha256:ba597010d9403127df8c67102186ef40c546a08101d1a93201d17f8108deb520
input-digest: sha256:11a1ffac48a4f18642bec9dffb744efe4f1d5cb23f50a584c79c61daf1a0a5a6
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

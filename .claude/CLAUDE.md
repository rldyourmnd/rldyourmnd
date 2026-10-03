<!--
GENERATED FILE - DO NOT EDIT DIRECTLY
generator: gds
bundle: 0.9.7-dev
source-tree-digest: sha256:6944618359758df76e230e0ba2edc12f342944d25479d445884231d4a3fc8cb1
input-digest: sha256:00e36b02ab2c89758bf9320f548b893ef9cffcb02a3d136fbb9edeb55da2a425
output-digest: sha256:88cb57297d8d713287872a8afaca8d42f7146ecf7a091e4996e65eee8f962665
edit-source:
  - .gds/repository.yaml
  - policies/base/repository-default.yaml
  - policies/owners/personal-default.yaml
  - templates/agents/repository.md.tmpl
  - templates/github-actions/go.yml.tmpl
  - templates/harnesses/claude.md.tmpl
-->
@AGENTS.md

# Claude Code delta

`AGENTS.md` above is the repository brief and is imported, not restated. This
file carries only what differs for Claude Code.

- Skills load on task match, not on arrival. A task contained in this repository
  goes straight to the relevant source and its verification command; `gds-orient`
  is for estate, device, topology and cross-repository scope.
- Serena memories under `.serena/memories/` are derived evidence. Their status
  records that sources were current and the body is the reviewed one; it does not
  certify the prose is correct.
- Prefer the repository's own commands over ad-hoc equivalents, so a failure is
  reproducible from the brief alone.

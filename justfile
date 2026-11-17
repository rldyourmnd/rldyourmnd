set shell := ["bash", "-euo", "pipefail", "-c"]

# Lists the commands.
default:
    @just --list

# Checks reproducible profile assets and workflow safety without network access.
check:
    just --fmt --check
    python3 -B tools/render_profile.py --check
    actionlint
    zizmor --offline --no-progress .github

# Runs every source check and the retained full-history secret scan.
verify: check
    gitleaks git --no-banner --redact .

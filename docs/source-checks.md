# Source checks

Run `just check` for the offline profile-source gate. It reproduces the existing
19 SVG files from `tools/render_profile.py` in memory, compares their exact bytes,
and checks the workflows with actionlint and zizmor.

`just verify` adds the existing full-history gitleaks scan. CI checks pull-request
changes through the shared security merge stops and runs full verification on
accepted main. The scheduled security workflow retains the shared daily report.
The shared job prepares the declared Python and zizmor selections. It prepares
actionlint and gitleaks through `.github/source-tools.json`, which binds the
existing official Linux x64 archives and executable members to exact asset IDs,
sizes and SHA-256 digests. There are no custom download commands in this
repository.

The profile has no application test or build command. These checks do not change
profile assets, compile generated policy, query remote links or verify account
settings. The separate historical Python regression files remain unchanged; this
maintenance does not claim their execution or current product coverage.

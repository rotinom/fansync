# PyPI Release Checklist for open-fansync

## One-time setup
- [x] Package name: `open-fansync` (import name `open_fansync`)
- [x] `pyproject.toml` with hatchling build, metadata, and dependencies
- [x] License: GPL-2.0-only, matching `LICENSE`
- [x] Clean public API in `open_fansync/__init__.py`
- [x] `README.md` renders as the PyPI long description (`twine check` passes)
- [x] GitHub workflow: `.github/workflows/publish-to-pypi.yml`
- [x] Dry-run upload to TestPyPI
- [ ] PyPI pending publisher: project `open-fansync`, owner `rotinom`, repo `fansync`,
      workflow `publish-to-pypi.yml`, environment `pypi`
- [ ] GitHub environment named `pypi` (Settings → Environments)

## Each release
- [ ] Commit and push to `main`
- [ ] Create a GitHub Release with a new tag like `v0.1.1`; the workflow builds and publishes

The version comes from the git tag (hatch-vcs), so there is no version number to edit.
Builds from an untagged commit get a dev version (e.g. `0.1.1.dev3+gabc123`) that
PyPI will not accept.

## Local build check
```
python -m build
twine check dist/*
```

## Someday
- [ ] Add tests (`test/` only holds captured JSON samples)
- [ ] Run tests in CI

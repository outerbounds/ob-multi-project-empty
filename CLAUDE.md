# Multi-Project Template

Monorepos with multiple ML systems need shared CI authentication but independent project deployment. This template shows the multi-project pattern: one `obproject_multi.toml` at the root for shared CI config, with each sub-project having its own `obproject.toml`, flows, and deployments.

## Architecture

```
repo/
  obproject_multi.toml          # Shared: CI auth (user, platform, perimeter)
  ml-infra/
    obproject.toml              # Project-specific config
    flows/
  batch-inference/
    obproject.toml
    flows/
  services/
    obproject.toml
    deployments/
```

`obproject-deploy` detects `obproject_multi.toml`, iterates over all sub-projects, deploys each independently.

## Platform features used

- **Multi-project layout**: `obproject_multi.toml` with `[cicd]` section (shared auth) + `[projects]` section (sub-project paths)
- **Independent sub-projects**: Each has its own `obproject.toml` with project name, platform, and optional branch/environment config
- **Shared CI auth**: One service principal authenticates for all sub-projects via `--from-obproject-toml --toml-path obproject_multi.toml`

## CI strategy

Three CI providers configured — GitHub Actions, Azure DevOps, CircleCI. All use `--from-obproject-toml --toml-path obproject_multi.toml` for auth. The `[cicd]` section in `obproject_multi.toml` provides user, platform, and perimeter.

This repo demonstrates that the same `--from-obproject-toml` pattern works for multi-project repos across all CI providers — the flag reads from the `[cicd]` section automatically.

## Run locally

```bash
# Deploy all sub-projects
obproject-deploy

# Or work on a single sub-project
cd ml-infra
python flows/<name>/flow.py run
```

## Verification

- [ ] GitHub Actions: push to main → all 3 sub-projects deploy
- [ ] Azure Pipelines: push to main → all 3 sub-projects deploy
- [ ] CircleCI: push to main → all 3 sub-projects deploy
- [ ] Each sub-project's flows appear in Outerbounds UI under their respective project names

## Good to know

- `obproject_multi.toml` is only for CI auth. Each sub-project's `obproject.toml` still controls its own platform, branch config, assets, etc.
- The service principal name in `[cicd].user` must have permissions to deploy to all sub-projects.
- `--toml-path obproject_multi.toml` tells `--from-obproject-toml` to read the multi-project file instead of `obproject.toml`.
- Sub-projects can be on different platforms if needed, but the CI auth uses the shared `[cicd].platform`.

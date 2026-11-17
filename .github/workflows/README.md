# 🐙 GitHub Workflow Index

| Workflow | Trigger | Purpose |
|---|---|---|
| quality.yml | Push, pull request, manual | Exercise structure, documentation links, and Markdown checks |
| docs-validation.yml | Push, pull request, manual | Documentation and repository structure validation |
| security-scan.yml | Push, pull request, manual | Limited private-key marker heuristic |
| stale.yml | Weekly schedule, manual | Stale issue and PR triage |

## Security notes
- Validation jobs use read-only repository permissions.
- The stale workflow requires issue and pull-request write permissions to apply labels and close inactive items.
- No deployment workflow exists because no production host is configured.
- No build or package audit workflow exists because the repository has no package manifest or build system.

Inspect workflow runs in the GitHub Actions tab before claiming a check passed.

# 📦 Dependency Security

## Current dependency surface
The HTML exercise pages do not import third-party JavaScript packages. There is no package manifest or lockfile. GitHub Actions are the only expected external automation dependencies when workflows are configured.

## Review guidance
- Use trusted actions and review their source.
- Prefer immutable commit references for high-assurance workflows.
- Keep action permissions minimal.
- Enable Dependabot for GitHub Actions updates.
- Avoid adding a package ecosystem workflow when no manifest exists.
- Reassess this policy if npm or another package manager is introduced.

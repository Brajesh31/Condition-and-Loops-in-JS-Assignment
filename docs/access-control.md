# 🚪 Access Control

## Application
The static exercise pages do not gate access. Anyone with a local copy can open them in a browser. There are no application roles or protected actions.

## Repository
Repository access is controlled by GitHub account and repository permissions. Maintainers should grant write access only to trusted collaborators and review all external pull requests before merging.

## Workflow permissions
GitHub Actions should request only the permissions needed for the job. Validation workflows should remain read-only.

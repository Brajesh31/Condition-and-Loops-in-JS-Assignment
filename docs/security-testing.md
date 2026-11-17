# 🧪 Security Testing

## Current checks
The repository does not contain a dedicated security test suite. The static examples use hard-coded values and no remote input.

## Manual review checklist
- [ ] No credentials or personal data in changed files.
- [ ] No new unnecessary external scripts.
- [ ] No string-based dynamic code execution.
- [ ] Any future user input is validated.
- [ ] GitHub workflow permissions are least-privilege.
- [ ] New dependencies and actions are reviewed.

## Reporting
Use the private process in [SECURITY.md](../SECURITY.md). Do not mark a security scan as passing unless an actual scanner has run and produced a successful result.

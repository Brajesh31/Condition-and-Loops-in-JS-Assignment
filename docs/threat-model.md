# 🛡️ Threat Model

## Assets
- Source code and educational examples.
- Repository integrity and contributor permissions.
- GitHub workflow credentials and repository tokens, if used by automation.
- Learner privacy in issue reports.

## Relevant threat scenarios
| Threat | Likelihood context | Mitigation |
|---|---|---|
| Accidental secret commit | Repository-wide risk | Secret scanning and immediate rotation |
| Malicious pull request | Open-source contribution risk | Review diffs before merging |
| Compromised third-party action | Workflow supply-chain risk | Pin and review actions; least privilege |
| Unsafe future user input | Only if interactive input is added | Validate and safely render values |
| Misleading docs or badges | Documentation integrity | Verify claims against source and CI |
| Private data posted in an issue | Community workflow | Warn reporters and use private security channel |

## Not currently applicable
There is no login flow, authorization model, API attack surface, database, session cookie, payment flow, or personal-data store.

## Review cadence
Revisit this model if the project adds remote services, user input, third-party scripts, or privileged workflows.

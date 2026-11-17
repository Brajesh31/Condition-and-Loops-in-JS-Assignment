# 🔐 Secret Management

## Current state
The assignment has no runtime secrets, environment variables, API credentials, or private service integrations. The root `.env.example` documents this explicitly.

## If a secret is exposed
1. Revoke or rotate it immediately at the issuing service.
2. Identify where it was used and whether it was accessed.
3. Remove it from active code and configuration.
4. Follow GitHub's guidance for sensitive history cleanup if necessary.
5. Review logs and downstream copies.
6. Record remediation without repeating the secret.

Never treat deletion from the latest commit as proof that a secret is safe.

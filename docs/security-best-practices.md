# 🔒 Security Best Practices

## Repository hygiene
- Never commit secrets, private keys, tokens, or personal data.
- Review changes to workflows and permissions.
- Keep GitHub Actions updated and trusted.
- Use the minimum permissions needed by automation.
- Avoid adding remote scripts to simple educational pages.

## JavaScript examples
- Do not use `eval` for beginner input parsing.
- Treat future user input as untrusted.
- Validate numeric input before comparisons.
- Use `textContent` rather than unsafe HTML insertion when rendering text.
- Avoid logging private values.

## Reporting
Use the private reporting route in [SECURITY.md](../SECURITY.md) for vulnerabilities. Public issues are appropriate for ordinary bugs and documentation corrections.

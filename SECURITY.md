# 🔒 Security Policy

## 📦 Scope and supported versions
The repository is a static educational assignment with five HTML files and embedded JavaScript. The current examples use hard-coded values and browser console output. There is no server-side application, authentication, database, API, or secret-management service. The default branch is the maintained source.

## 🧭 Security expectations
- Do not commit API keys, passwords, tokens, private data, or personal contact details.
- Keep third-party scripts and external dependencies out unless a clear educational need exists.
- Do not use `eval` or construct executable code from untrusted strings.
- If future exercises accept user input, validate it and avoid inserting untrusted values as HTML.
- Review new workflows for least-privilege permissions and trusted action versions.
- Keep dependencies and GitHub Actions updated when introduced.

## 🚨 Reporting a vulnerability
Please do not publish exploitable details in a public issue. Contact the repository owner privately using the contact route on the GitHub profile. Include:
1. Affected file, commit, or workflow.
2. Reproduction steps and a minimal proof of concept.
3. Potential impact and realistic attack prerequisites.
4. Suggested mitigation, if known.

Do not include secrets belonging to you or another person in the report.

## 🔍 Triage and disclosure
The maintainer will acknowledge and review reports as availability permits, validate the issue, assess impact, and decide whether a correction is required. A fix may be published with a concise security note. Coordinated disclosure is preferred so users can update before exploit details become public.

## ⏱️ Response expectations
This is a small educational repository maintained on a best-effort basis. No guaranteed response or remediation SLA is currently offered. For urgent exposure of a credential, revoke or rotate it immediately at the issuing service.

## 🧯 Incident response
1. Preserve relevant commit and workflow evidence.
2. Identify affected files and versions.
3. Remove exposed secrets from active code and rotate credentials.
4. Correct the issue and validate the change.
5. Document user impact and remediation without reproducing sensitive values.

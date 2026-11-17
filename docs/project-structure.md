# 📁 Complete Project Structure

This tree reflects the repository's actual tracked file layout. It includes the original assignment files and the documentation/governance additions.

```text
.
├── .github/
│   ├── CODEOWNERS
│   ├── FUNDING.yml
│   ├── dependabot.yml
│   ├── ISSUE_TEMPLATE/
│   │   ├── accessibility_report.yml
│   │   ├── bug_report.yml
│   │   ├── config.yml
│   │   ├── documentation.yml
│   │   ├── feature_request.yml
│   │   ├── performance_issue.yml
│   │   └── security_report.yml
│   ├── DISCUSSION_TEMPLATE/
│   │   ├── announcements.yml
│   │   ├── ideas.yml
│   │   └── questions.yml
│   ├── workflows/
│   │   ├── README.md
│   │   ├── docs-validation.yml
│   │   ├── quality.yml
│   │   ├── security-scan.yml
│   │   ├── stale.yml
│   │   └── update-readme.yml
│   └── PULL_REQUEST_TEMPLATE.md
├── Assignment_19_Conditions and Loops in JavaScript/
│   ├── asset/
│   │   ├── asset4.png
│   │   ├── asset5.png
│   │   ├── asset6.png
│   │   ├── asset7.png
│   │   ├── asset_1.png
│   │   ├── asset_2.png
│   │   └── asset_3.png
│   ├── OutPut/
│   │   ├── q1.png
│   │   ├── q2.png
│   │   └── q3.png
│   ├── Q1.html
│   ├── Q2.html
│   ├── Q3.html
│   ├── Q4.html
│   └── Q5.html
├── docs/
│   ├── assets/
│   │   ├── architecture-overview.svg
│   │   ├── loop-lifecycle.svg
│   │   └── project-banner.svg
│   ├── templates/
│   │   ├── README.md
│   │   ├── accessibility-audit-template.md
│   │   ├── adr-template.md
│   │   ├── api-documentation-template.md
│   │   ├── architecture-template.md
│   │   ├── bug-report-template.md
│   │   ├── change-request-template.md
│   │   ├── code-review-template.md
│   │   ├── database-schema-template.md
│   │   ├── deployment-checklist.md
│   │   ├── feature-specification-template.md
│   │   ├── incident-report-template.md
│   │   ├── maintenance-checklist.md
│   │   ├── meeting-notes-template.md
│   │   ├── migration-template.md
│   │   ├── project-status-template.md
│   │   ├── qa-test-case-template.md
│   │   ├── release-checklist.md
│   │   ├── risk-assessment-template.md
│   │   ├── rollback-checklist.md
│   │   ├── security-audit-template.md
│   │   ├── test-plan-template.md
│   │   ├── test-report-template.md
│   │   └── threat-assessment-template.md
│   ├── README.md
│   ├── exercises-guide.md
│   ├── javascript-concepts.md
│   └── project-structure.md
├── scripts/
│   ├── README.md
│   ├── check-project-structure.py
│   ├── security-check.py
│   ├── validate-docs.py
│   ├── validate-exercises.py
│   └── validate-markdown.py
├── .editorconfig
├── .env.example
├── .gitattributes
├── .gitignore
├── .gitleaks.toml
├── .markdownlint.json
├── AUTHORS.md
├── CHANGELOG.md
├── CITATION.cff
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── ROADMAP.md
├── SECURITY.md
└── SUPPORT.md
```

## 🧭 Directory responsibilities

| Directory or file | Responsibility |
|---|---|
| Assignment directory | Original five standalone HTML exercises |
| asset/ | Seven original instructional PNGs referenced by Q1-Q3 |
| OutPut/ | Three existing output screenshots for Q1-Q3 |
| docs/ | Product, architecture, development, security, accessibility, quality, privacy, operations, and maintainer guidance |
| docs/assets/ | Original SVG banner and architecture/loop illustrations |
| docs/templates/ | Reusable architecture, feature, test, security, accessibility, release, and maintenance templates |
| scripts/ | Python validation utilities |
| .github/ISSUE_TEMPLATE/ | Structured issue forms |
| .github/DISCUSSION_TEMPLATE/ | Discussion templates |
| .github/workflows/ | Repository validation, security heuristic, and stale triage automation |

## ⚙️ Runtime entry points
There is no shared application entry point. Each Q1-Q5 HTML file is opened independently. JavaScript is embedded in the page. There is no frontend/backend split, route configuration, database, API, or application build output.

## 🔍 Configuration
The root EditorConfig, Git attributes, ignore rules, Markdown lint settings, and Gitleaks configuration support repository maintenance. No runtime environment variables are currently needed.

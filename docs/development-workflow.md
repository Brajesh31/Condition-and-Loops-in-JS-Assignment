# 🔄 Development Workflow

```mermaid
flowchart TD
  A([Choose issue or improvement]) --> B[Inspect affected exercise]
  B --> C[Create focused branch]
  C --> D[Make small change]
  D --> E[Run structural validation]
  E --> F{Validator passes?}
  F -->|No| D
  F -->|Yes| G[Manual browser check]
  G --> H[Update docs and screenshots if needed]
  H --> I[Review diff and commit]
  I --> J[Open pull request]
  J --> K[Address review feedback]
  K --> L([Merge after approval])
```

## Principles
- Preserve original assignment content unless a behavior change is intentional.
- Keep the change focused.
- Do not fabricate screenshot evidence or test outcomes.
- Update documentation with code changes.
- State any checks that could not be run.

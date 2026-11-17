# 🧠 Design Patterns and Teaching Patterns

This repository is intentionally too small to justify conventional application architecture patterns such as MVC, repository, dependency injection, or service layers.

## Patterns visible in the examples
- **Guarded branch:** an `if` condition controls whether a statement runs.
- **Ordered decision chain:** `if / else if / else` selects the first matching branch.
- **Value dispatch:** `switch` matches a value to a case.
- **Counter-controlled iteration:** loop state changes until a boundary is reached.
- **Pre-test iteration:** `for` and `while` check the condition before the body.
- **Post-test iteration:** `do...while` checks after executing the body.

## Teaching recommendation
Use trace tables when a learner has difficulty following counter state. Keep each new example small enough that the complete sequence of condition checks and outputs can be followed manually.

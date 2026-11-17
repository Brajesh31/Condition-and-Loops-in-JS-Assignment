# 🧪 Testing Strategy

## Current testing state
The repository contains five static HTML files with inline JavaScript. There is no JavaScript test runner, assertion library, browser automation, coverage collector, or lint configuration.

## Structural validation
Run from the repository root:
```bash
python scripts/validate-exercises.py
```
This checks the expected HTML files, basic document markers, embedded script blocks, and local image references in Q1-Q3. It does not execute JavaScript or render a page.

## Manual behavior matrix
| Page | Expected observation |
|---|---|
| Q1 | Adult, pleasant-weather, and Monday messages |
| Q2 | `grade B` |
| Q3 | Three groups of five numbered messages |
| Q4 | Values 6 through 15 |
| Q5 | Values 1 through 25, then 24 through 1 |

## Future automation
A JavaScript test harness may extract or refactor logic into testable functions. Do not claim coverage until a test runner has executed and produced evidence.

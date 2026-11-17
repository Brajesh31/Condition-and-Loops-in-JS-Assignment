# 🧪 Test Strategy

## Layers
| Layer | Current status | Appropriate check |
|---|---|---|
| File structure | Script planned/available | Python structural validator |
| JavaScript behavior | Manual only | Browser Console comparison |
| Browser rendering | Manual only | Open each page |
| Asset references | Structural check for Q1-Q3 | Verify local files |
| Accessibility | Guidance only | Manual audit |
| Security | Source review guidance | Review diffs and workflows |

## Priorities
Test boundary conditions in grade comparisons and loop termination. For any changed loop, inspect both the first iteration and the final failed condition.

## Exclusions
There are no APIs, database operations, authentication flows, or deployed application routes to integration-test in the current repository.

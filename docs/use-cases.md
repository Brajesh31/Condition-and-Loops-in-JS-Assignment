# 🧩 Use Cases

| ID | Actor | Goal | Relevant page or guide |
|---|---|---|---|
| UC-01 | Learner | See a true/false branch | Q1 |
| UC-02 | Learner | Compare an if-chain and switch | Q1 |
| UC-03 | Learner | Trace grade selection | Q2 |
| UC-04 | Learner | Compare loop structures | Q3 |
| UC-05 | Learner | Understand a transformed counter | Q4 |
| UC-06 | Learner | Trace ascending and descending loops | Q5 |
| UC-07 | Instructor | Demonstrate loop boundaries | Q3-Q5 |
| UC-08 | Contributor | Validate exercise structure | scripts/validate-exercises.py |
| UC-09 | Maintainer | Review security and contribution expectations | SECURITY.md, CONTRIBUTING.md |

## Example: UC-05 numeric range
**Precondition:** The learner can open Q4 in a browser.

**Main flow:** Inspect the initialization, condition, update, and `console.log(i + 1)` expression. Trace counter values 5 to 14.

**Expected observation:** The displayed values are 6 to 15.

**Teaching point:** The displayed value is not identical to the loop counter.

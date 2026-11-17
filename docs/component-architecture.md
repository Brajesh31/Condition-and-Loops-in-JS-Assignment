# 🧩 Component Architecture

This repository does not use a component framework. Its meaningful units are independent pages and their embedded scripts.

| Unit | Responsibility | Coupling |
|---|---|---|
| Q1.html | Conditional examples | Independent |
| Q2.html | Grade branch example | Independent |
| Q3.html | Loop comparison | Independent |
| Q4.html | Numeric range example | Independent |
| Q5.html | Counting examples | Independent |
| asset/ | Lesson illustrations | Referenced by Q1-Q3 |
| OutPut/ | Existing visual evidence | Stored screenshots |

## Relationship diagram
```mermaid
flowchart TB
  Assignment[Assignment directory]
  Assignment --> Q1[Q1.html]
  Assignment --> Q2[Q2.html]
  Assignment --> Q3[Q3.html]
  Assignment --> Q4[Q4.html]
  Assignment --> Q5[Q5.html]
  Q1 --> Assets[asset/]
  Q2 --> Assets
  Q3 --> Assets
  Assignment --> Evidence[OutPut/]
```

No React components, reusable UI library, or module import graph is present.

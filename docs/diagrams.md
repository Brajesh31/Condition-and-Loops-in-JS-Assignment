# 🧭 Project and Control-Flow Diagrams

The diagrams below model only the checked-in static assignment. Authentication, API, database, and server diagrams are not applicable to the current architecture.

## 🏗️ High-level architecture
```mermaid
flowchart TB
  L[Learner] --> B[Modern web browser]
  B --> Q1[Q1.html]
  B --> Q2[Q2.html]
  B --> Q3[Q3.html]
  B --> Q4[Q4.html]
  B --> Q5[Q5.html]
  Q1 --> C[Developer Tools Console]
  Q2 --> C
  Q3 --> C
  Q4 --> C
  Q5 --> C
```

## 🔁 Overall learner workflow
```mermaid
flowchart TD
  A([Start]) --> B[Choose exercise]
  B --> C[Open HTML file]
  C --> D[Browser parses HTML]
  D --> E[Inline JavaScript executes]
  E --> F[console.log output]
  F --> G[Inspect Console]
  G --> H[Trace condition or counter]
  H --> I([Learning complete])
```

## 🧭 Conditional flow
```mermaid
flowchart TD
  A([Start]) --> B[Evaluate condition]
  B --> C{True?}
  C -->|Yes| D[Run matching branch]
  C -->|No| E[Evaluate next branch or fallback]
  D --> F([Continue])
  E --> F
```

## 🏅 Grade decision flow
```mermaid
flowchart TD
  A([Start, marks = 80]) --> B{marks >= 90?}
  B -->|Yes| C[Grade A]
  B -->|No| D{marks >= 70?}
  D -->|Yes| E[Grade B]
  D -->|No| F{marks >= 50?}
  F -->|Yes| G[Grade C]
  F -->|No| H[Grade F]
```

## 🔂 Pre-test loop sequence
```mermaid
sequenceDiagram
  participant S as Script
  participant K as Counter
  participant C as Condition
  participant O as Console
  S->>K: Initialize
  loop While condition is true
    S->>C: Evaluate counter condition
    C-->>S: true
    S->>O: Log output expression
    S->>K: Update counter
  end
  S->>C: Evaluate again
  C-->>S: false
  S-->>S: Exit loop
```

## 🔄 do...while state
```mermaid
stateDiagram-v2
  [*] --> ExecuteBody
  ExecuteBody --> CheckCondition
  CheckCondition --> ExecuteBody: true
  CheckCondition --> [*]: false
```

## ↕️ Q5 output transformation
```mermaid
flowchart LR
  A[Ascending counter 0..24] --> B[Log counter + 1]
  B --> C[Displayed 1..25]
  D[Descending counter 25..2] --> E[Log counter - 1]
  E --> F[Displayed 24..1]
```

## 🧪 Validation workflow
```mermaid
flowchart TD
  A([Change proposed]) --> B[Run Python validator]
  B --> C{Structure valid?}
  C -->|No| D[Fix missing files or references]
  D --> B
  C -->|Yes| E[Open changed page in browser]
  E --> F[Inspect Console and images]
  F --> G[Update documentation]
  G --> H([Ready for review])
```

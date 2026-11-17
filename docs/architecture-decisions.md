# 🏛️ Architecture Decisions

## ADR-001: Independent HTML exercises
**Status:** Accepted

**Context:** The assignment teaches discrete JavaScript fundamentals and has five small exercises.

**Decision:** Keep each question as an independent HTML page with its inline script.

**Consequences:** Pages can be opened directly without a build system. Some repeated HTML structure may remain, but the learning examples stay isolated.

## ADR-002: Browser Console output
**Status:** Accepted

**Context:** The core learning objective is JavaScript control flow.

**Decision:** Use `console.log` for the existing exercise output.

**Consequences:** No output UI or dependency is needed. Learners must know how to open Developer Tools.

## ADR-003: Documentation without invented subsystems
**Status:** Accepted

**Context:** A generic repository checklist contains API, database, authentication, deployment, and infrastructure topics that do not apply to every repository.

**Decision:** Document the actual static architecture and explicitly state when a subsystem is absent.

**Consequences:** Avoids false claims and unnecessary empty folders.

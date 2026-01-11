# ADR Constitution

This document defines the rules and conventions for Architecture Decision Records (ADRs).

## Mandatory ADRs
Before implementation begins, the following core architectural decisions MUST be made and recorded (Minimum 3-5 records ideal):

1.  **Language / Runtime Selection**: (e.g., Python, Node.js, Go)
2.  **Communication Pattern**: Synchronous (REST/gRPC) vs Asynchronous (Messaging).
3.  **State Management**: Stateful vs Stateless architecture.
4.  **Data Persistence**: Datastore selection (Relational, NoSQL, etc.).
5.  **Authentication**: Concrete authentication method (OIDC, JWT, Session).

## Directory Structure & Naming
ADRs are stored in `doc/adr/decisions/` and follow a strict naming convention to ensure ordering.

```
doc/adr/
|-- constitution.md        # This file (Rules)
|-- index.md               # Table of Contents
|-- decisions/             # Stored decisions
    |-- language-selection.md
    |-- database-selection.md
    `-- ...
```

**Naming Convention**:
- Filename: `short-title.md`
- Title: `[ADR-{Category}-{Number}] Title Case Name`
- **Format**: ``ADR-{Category}-{Number}``
    - ``Category``: 3-4 letter code (e.g., ``ARCH``, ``AUTH``, ``DATA``, ``INF``, ``TECH``).
    - ``Number``: Monotonic integer within category (e.g., 001).
- **Example**: ``[ADR-AUTH-001] Select Auth Provider``

## Required Structure
ADRs SHOULD follow the **Madr** template structure. Key sections include:

1.  **Context and Problem Statement**: What is the issue? Why is it a problem?
2.  **Decision Drivers**: Forces, constraints, and requirements driving the decision.
3.  **Considered Options**: List of alternatives evaluated (including "do nothing").
4.  **Decision Outcome**: The selected option and the justification (Rational).
5.  **Consequences**:
    *   **Positive**: Benefits, improvements.
    *   **Negative**: Trade-offs, new debts, complexity.

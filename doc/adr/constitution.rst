ADR Constitution
================

This document defines the rules and conventions for Architecture Decision Records (ADRs).

Mandatory ADRs
--------------
Before implementation begins, the following core architectural decisions MUST be made and recorded (Minimum 3-5 records ideal):

1.  **Language / Runtime Selection**: (e.g., Python, Node.js, Go)
2.  **Communication Pattern**: Synchronous (REST/gRPC) vs Asynchronous (Messaging).
3.  **State Management**: Stateful vs Stateless architecture.
4.  **Data Persistence**: Datastore selection (Relational, NoSQL, etc.).
5.  **Authentication**: Concrete authentication method (OIDC, JWT, Session).

Directory Structure & Naming
----------------------------
ADRs are stored in `doc/adr/` and follow a strict naming convention to ensure ordering.

**Structure**:

::

    doc/adr/
    |-- constitution.rst       # This file (Rules)
    |-- index.rst              # Table of Contents
    |-- template.rst           # Copy this to create new ADRs
    |-- 0001-language.rst      # Sequential ID and kebab-case title
    |-- 0002-database.rst
    `-- ...

**Naming Convention**:
- Filename: ``NNNN-short-title.rst``
- ``NNNN``: Monotonic integer, distinct (e.g., 0001, 0002).
- ``short-title``: Kebab-case description (e.g., ``event-bus-selection``).

Lifecycle
---------
- **Proposed**: Draft state, under review.
- **Accepted**: Approved and binding.
- **Deprecated**: No longer valid due to newer decisions.
- **Superseded**: Replaced by a specific newer ADR (reference the new ID).

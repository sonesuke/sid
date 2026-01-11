Architecture Constitution
=========================

This document defines the rules and conventions specifically for the architecture documentation.

**Relationship to Main Constitution**
This constitution inherits all principles from the :doc:`Main Specification Constitution <../../constitution>`. In case of conflict, the Main Constitution takes precedence for spec-related matters, while this document governs architectural decisions.

**Architectural Decision Records (ADRs)**
- All significant architectural decisions MUST be recorded as ADRs in `doc/adr`.
- ADRs SHOULD follow the [Madr](https://adr.github.io/madr/) template.

**Diagramming Standards**
- **Format**: Diagrams SHOULD be defined using Mermaid.js code blocks where possible for version control.
- **Model**: The C4 model (Context, Containers, Components, Code) SHALL be used for structural views.

**References**
- Architecture views MUST reference Functional Requirements (FR) and Non-Functional Requirements (NFR) using their identifiers.
- Architecture views SHOULD NOT restate requirement text.

Architectural Views and Their Roles
-----------------------------------

This project adopts a layered architecture documentation model.
Each view has a clearly defined purpose and scope.
Views SHALL NOT overlap in responsibility.

Specification (Requirements Layer)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Functional Requirements (FR), Non-Functional Requirements (NFR),
  Constraints (CON), and Error Definitions (ERR) define **what the system must do**
  and **under what conditions**.
- Specification documents are the **single source of truth** for requirements.
- Architecture documents SHALL NOT redefine or restate requirements.

Context View (C4 Level 1)
~~~~~~~~~~~~~~~~~~~~~~~~~

**Purpose**:
- Define the system boundary and its external environment.

**Scope**:
- External actors and external systems
- High-level interactions across the system boundary

**Rules**:
- The Context View SHALL NOT describe internal structure.
- Use cases and actors SHALL be referenced, not restated.

Building Block View (C4 Level 2 / 3)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Purpose**:
- Allocate responsibilities to architectural building blocks.

**Scope**:
- Major deployable units (containers) and their responsibilities
- Relationships between building blocks
- Mapping of responsibilities to Functional Requirements (by reference)

**Rules**:
- Building Blocks represent **responsibility-bearing units**, not technologies.
- Specific Cloud Managed Services (e.g., AWS Cognito) SHALL NOT be named; use generic terms (e.g., IdP) instead.
- Implementation technologies SHALL NOT be specified.
- Each Functional Requirement SHALL have a clear architectural owner.

Runtime View
~~~~~~~~~~~~

**Purpose**:
- Explain how building blocks collaborate at runtime to fulfill key scenarios.

**Scope**:
- Representative interaction flows
- Responsibility transitions between building blocks
- Normal and exceptional execution paths (by reference to ERR)

**Rules**:
- Runtime Views SHALL NOT redefine Functional Requirements.
- Error semantics are defined in ERR and SHALL be referenced only.

Architecture Decision Records (ADR)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Purpose**:
- Record significant architectural decisions and their rationale.

**Scope**:
- Decisions involving trade-offs, alternatives, or long-term impact
- Technology choices, architectural patterns, and deployment strategies

**Rules**:
- ADRs are created when multiple viable options exist.
- Architecture Views SHALL reference ADRs where decisions affect the structure.
- ADRs SHALL NOT redefine requirements.

Deployment View
~~~~~~~~~~~~~~~

**Purpose**:
- Describe how building blocks are deployed onto physical or cloud infrastructure.

**Scope**:
- Environments, regions, and network boundaries
- Infrastructure components (e.g., cloud services)
- Mapping of building blocks to deployment units

**Rules**:
- Deployment Views MAY reference specific platforms or services (e.g., AWS).
- This is the primary view for mapping abstract building blocks to concrete Cloud Managed Services.
- Deployment Views SHALL demonstrate how NFRs and CONs are satisfied.
- No new Functional Requirements SHALL be introduced.

Cross-cutting Concepts
~~~~~~~~~~~~~~~~~~~~~~

**Purpose**:
- Describe architectural mechanisms that apply across multiple building blocks.

**Scope**:
- Security, authentication, authorization
- Logging, monitoring, and observability
- Configuration, multi-tenancy, and data isolation

**Rules**:
- Cross-cutting Concepts explain **how** requirements are realized structurally.
- Detailed requirement definitions remain in the Specification layer.
- Concepts SHALL be consistent across all relevant views.

Dependency Direction
~~~~~~~~~~~~~~~~~~~~

The dependency direction between documents SHALL be strictly maintained:

- Specification → Architecture Views
- Architecture Views → ADRs
- Architecture Views → Deployment Views

Reverse dependencies SHALL NOT exist.

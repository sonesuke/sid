# Architecture Constitution

This document defines the rules and conventions specifically for the architecture documentation.

## Relationship to Main Constitution

This constitution inherits all principles from the [Main Specification Constitution](../spec/constitution.md). In case of conflict, the Main Constitution takes precedence for spec-related matters, while this document governs architectural decisions.

## Architectural Decision Records (ADRs)

- All significant architectural decisions MUST be recorded as ADRs in `doc/adr`.
- ADRs SHOULD follow the `Madr <https://adr.github.io/madr/>`_ template.

## Diagramming Standards

- **Format**: Diagrams SHOULD be defined using Mermaid.js code blocks where possible for version control.
- **Model**: The C4 model (Context, Containers, Components, Code) SHALL be used for structural views.

## References

- Architecture views MUST reference Functional Requirements (FR) and Non-Functional Requirements (NFR) using their identifiers.
- Architecture views SHOULD NOT restate requirement text.

## ID Naming Convention

- Architectural Elements and Rules SHALL be assigned unique Reference IDs to facilitate traceability.
  - **CTX-{Element}**: Context View Elements
  - **BB-{Component}**: Building Block Elements
  - **RT-{Number}**: Runtime View Scenarios (e.g., `RT-001`)
  - **DEP-{Topic}**: Deployment Elements
  - **CC-{Topic}-{Number}**: Cross-cutting Rules (e.g., `CC-AUTH-001`)

## Architectural Views and Their Roles

This project adopts a layered architecture documentation model.
Each view has a clearly defined purpose and scope.
Views SHALL NOT overlap in responsibility.

### Specification (Requirements Layer)

- Functional Requirements (FR), Non-Functional Requirements (NFR),
  Constraints (CON), and Error Definitions (ERR) define **what the system must do**
  and **under what conditions**.
- Specification documents are the **single source of truth** for requirements.
- Architecture documents SHALL NOT redefine or restate requirements.

### Context View (C4 Level 1)

**Purpose**:
- Define the system boundary and its external environment.

**Scope**:
- External actors and external systems
- High-level interactions across the system boundary

**Rules**:
- The Context View SHALL NOT describe internal structure.
- Use cases and actors SHALL be referenced, not restated.

### Building Block View (C4 Level 2 / 3)

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

### Runtime View

**Purpose**:
- Explain how building blocks collaborate at runtime to fulfill key scenarios.
- Demonstrate Cross-cutting Concepts "in action".

**Scope**:
- Representative interaction flows (5-10 key scenarios)
- Responsibility transitions between building blocks
- Normal and exceptional execution paths (by reference to ERR)

**ID Convention**:
- **RT-{Number}**: Runtime Scenario identifier (e.g., `RT-001`, `RT-002`)

**Required Structure** (per Scenario):
1. **Scenario**: Brief description of the runtime behavior.
2. **Actors**: List of Building Blocks and external systems involved.
3. **Flow**: Step-by-step sequence, preferably as a **Mermaid Sequence Diagram**.
4. **Cross-cutting**: Which CC rules are "active" during this flow.
5. **Requirements**: Related FR/NFR references.

**Typical Scenarios**:
- User Login (Authentication flow)
- Authenticated API Request
- Async Event Processing (Pub/Sub)
- Blue-Green Switchover (Traffic Switching Behavior)
- Error Handling / Retry Flow

**Rules**:
- Runtime Views SHALL NOT redefine Functional Requirements.
- Error semantics are defined in ERR and SHALL be referenced only.
- Focus on **time-axis stories**: "Who calls whom, in what order, under what rules."

### Architecture Decision Records (ADR)

**Purpose**:
- Record significant architectural decisions and their rationale.

**Scope**:
- Decisions involving trade-offs, alternatives, or long-term impact
- Technology choices, architectural patterns, and deployment strategies

**Rules**:
- ADRs are created when multiple viable options exist.
- Architecture Views SHALL reference ADRs where decisions affect the structure.
- ADRs SHALL NOT redefine requirements.

### Deployment View

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

### Cross-cutting Concepts

**Purpose**:
- Define the **"Design Constitution"**: the permanent rules, principles, and mechanisms that apply consistently across all architectural elements.
- It is the "Physical Laws" of the system that every component must obey.

**Scope (Typical Topics)**:
1. **Authentication & Authorization**: (e.g., "Delegate to External IdP", "Role + Scope model").
2. **Error Handling**: (e.g., "Map internal exceptions to standard error codes").
3. **Logging & Auditing**: (e.g., "Mandatory Correlation ID", "No PII in logs").
4. **Security**: (e.g., "Zero Trust", "TLS everywhere").
5. **Data & Transactions**: (e.g., "Idempotency", "Eventual Consistency", "No Distributed Tx").
6. **API Design**: (e.g., "REST + JSON", "Versioning rules").
7. **Observability**: (e.g., "SLI/SLO driven").

**Rules**:
- **DO NOT** write component-specific specific logic (Use Building Block View).
- **DO NOT** write ADR rationale or history (Use ADRs).
- **DO NOT** write generic best practices; only document rules adopted by this system.
- Cross-cutting Concepts should be viewed as **"Permanent Rules extracted from ADRs"**.
- Consistent with NFRs (Requirements) and ADRs (Decisions).

**Operational Rules**:
1. **Promotion**: If an ADR is referenced 2-3 times with the same reasoning across different contexts, it is a candidate for promotion to a Cross-cutting Concept (CC).
2. **Stability**: Once promoted to a CC, the rule represents a stable "Institution". The original ADR may be detached or superseded to prevent regression.
3. **Exceptions**: Any ADR that violates a Cross-cutting Concept MUST be explicitly labeled as an **"Exception ADR"** with strong justification.

### Dependency Direction

The dependency direction between documents SHALL be strictly maintained:

- Specification → Architecture Views
- Architecture Views → ADRs
- Architecture Views → Deployment Views

Reverse dependencies SHALL NOT exist.

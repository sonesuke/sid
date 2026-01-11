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

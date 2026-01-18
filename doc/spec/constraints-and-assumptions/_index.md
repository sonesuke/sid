# Constraints and Assumptions

This section documents the mandatory conditions imposed on the system.

## Guidelines

**Derivation Rule**: Constraints (CON) MUST be derived into Functional Requirements (FR) or Non-Functional Requirements (NFR). If a constraint effectively limits the system, it must be reflected in the requirements.

## Defining a New Constraint

When adding a new constraint, add it to the appropriate category file or create a new one following this structure:

```markdown
&lt;a id="CON-{{CATEGORY}}-{{ID}}"&gt;&lt;/a&gt;

## CON-{{CATEGORY}}-{{ID}} {{NAME}}

{{SHORT_DESCRIPTION (2-3 lines)}}

**Rationale**:

* {{RATIONALE_ITEM}} (e.g., "GDPR Article 17", "NIST CSF 2.0 - PR.DS-1", "Business Strategy 2025 - Global Expansion")

**Related FRs** (Optional):

* [{{FR_ID}} ({{FR_NAME}})]({{FR_PATH}})

**Related NFRs** (Optional):

* [{{NFR_ID}} ({{NFR_NAME}})]({{NFR_PATH}})

**Details** (Optional):

{{DETAILED_DESCRIPTION}}
```

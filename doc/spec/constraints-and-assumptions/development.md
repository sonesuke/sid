# Development Constraints

<a id="CON-DEV-001"></a>

## CON-DEV-001 Secure Software Development Lifecycle

All software development SHALL follow Secure SDLC practices:

* Security by Design principles.
* Static and dynamic code analysis.
* Code review for security vulnerabilities.
* Dependency vulnerability scanning.

**Rationale**:

* NIST CSF 2.0 - Software integrity.

**Related NFRs**:

* [NFR-SEC-007 (Secure Development)](../non-functional-requirements/security.md#NFR-SEC-007)

<a id="CON-DEV-002"></a>

## CON-DEV-002 Supply Chain Risk Management

The project SHALL implement Cyber Supply Chain Risk Management (C-SCRM):

* Inventory of third-party dependencies.
* Regular vulnerability assessment of dependencies.
* Risk evaluation of third-party service providers.

**Rationale**:

* NIST CSF 2.0 - Supply chain security.

**Related NFRs**:

* [NFR-SEC-008 (Supply Chain Security)](../non-functional-requirements/security.md#NFR-SEC-008)

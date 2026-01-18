# Security Constraints

<a id="CON-SEC-PASSWORD-POLICY"></a>

## CON-SEC-PASSWORD-POLICY Configurable Password Policy

The [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP) SHALL allow each [DAT-TENANT (Tenants)](../data-model/schema.md#DAT-TENANT) to configure password complexity requirements (e.g., minimum length, character types).

**Rationale**:

* Compliance with Japan's Act on the Protection of Personal Information (APPI).

<a id="CON-SEC-AUDIT-LOG"></a>

## CON-SEC-AUDIT-LOG Audit Log Provision

The [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP) SHALL provide audit logs recording access to and modifications of personal data.

**Rationale**:

* Compliance with Japan's Act on the Protection of Personal Information (APPI).

<a id="CON-SEC-ENCRYPTION-TRANSIT"></a>

## CON-SEC-ENCRYPTION-TRANSIT Encryption in Transit

All communications between components and external systems SHALL be encrypted using TLS 1.2 or higher.

**Rationale**:

* NIST CSF 2.0 / ISO 27001 - Encryption in transit.

**Related NFRs**:

* [NFR-SEC-001 (Encryption in Transit)](../non-functional-requirements/security.md#NFR-SEC-001)

<a id="CON-SEC-ENCRYPTION-REST"></a>

## CON-SEC-ENCRYPTION-REST Encryption at Rest

All persistent data SHALL be encrypted at rest using AES-256 or equivalent.

**Rationale**:

* NIST CSF 2.0 / ISO 27001 - Encryption at rest.

**Related NFRs**:

* [NFR-SEC-002 (Encryption at Rest)](../non-functional-requirements/security.md#NFR-SEC-002)

<a id="CON-SEC-MFA"></a>

## CON-SEC-MFA Multi-Factor Authentication

The system SHALL support Multi-Factor Authentication (MFA) for user login.

**Rationale**:

* NIST CSF 2.0 - Strong authentication.

**Related NFRs**:

* [NFR-SEC-003 (Multi-Factor Authentication)](../non-functional-requirements/security.md#NFR-SEC-003)

<a id="CON-SEC-KEY-MANAGEMENT"></a>

## CON-SEC-KEY-MANAGEMENT Key Management

The system SHALL implement secure key management practices.

**Rationale**:

* NIST CSF 2.0 - Data protection.

**Related NFRs**:

* [NFR-SEC-004 (Key Management)](../non-functional-requirements/security.md#NFR-SEC-004)

<a id="CON-SEC-LEAST-PRIVILEGE"></a>

## CON-SEC-LEAST-PRIVILEGE Least Privilege

The system SHALL enforce the principle of least privilege.

**Rationale**:

* NIST CSF 2.0 - Access control.

**Related NFRs**:

* [NFR-SEC-005 (Least Privilege)](../non-functional-requirements/security.md#NFR-SEC-005)

<a id="CON-SEC-ADAPTIVE-AUTH"></a>

## CON-SEC-ADAPTIVE-AUTH Adaptive Authentication

The system SHOULD implement adaptive (risk-based) authentication.

**Rationale**:

* NIST CSF 2.0 - Context-aware security.

**Related NFRs**:

* [NFR-SEC-006 (Adaptive Authentication)](../non-functional-requirements/security.md#NFR-SEC-006)

<a id="CON-SEC-ERROR-DISCLOSURE"></a>

## CON-SEC-ERROR-DISCLOSURE Error Disclosure

Error responses SHALL NOT reveal sensitive internal details including:

* Stack traces or internal exception messages
* Database query details
* Internal service names or versions
* User existence confirmation (for security-sensitive operations)

**Rationale**:

* NIST CSF 2.0 / OWASP - Information disclosure prevention.

**Related FRs**:

* [FR-SYS-001 (Application Registration)](../functional-requirements/system-ops.md#FR-SYS-001)

# Constraints and Assumptions

This section documents the mandatory conditions imposed on the system.

## Security Constraints

<a id="CON-SEC-001"></a>

### CON-SEC-001 Configurable Password Policy

The [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP) SHALL allow each [DAT-TENANT (Tenants)](../data-model/schema.md#DAT-TENANT) to configure password complexity requirements (e.g., minimum length, character types).

**Rationale**: Compliance with Japan's Act on the Protection of Personal Information (APPI).

<a id="CON-SEC-002"></a>

#### CON-SEC-002 Audit Log Provision

The [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP) SHALL provide audit logs recording access to and modifications of personal data.

**Rationale**: Compliance with Japan's Act on the Protection of Personal Information (APPI).

<a id="CON-SEC-003"></a>

#### CON-SEC-003 Encryption in Transit

All communications between components and external systems SHALL be encrypted using TLS 1.2 or higher.

**Rationale**: NIST CSF 2.0 / ISO 27001 - Encryption in transit.

**Related NFRs**:

* [NFR-SEC-001 (Encryption in Transit)](../non-functional-requirements/security.md#NFR-SEC-001)

<a id="CON-SEC-004"></a>

#### CON-SEC-004 Encryption at Rest

All persistent data SHALL be encrypted at rest using AES-256 or equivalent.

**Rationale**: NIST CSF 2.0 / ISO 27001 - Encryption at rest.

**Related NFRs**:

* [NFR-SEC-002 (Encryption at Rest)](../non-functional-requirements/security.md#NFR-SEC-002)

<a id="CON-SEC-005"></a>

#### CON-SEC-005 Multi-Factor Authentication

The system SHALL support Multi-Factor Authentication (MFA) for user login.

**Rationale**: NIST CSF 2.0 - Strong authentication.

**Related NFRs**:

* [NFR-SEC-003 (Multi-Factor Authentication)](../non-functional-requirements/security.md#NFR-SEC-003)

<a id="CON-SEC-006"></a>

#### CON-SEC-006 Key Management

The system SHALL implement secure key management practices.

**Rationale**: NIST CSF 2.0 - Data protection.

**Related NFRs**:

* [NFR-SEC-004 (Key Management)](../non-functional-requirements/security.md#NFR-SEC-004)

<a id="CON-SEC-007"></a>

#### CON-SEC-007 Least Privilege

The system SHALL enforce the principle of least privilege.

**Rationale**: NIST CSF 2.0 - Access control.

**Related NFRs**:

* [NFR-SEC-005 (Least Privilege)](../non-functional-requirements/security.md#NFR-SEC-005)

<a id="CON-SEC-008"></a>

#### CON-SEC-008 Adaptive Authentication

The system SHOULD implement adaptive (risk-based) authentication.

**Rationale**: NIST CSF 2.0 - Context-aware security.

**Related NFRs**:

* [NFR-SEC-006 (Adaptive Authentication)](../non-functional-requirements/security.md#NFR-SEC-006)

<a id="CON-SEC-009"></a>

#### CON-SEC-009 Error Disclosure

Error responses SHALL NOT reveal sensitive internal details including:

* Stack traces or internal exception messages
* Database query details
* Internal service names or versions
* User existence confirmation (for security-sensitive operations)

**Rationale**: NIST CSF 2.0 / OWASP - Information disclosure prevention.

**Related FRs**:

* [FR-SYS-001 (Application Registration)](../functional-requirements/system-ops.md#FR-SYS-001)

## Data Constraints

<a id="CON-DATA-001"></a>

### CON-DATA-001 Data Residency

All customer data SHALL be stored exclusively in data centers located in Japan or the European Union.

**Rationale**: GDPR / APPI - Cross-border data transfer restrictions.

**Related NFRs**:

* [NFR-DATA-001 (Data Residency)](../non-functional-requirements/data.md#NFR-DATA-001)

<a id="CON-DATA-002"></a>

#### CON-DATA-002 Audit Log Retention

[DAT-LOG (Audit Logs)](../data-model/schema.md#DAT-LOG) SHALL be retained for a minimum of 7 years to comply with Japanese accounting laws and APPI requirements.

**Rationale**: Legal compliance (Japan Accounting Law, APPI).

<a id="CON-DATA-003"></a>

#### CON-DATA-003 Billing Data Retention

[DAT-BILL-EVENT (Billing Events)](../data-model/schema.md#DAT-BILL-EVENT) SHALL be retained for a minimum of 5 years to comply with tax regulations.

**Rationale**: Legal compliance (Tax regulations).

## Capacity Constraints

<a id="CON-CAP-001"></a>

### CON-CAP-001 Tenant Capacity

The system SHALL support a minimum of 1,000 active [DAT-TENANT (Tenants)](../data-model/schema.md#DAT-TENANT).

**Rationale**: Business scalability requirement.

**Related NFRs**:

* [NFR-CAP-001 (Tenant Scalability)](../non-functional-requirements/capacity.md#NFR-CAP-001)

<a id="CON-CAP-002"></a>

#### CON-CAP-002 User Capacity per Tenant

The system SHALL support a minimum of 10,000 [DAT-USER (Users)](../data-model/schema.md#DAT-USER) per [DAT-TENANT (Tenants)](../data-model/schema.md#DAT-TENANT).

**Rationale**: Business scalability requirement.

**Related NFRs**:

* [NFR-CAP-002 (User Scalability)](../non-functional-requirements/capacity.md#NFR-CAP-002)

## Operational Constraints

<a id="CON-OPS-001"></a>

### CON-OPS-001 Availability SLO

The system SHALL target a Service Level Objective (SLO) of 99.9% availability, excluding scheduled maintenance windows.

**Rationale**: Business continuity requirement.

**Related NFRs**:

* [NFR-OPS-001 (Service Level Objective)](../non-functional-requirements/availability.md#NFR-OPS-001)

<a id="CON-OPS-002"></a>

#### CON-OPS-002 Maintenance Window

Scheduled maintenance windows SHALL be defined and communicated in advance. (Details TBD)

**Rationale**: Operational planning.

**Related NFRs**:

* [NFR-OPS-002 (Maintenance Scheduling)](../non-functional-requirements/availability.md#NFR-OPS-002)

<a id="CON-OPS-003"></a>

#### CON-OPS-003 Load Balancing and Failover

The system SHALL implement load balancing and automatic failover.

**Rationale**: NIST CSF 2.0 - Availability.

**Related NFRs**:

* [NFR-OPS-003 (Load Balancing and Failover)](../non-functional-requirements/availability.md#NFR-OPS-003)

<a id="CON-OPS-004"></a>

#### CON-OPS-004 Backup and Redundancy

The system SHALL implement backup and recovery capabilities following the 3-2-1 rule.

**Rationale**: NIST CSF 2.0 - Recovery.

**Related NFRs**:

* [NFR-OPS-004 (Backup and Redundancy)](../non-functional-requirements/availability.md#NFR-OPS-004)

## Monitoring Constraints

<a id="CON-MON-001"></a>

### CON-MON-001 Continuous Monitoring

The system SHALL implement continuous monitoring and anomaly detection.

**Rationale**: NIST CSF 2.0 - Detection.

**Related NFRs**:

* [NFR-MON-001 (Continuous Monitoring)](../non-functional-requirements/monitoring.md#NFR-MON-001)

## Development Constraints

<a id="CON-DEV-001"></a>

### CON-DEV-001 Secure Software Development Lifecycle

All software development SHALL follow Secure SDLC practices:

* Security by Design principles.
* Static and dynamic code analysis.
* Code review for security vulnerabilities.
* Dependency vulnerability scanning.

**Rationale**: NIST CSF 2.0 - Software integrity.

**Affected Actors**:

* [ACT-DEV (Developer)](../actors/list.md#ACT-DEV)

<a id="CON-DEV-002"></a>

#### CON-DEV-002 Supply Chain Risk Management

The project SHALL implement Cyber Supply Chain Risk Management (C-SCRM):

* Inventory of third-party dependencies.
* Regular vulnerability assessment of dependencies.
* Risk evaluation of third-party service providers.

**Rationale**: NIST CSF 2.0 - Supply chain security.

**Affected Actors**:

* [ACT-DEV (Developer)](../actors/list.md#ACT-DEV)

## Compliance Constraints

<a id="CON-COMP-001"></a>

### CON-COMP-001 Data Subject Rights

The system SHALL support data subject rights as required by GDPR and Japan APPI:

* Right to access personal data.
* Right to rectification.
* Right to erasure (right to be forgotten).
* Data portability.

**Rationale**: Legal compliance with privacy regulations.

**Related NFRs**:

* [NFR-DATA-001 (Data Residency)](../non-functional-requirements/data.md#NFR-DATA-001)

## Performance Constraints

<a id="CON-PERF-001"></a>

### CON-PERF-001 Response Time and Throughput

The system SHALL meet performance targets for latency and throughput to ensure a responsive user experience.

**Rationale**: User-Centricity principle - responsive systems improve user satisfaction.

**Related NFRs**:

* [NFR-PERF-001 (Authentication Latency)](../non-functional-requirements/performance.md#NFR-PERF-001)
* [NFR-PERF-002 (API Latency)](../non-functional-requirements/performance.md#NFR-PERF-002)
* [NFR-PERF-003 (UI Responsiveness)](../non-functional-requirements/performance.md#NFR-PERF-003)
* [NFR-PERF-004 (Authentication Throughput)](../non-functional-requirements/performance.md#NFR-PERF-004)

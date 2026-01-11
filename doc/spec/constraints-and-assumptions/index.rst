Constraints and Assumptions
===========================

This section documents the mandatory conditions imposed on the system.

Security Constraints
--------------------

.. _CON-SEC-001:

CON-SEC-001 Configurable Password Policy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The :ref:`TERM-SYS-CP` SHALL allow each :ref:`Tenant <DAT-TENANT>` to configure password complexity requirements (e.g., minimum length, character types).

**Rationale**: Compliance with Japan's Act on the Protection of Personal Information (APPI).

**Impacts**: :ref:`FR-AUTH-006`

.. _CON-SEC-002:

CON-SEC-002 Audit Log Provision
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The :ref:`TERM-SYS-CP` SHALL provide audit logs recording access to and modifications of personal data.

**Rationale**: Compliance with Japan's Act on the Protection of Personal Information (APPI).

**Impacts**: :ref:`FR-LOG-001`, :ref:`FR-LOG-002`

.. _CON-SEC-003:

CON-SEC-003 Encryption in Transit
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
All communications between components and external systems SHALL be encrypted using TLS 1.2 or higher.

**Rationale**: NIST CSF 2.0 / ISO 27001 - Encryption in transit.

**Impacts**: :ref:`NFR-SEC-001`

.. _CON-SEC-004:

CON-SEC-004 Encryption at Rest
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
All persistent data SHALL be encrypted at rest using AES-256 or equivalent.

**Rationale**: NIST CSF 2.0 / ISO 27001 - Encryption at rest.

**Impacts**: :ref:`NFR-SEC-002`

.. _CON-SEC-005:

CON-SEC-005 Multi-Factor Authentication
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The system SHALL support Multi-Factor Authentication (MFA) for user login.

**Rationale**: NIST CSF 2.0 - Strong authentication.

**Impacts**: :ref:`NFR-SEC-003`

.. _CON-SEC-006:

CON-SEC-006 Key Management
^^^^^^^^^^^^^^^^^^^^^^^^^^
The system SHALL implement secure key management practices.

**Rationale**: NIST CSF 2.0 - Data protection.

**Impacts**: :ref:`NFR-SEC-004`

.. _CON-SEC-007:

CON-SEC-007 Least Privilege
^^^^^^^^^^^^^^^^^^^^^^^^^^^
The system SHALL enforce the principle of least privilege.

**Rationale**: NIST CSF 2.0 - Access control.

**Impacts**: :ref:`NFR-SEC-005`

.. _CON-SEC-008:

CON-SEC-008 Adaptive Authentication
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The system SHOULD implement adaptive (risk-based) authentication.

**Rationale**: NIST CSF 2.0 - Context-aware security.

**Impacts**: :ref:`NFR-SEC-006`

.. _CON-SEC-009:

CON-SEC-009 Error Disclosure
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Error responses SHALL NOT reveal sensitive internal details including:

*   Stack traces or internal exception messages
*   Database query details
*   Internal service names or versions
*   User existence confirmation (for security-sensitive operations)

**Rationale**: NIST CSF 2.0 / OWASP - Information disclosure prevention.

**Impacts**: :ref:`ERR-AUTH-401`, :ref:`ERR-AUTH-403`, :ref:`ERR-RES-404`, :ref:`ERR-SYS-500`

Data Constraints
----------------

.. _CON-DATA-001:

CON-DATA-001 Data Residency
^^^^^^^^^^^^^^^^^^^^^^^^^^^
All customer data SHALL be stored exclusively in data centers located in Japan or the European Union.

**Rationale**: GDPR / APPI - Cross-border data transfer restrictions.

**Impacts**: :ref:`NFR-DATA-001`

.. _CON-DATA-002:

CON-DATA-002 Audit Log Retention
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
:ref:`Audit Logs <DAT-LOG>` SHALL be retained for a minimum of 7 years to comply with Japanese accounting laws and APPI requirements.

**Rationale**: Legal compliance (Japan Accounting Law, APPI).

**Impacts**: :ref:`FR-OPS-003`

.. _CON-DATA-003:

CON-DATA-003 Billing Data Retention
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
:ref:`Billing Events <DAT-BILL-EVENT>` SHALL be retained for a minimum of 5 years to comply with tax regulations.

**Rationale**: Legal compliance (Tax regulations).

**Impacts**: :ref:`FR-OPS-003`

Capacity Constraints
--------------------

.. _CON-CAP-001:

CON-CAP-001 Tenant Capacity
^^^^^^^^^^^^^^^^^^^^^^^^^^^
The system SHALL support a minimum of 1,000 active :ref:`Tenants <DAT-TENANT>`.

**Rationale**: Business scalability requirement.

**Impacts**: :ref:`NFR-CAP-001`

.. _CON-CAP-002:

CON-CAP-002 User Capacity per Tenant
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The system SHALL support a minimum of 10,000 :ref:`Users <DAT-USER>` per :ref:`Tenant <DAT-TENANT>`.

**Rationale**: Business scalability requirement.

**Impacts**: :ref:`NFR-CAP-002`

Operational Constraints
-----------------------

.. _CON-OPS-001:

CON-OPS-001 Availability SLO
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The system SHALL target a Service Level Objective (SLO) of 99.9% availability, excluding scheduled maintenance windows.

**Rationale**: Business continuity requirement.

**Impacts**: :ref:`NFR-OPS-001`

.. _CON-OPS-002:

CON-OPS-002 Maintenance Window
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Scheduled maintenance windows SHALL be defined and communicated in advance. (Details TBD)

**Rationale**: Operational planning.

**Impacts**: :ref:`NFR-OPS-002`

.. _CON-OPS-003:

CON-OPS-003 Load Balancing and Failover
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The system SHALL implement load balancing and automatic failover.

**Rationale**: NIST CSF 2.0 - Availability.

**Impacts**: :ref:`NFR-OPS-003`

.. _CON-OPS-004:

CON-OPS-004 Backup and Redundancy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The system SHALL implement backup and recovery capabilities following the 3-2-1 rule.

**Rationale**: NIST CSF 2.0 - Recovery.

**Impacts**: :ref:`NFR-OPS-004`

Monitoring Constraints
----------------------

.. _CON-MON-001:

CON-MON-001 Continuous Monitoring
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The system SHALL implement continuous monitoring and anomaly detection.

**Rationale**: NIST CSF 2.0 - Detection.

**Impacts**: :ref:`NFR-MON-001`

Development Constraints
-----------------------

.. _CON-DEV-001:

CON-DEV-001 Secure Software Development Lifecycle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
All software development SHALL follow Secure SDLC practices:

*   Security by Design principles.
*   Static and dynamic code analysis.
*   Code review for security vulnerabilities.
*   Dependency vulnerability scanning.

**Rationale**: NIST CSF 2.0 - Software integrity.

**Impacts**: All FRs

.. _CON-DEV-002:

CON-DEV-002 Supply Chain Risk Management
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The project SHALL implement Cyber Supply Chain Risk Management (C-SCRM):

*   Inventory of third-party dependencies.
*   Regular vulnerability assessment of dependencies.
*   Risk evaluation of third-party service providers.

**Rationale**: NIST CSF 2.0 - Supply chain security.

**Impacts**: All FRs

Compliance Constraints
----------------------

.. _CON-COMP-001:

CON-COMP-001 Data Subject Rights
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The system SHALL support data subject rights as required by GDPR and Japan APPI:

*   Right to access personal data.
*   Right to rectification.
*   Right to erasure (right to be forgotten).
*   Data portability.

**Rationale**: Legal compliance with privacy regulations.

**Impacts**: :ref:`FR-TENANT-002`, :ref:`FR-LOG-002`

Performance Constraints
-----------------------

.. _CON-PERF-001:

CON-PERF-001 Response Time and Throughput
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The system SHALL meet performance targets for latency and throughput to ensure a responsive user experience.

**Rationale**: User-Centricity principle - responsive systems improve user satisfaction.

**Impacts**: :ref:`NFR-PERF-001`, :ref:`NFR-PERF-002`, :ref:`NFR-PERF-003`, :ref:`NFR-PERF-004`

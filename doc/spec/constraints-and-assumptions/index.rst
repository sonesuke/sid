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

**Rationale**: Security baseline requirement.

**Impacts**: :ref:`NFR-SEC-001`

.. _CON-SEC-004:

CON-SEC-004 Encryption at Rest
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
All persistent data SHALL be encrypted at rest using AES-256 or equivalent.

**Rationale**: Security baseline requirement.

**Impacts**: :ref:`NFR-SEC-002`

Data Constraints
----------------

.. _CON-DATA-001:

CON-DATA-001 Data Residency
^^^^^^^^^^^^^^^^^^^^^^^^^^^
All customer data SHALL be stored exclusively in data centers located in Japan or the European Union.

**Rationale**: Data sovereignty and regulatory compliance.

**Impacts**: :ref:`NFR-DATA-001`

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

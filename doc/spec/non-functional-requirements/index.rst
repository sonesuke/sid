Non-Functional Requirements
===========================

This section defines quality attributes that apply across the system.

Security Requirements
---------------------

.. _NFR-SEC-001:

NFR-SEC-001 Encryption in Transit
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
All network communications SHALL use TLS 1.2 or higher.

**Constrained by**: :ref:`CON-SEC-003`

.. _NFR-SEC-002:

NFR-SEC-002 Encryption at Rest
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
All persistent data SHALL be encrypted using AES-256 or equivalent algorithm.

**Constrained by**: :ref:`CON-SEC-004`

Data Requirements
-----------------

.. _NFR-DATA-001:

NFR-DATA-001 Data Residency
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Customer data SHALL be stored exclusively in data centers located in Japan or the European Union.

**Constrained by**: :ref:`CON-DATA-001`

Capacity Requirements
---------------------

.. _NFR-CAP-001:

NFR-CAP-001 Tenant Scalability
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The system SHALL scale to support a minimum of 1,000 concurrent active :ref:`Tenants <DAT-TENANT>`.

**Constrained by**: :ref:`CON-CAP-001`

.. _NFR-CAP-002:

NFR-CAP-002 User Scalability
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The system SHALL scale to support a minimum of 10,000 :ref:`Users <DAT-USER>` per :ref:`Tenant <DAT-TENANT>`.

**Constrained by**: :ref:`CON-CAP-002`

Availability Requirements
-------------------------

.. _NFR-OPS-001:

NFR-OPS-001 Service Level Objective
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The system SHALL maintain 99.9% availability, excluding scheduled maintenance windows.

**Constrained by**: :ref:`CON-OPS-001`

.. _NFR-OPS-002:

NFR-OPS-002 Maintenance Scheduling
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Scheduled maintenance windows SHALL be defined and communicated to stakeholders in advance. (Details TBD)

**Constrained by**: :ref:`CON-OPS-002`

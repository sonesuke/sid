System Operations
=================

.. _FR-SYS-001:

FR-SYS-001 Application Registration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The :ref:`TERM-SYS-CP` SHALL allow :ref:`ACT-DEV` to register a new :ref:`Managed Application <DAT-APP>`.
The system SHALL generate a unique Application ID upon registration.

**Quality Attributes**:

*   :ref:`Encryption in Transit <NFR-SEC-001>`
*   :ref:`Key Management <NFR-SEC-004>`
*   :ref:`Least Privilege <NFR-SEC-005>`
*   :ref:`Availability SLO <NFR-OPS-001>`

**Error Conditions**:

*   :ref:`Access Denied <ERR-AUTH-403>`
*   :ref:`Invalid Input <ERR-VAL-400>`
*   :ref:`Conflict <ERR-VAL-409>`

.. _FR-SYS-002:

FR-SYS-002 API Key Management
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The :ref:`TERM-SYS-CP` SHALL allow :ref:`ACT-DEV` to issue :ref:`API Access Keys <DAT-KEY>` for a registered :ref:`Managed Application <DAT-APP>`.
The system SHALL display the Client Secret only once upon issuance.
The system SHALL allow :ref:`ACT-DEV` to revoke existing keys.

**Quality Attributes**:

*   :ref:`Encryption in Transit <NFR-SEC-001>`
*   :ref:`Encryption at Rest <NFR-SEC-002>`
*   :ref:`Key Management <NFR-SEC-004>`
*   :ref:`Least Privilege <NFR-SEC-005>`
*   :ref:`Availability SLO <NFR-OPS-001>`

**Error Conditions**:

*   :ref:`Access Denied <ERR-AUTH-403>`
*   :ref:`Resource Not Found <ERR-RES-404>`

.. _FR-SYS-003:

FR-SYS-003 Application Lifecycle Management
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The :ref:`TERM-SYS-CP` SHALL allow :ref:`ACT-DEV` to update the configuration of a :ref:`Managed Application <DAT-APP>`.
The :ref:`TERM-SYS-CP` SHALL allow :ref:`ACT-DEV` to change the :ref:`Status <DAT-APP>` (e.g., Disable) to block access.

**Quality Attributes**:

*   :ref:`Encryption in Transit <NFR-SEC-001>`
*   :ref:`Least Privilege <NFR-SEC-005>`
*   :ref:`Availability SLO <NFR-OPS-001>`

**Error Conditions**:

*   :ref:`Access Denied <ERR-AUTH-403>`
*   :ref:`Resource Not Found <ERR-RES-404>`

.. _FR-SYS-004:

FR-SYS-004 Operator JIT Provisioning
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The :ref:`TERM-SYS-CP` SHALL automatically provision a :ref:`User <DAT-USER>` record for :ref:`Platform Operators <ACT-OPS>` upon their first successful authentication via the external Identity Provider.

*   The provisioned user SHALL have ``tenant_id`` set to NULL (platform-level user).
*   The user's ``id`` SHALL be used as ``actor_id`` in :ref:`Audit Logs <DAT-LOG>`.
*   Subsequent logins SHALL reuse the existing user record.

**Quality Attributes**:

*   :ref:`Encryption in Transit <NFR-SEC-001>`
*   :ref:`Least Privilege <NFR-SEC-005>`
*   :ref:`Availability SLO <NFR-OPS-001>`
*   :ref:`Continuous Monitoring <NFR-MON-001>`

**Error Conditions**:

*   :ref:`Invalid Credentials <ERR-AUTH-401>`
*   :ref:`Internal Error <ERR-SYS-500>`

.. _FR-SYS-005:

FR-SYS-005 System Health Monitoring
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The :ref:`TERM-SYS-CP` SHALL provide a Dashboard or API for :ref:`Platform Operators <ACT-OPS>` to view the real-time health status of system components.

*   Status SHALL include connectivity to downstream dependencies (DB, Identity Provider, Event Bus).
*   Status SHALL include Error Rates and P99 Latency of key services.

**Quality Attributes**:

*   :ref:`Continuous Monitoring <NFR-MON-001>`
*   :ref:`System Health Alerting <NFR-MON-002>`


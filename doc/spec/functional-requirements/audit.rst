Audit & Logging
===============

.. _FR-LOG-001:

FR-LOG-001 Audit Log Collection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The :ref:`TERM-SYS-CP` SHALL collect security and operational logs from all components via :ref:`API-LOG` and persist them as :ref:`Audit Logs <DAT-LOG>`.

**Realized by**:

*   :ref:`API-LOG`

**Quality Attributes**:

*   :ref:`Encryption in Transit <NFR-SEC-001>`
*   :ref:`Encryption at Rest <NFR-SEC-002>`
*   :ref:`Data Residency <NFR-DATA-001>`
*   :ref:`Availability SLO <NFR-OPS-001>`
*   :ref:`Backup and Redundancy <NFR-OPS-004>`
*   :ref:`Continuous Monitoring <NFR-MON-001>`

**Error Conditions**:

*   :ref:`Internal Error <ERR-SYS-500>`
*   :ref:`Service Unavailable <ERR-SYS-503>`

.. _FR-LOG-002:

FR-LOG-002 Audit Log Export
^^^^^^^^^^^^^^^^^^^^^^^^^^^
The :ref:`TERM-SYS-CP` SHALL allow :ref:`ACT-AUDIT` to export :ref:`Audit Logs <DAT-LOG>` in CSV format.

**Realized by**:

*   :ref:`Auditor Console <IF-AUDIT-CONSOLE>`

**Quality Attributes**:

*   :ref:`Encryption in Transit <NFR-SEC-001>`
*   :ref:`Least Privilege <NFR-SEC-005>`
*   :ref:`Data Residency <NFR-DATA-001>`
*   :ref:`Availability SLO <NFR-OPS-001>`

**Error Conditions**:

*   :ref:`Access Denied <ERR-AUTH-403>`
*   :ref:`Internal Error <ERR-SYS-500>`

.. _FR-LOG-003:

FR-LOG-003 Control Plane Auditing
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The :ref:`TERM-SYS-CP` SHALL record its own state-changing operations (e.g., Tenant Provisioning, User Management) as :ref:`Audit Logs <DAT-LOG>`.

**Quality Attributes**:

*   :ref:`Encryption at Rest <NFR-SEC-002>`
*   :ref:`Data Residency <NFR-DATA-001>`
*   :ref:`Availability SLO <NFR-OPS-001>`
*   :ref:`Continuous Monitoring <NFR-MON-001>`

**Error Conditions**:

*   :ref:`Internal Error <ERR-SYS-500>`

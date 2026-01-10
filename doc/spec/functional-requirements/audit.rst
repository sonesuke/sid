Audit & Logging
===============

.. _FR-LOG-001:

FR-LOG-001 Audit Log Collection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The :ref:`TERM-SYS-CP` SHALL collect security and operational logs from all components via :ref:`API-LOG`.

.. _FR-LOG-002:

FR-LOG-002 Audit Log Export
^^^^^^^^^^^^^^^^^^^^^^^^^^^
The :ref:`TERM-SYS-CP` SHALL allow :ref:`ACT-AUDIT` to export audit logs in CSV format.

.. _FR-LOG-003:

FR-LOG-003 Control Plane Auditing
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The :ref:`TERM-SYS-CP` SHALL record its own state-changing operations (e.g., Tenant Provisioning, User Management) as audit logs.

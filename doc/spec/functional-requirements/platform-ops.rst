Platform Operations
===================

.. _FR-OPS-001:

FR-OPS-001 Tenant Status Management
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The :ref:`TERM-SYS-CP` SHALL allow :ref:`ACT-OPS` to modify the status of a :ref:`Tenant <DAT-TENANT>` (e.g., Active, Suspended).
When a :ref:`Tenant <DAT-TENANT>` is Suspended, the system SHALL revoke access for all :ref:`Users <DAT-USER>` associated with that tenant.

**Realized by**: :ref:`Operator Console <IF-OPS-CONSOLE>`

**Quality Attributes**:

*   :ref:`Encryption in Transit <NFR-SEC-001>`
*   :ref:`Least Privilege <NFR-SEC-005>`
*   :ref:`Tenant Scalability <NFR-CAP-001>`
*   :ref:`Availability SLO <NFR-OPS-001>`

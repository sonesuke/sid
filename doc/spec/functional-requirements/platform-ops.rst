Platform Operations
===================

.. _FR-OPS-001:

FR-OPS-001 Tenant Status Management
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The :ref:`TERM-SYS-CP` SHALL allow :ref:`ACT-OPS` to modify the status of a :ref:`Tenant <DAT-TENANT>` (e.g., Active, Suspended).
When a :ref:`Tenant <DAT-TENANT>` is Suspended, the system SHALL revoke access for all :ref:`Users <DAT-USER>` associated with that tenant.

**Realized by**:

*   :ref:`Operator Console <IF-OPS-CONSOLE>`

**Quality Attributes**:

*   :ref:`Encryption in Transit <NFR-SEC-001>`
*   :ref:`Least Privilege <NFR-SEC-005>`
*   :ref:`Tenant Scalability <NFR-CAP-001>`
*   :ref:`Availability SLO <NFR-OPS-001>`

**Error Conditions**:

*   :ref:`Access Denied <ERR-AUTH-403>`
*   :ref:`Resource Not Found <ERR-RES-404>`

.. _FR-OPS-002:

FR-OPS-002 Tenant Deletion
^^^^^^^^^^^^^^^^^^^^^^^^^^
The :ref:`TERM-SYS-CP` SHALL allow :ref:`ACT-OPS` to permanently delete a :ref:`Tenant <DAT-TENANT>` and all associated data upon contract termination or deletion request.

*   Upon deletion request, the tenant SHALL enter a 30-day grace period (recoverable).
*   After the grace period, all tenant data SHALL be permanently and irrecoverably deleted.
*   Deleted data includes: :ref:`Users <DAT-USER>`, :ref:`Sessions <DAT-SESSION>`, :ref:`Audit Logs <DAT-LOG>`, :ref:`Billing Events <DAT-BILL-EVENT>`, and configuration.

**Constrained by**: :ref:`CON-COMP-001`

**Realized by**:

*   :ref:`Operator Console <IF-OPS-CONSOLE>`

**Quality Attributes**:

*   :ref:`Encryption in Transit <NFR-SEC-001>`
*   :ref:`Least Privilege <NFR-SEC-005>`
*   :ref:`Availability SLO <NFR-OPS-001>`

**Error Conditions**:

*   :ref:`Access Denied <ERR-AUTH-403>`
*   :ref:`Resource Not Found <ERR-RES-404>`
*   :ref:`Resource Gone <ERR-RES-410>`

.. _FR-OPS-003:

FR-OPS-003 Data Retention Enforcement
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The :ref:`TERM-SYS-CP` SHALL automatically enforce data retention policies:

*   :ref:`Audit Logs <DAT-LOG>` SHALL be retained for a minimum of 7 years, then securely deleted.
*   :ref:`Billing Events <DAT-BILL-EVENT>` SHALL be retained for a minimum of 5 years, then securely deleted.

**Constrained by**: :ref:`CON-DATA-002`, :ref:`CON-DATA-003`

**Realized by**:

*   :ref:`TERM-SYS-CP` (automated process)

**Quality Attributes**:

*   :ref:`Encryption at Rest <NFR-SEC-002>`
*   :ref:`Data Residency <NFR-DATA-001>`
*   :ref:`Availability SLO <NFR-OPS-001>`

**Error Conditions**:

*   :ref:`Internal Error <ERR-SYS-500>`

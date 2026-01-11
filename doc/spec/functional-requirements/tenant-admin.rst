Tenant Administration
=====================

.. _FR-TENANT-001:

FR-TENANT-001 User Invitation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The :ref:`TERM-SYS-CP` SHALL allow Tenant Owners and Administrators to invite new :ref:`Users <DAT-USER>` to their :ref:`Tenant <DAT-TENANT>`.
This process SHALL create a :ref:`User Invitation <DAT-INVITE>` record.

*   Invitations SHALL have a configurable expiration period (default: 7 days).
*   Expired invitations SHALL be marked as invalid and cannot be used for registration.

**Realized by**:

*   :ref:`Tenant Administration Console <IF-TENANT-CONSOLE>`

**Quality Attributes**:

*   :ref:`Encryption in Transit <NFR-SEC-001>`
*   :ref:`Least Privilege <NFR-SEC-005>`
*   :ref:`User Scalability <NFR-CAP-002>`
*   :ref:`Availability SLO <NFR-OPS-001>`

**Error Conditions**:

*   :ref:`Access Denied <ERR-AUTH-403>`
*   :ref:`Conflict <ERR-VAL-409>`
*   :ref:`Business Rule Violation <ERR-VAL-422>`

.. _FR-TENANT-002:

FR-TENANT-002 User Deletion
^^^^^^^^^^^^^^^^^^^^^^^^^^^
The :ref:`TERM-SYS-CP` SHALL allow Tenant Owners and Administrators to delete :ref:`Users <DAT-USER>` from their :ref:`Tenant <DAT-TENANT>`.
When a user is deleted, the system SHALL invalidate all active :ref:`Sessions <DAT-SESSION>` for that user.

**Realized by**:

*   :ref:`Tenant Administration Console <IF-TENANT-CONSOLE>`

**Quality Attributes**:

*   :ref:`Encryption in Transit <NFR-SEC-001>`
*   :ref:`Encryption at Rest <NFR-SEC-002>`
*   :ref:`Least Privilege <NFR-SEC-005>`
*   :ref:`Availability SLO <NFR-OPS-001>`

**Error Conditions**:

*   :ref:`Access Denied <ERR-AUTH-403>`
*   :ref:`Resource Not Found <ERR-RES-404>`

.. _FR-TENANT-003:

FR-TENANT-003 Contract Modification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The :ref:`TERM-SYS-CP` SHALL allow only Tenant Owners to modify the tenant's subscription contract (specifically :ref:`Tenant.plan <DAT-TENANT>`).

**Realized by**:

*   :ref:`Tenant Administration Console <IF-TENANT-CONSOLE>`

**Quality Attributes**:

*   :ref:`Encryption in Transit <NFR-SEC-001>`
*   :ref:`Least Privilege <NFR-SEC-005>`
*   :ref:`Tenant Scalability <NFR-CAP-001>`
*   :ref:`Availability SLO <NFR-OPS-001>`

**Error Conditions**:

*   :ref:`Access Denied <ERR-AUTH-403>`

.. _FR-TENANT-004:

FR-TENANT-004 User Role Management
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The :ref:`TERM-SYS-CP` SHALL allow Tenant Owners and Administrators to modify the :ref:`Roles <DAT-ROLE>` of existing :ref:`Users <DAT-USER>` within their :ref:`Tenant <DAT-TENANT>`.
When a role is updated, the system SHALL invalidate all active :ref:`Sessions <DAT-SESSION>` for the target user.

**Realized by**:

*   :ref:`Tenant Administration Console <IF-TENANT-CONSOLE>`

**Quality Attributes**:

*   :ref:`Encryption in Transit <NFR-SEC-001>`
*   :ref:`Least Privilege <NFR-SEC-005>`
*   :ref:`Availability SLO <NFR-OPS-001>`

**Error Conditions**:

*   :ref:`Access Denied <ERR-AUTH-403>`
*   :ref:`Resource Not Found <ERR-RES-404>`

.. _FR-TENANT-006:

FR-TENANT-006 User Status Management
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The :ref:`TERM-SYS-CP` SHALL allow Tenant Owners and Administrators to modify the :ref:`Status <DAT-USER>` of existing :ref:`Users <DAT-USER>` (e.g., Enable, Disable).
When a user is Disabled, the system SHALL invalidate all active :ref:`Sessions <DAT-SESSION>` for that user.

**Realized by**:

*   :ref:`Tenant Administration Console <IF-TENANT-CONSOLE>`

**Quality Attributes**:

*   :ref:`Encryption in Transit <NFR-SEC-001>`
*   :ref:`Least Privilege <NFR-SEC-005>`
*   :ref:`Availability SLO <NFR-OPS-001>`

**Error Conditions**:

*   :ref:`Access Denied <ERR-AUTH-403>`
*   :ref:`Resource Not Found <ERR-RES-404>`

.. _FR-TENANT-007:

FR-TENANT-007 Invitation Resend
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The :ref:`TERM-SYS-CP` SHALL allow Tenant Owners and Administrators to resend an invitation to a user whose invitation has expired or was not received.

*   Resending SHALL invalidate the previous :ref:`User Invitation <DAT-INVITE>` and create a new one.
*   The new invitation SHALL have a fresh expiration period.

**Realized by**:

*   :ref:`Tenant Administration Console <IF-TENANT-CONSOLE>`

**Quality Attributes**:

*   :ref:`Encryption in Transit <NFR-SEC-001>`
*   :ref:`Least Privilege <NFR-SEC-005>`
*   :ref:`Availability SLO <NFR-OPS-001>`

**Error Conditions**:

*   :ref:`Access Denied <ERR-AUTH-403>`
*   :ref:`Resource Not Found <ERR-RES-404>`

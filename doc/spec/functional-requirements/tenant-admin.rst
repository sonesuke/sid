Tenant Administration
=====================

.. _FR-TENANT-001:

FR-TENANT-001 User Invitation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The :ref:`TERM-SYS-CP` SHALL allow Tenant Owners and Administrators to invite new :ref:`Users <DAT-USER>` to their :ref:`Tenant <DAT-TENANT>`.
This process SHALL create a :ref:`User Invitation <DAT-INVITE>` record.

**Realized by**: :ref:`Tenant Administration Console <IF-TENANT-CONSOLE>`

.. _FR-TENANT-002:

FR-TENANT-002 User Deletion
^^^^^^^^^^^^^^^^^^^^^^^^^^^
The :ref:`TERM-SYS-CP` SHALL allow Tenant Owners and Administrators to delete :ref:`Users <DAT-USER>` from their :ref:`Tenant <DAT-TENANT>`.

**Realized by**: :ref:`Tenant Administration Console <IF-TENANT-CONSOLE>`

When a user is deleted, the system SHALL invalidate all active :ref:`Sessions <DAT-SESSION>` for that user.

.. _FR-TENANT-003:

FR-TENANT-003 Contract Modification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The :ref:`TERM-SYS-CP` SHALL allow only Tenant Owners to modify the tenant's subscription contract (specifically :ref:`Tenant.plan <DAT-TENANT>`).

**Realized by**: :ref:`Tenant Administration Console <IF-TENANT-CONSOLE>`

.. _FR-TENANT-004:

FR-TENANT-004 User Role Management
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The :ref:`TERM-SYS-CP` SHALL allow Tenant Owners and Administrators to modify the :ref:`Roles <DAT-ROLE>` of existing :ref:`Users <DAT-USER>` within their :ref:`Tenant <DAT-TENANT>`.
When a role is updated, the system SHALL invalidate all active :ref:`Sessions <DAT-SESSION>` for the target user.

**Realized by**: :ref:`Tenant Administration Console <IF-TENANT-CONSOLE>`

.. _FR-TENANT-006:

FR-TENANT-006 User Status Management
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The :ref:`TERM-SYS-CP` SHALL allow Tenant Owners and Administrators to modify the :ref:`Status <DAT-USER>` of existing :ref:`Users <DAT-USER>` (e.g., Enable, Disable).
When a user is Disabled, the system SHALL invalidate all active :ref:`Sessions <DAT-SESSION>` for that user.

**Realized by**: :ref:`Tenant Administration Console <IF-TENANT-CONSOLE>`

Tenant Provisioning & Lifecycle
===============================

.. _UC-PROV-001:

UC-PROV-001 Tenant Provisioning
-------------------------------
**Actor**: :ref:`Platform Operator <ACT-OPS>`

**Description**:
The :ref:`Platform Operator <ACT-OPS>` creates a new tenant configuration and enables subscribed features, allowing the tenant to immediately access the :ref:`Managed Application <TERM-APP-TARGET>`.

**Trigger**:
A new customer subscription is confirmed.

**Preconditions**:

1. The :ref:`Platform Operator <ACT-OPS>` is logged in.

**Postconditions**:

1. A new tenant entity is created in the :ref:`Control Plane <TERM-SYS-CP>`.
2. Initial :ref:`Tenant User <ACT-USER>` (Role: Owner) is provisioned.
3. Feature flags corresponding to the subscription plan are active.

**Scenario**:

1. The :ref:`Platform Operator <ACT-OPS>` navigates to the **Operator Console**.
2. The :ref:`Platform Operator <ACT-OPS>` enters tenant details (Name, Domain, Plan) and the email address for the initial Owner.
3. The :ref:`Platform Operator <ACT-OPS>` selects the :ref:`Managed Application <TERM-APP-TARGET>` to enable.
4. The :ref:`Platform Operator <ACT-OPS>` selects the "Provision" action.
5. The :ref:`Control Plane <TERM-SYS-CP>` creates the tenant and the initial :ref:`Tenant User <ACT-USER>` (Role: Owner).
6. The :ref:`Control Plane <TERM-SYS-CP>` enables access to the :ref:`Managed Application <TERM-APP-TARGET>`.

**Related Requirements**:

*   :ref:`Flag Configuration <FR-FLAG-001>`
*   :ref:`User Invitation <FR-TENANT-001>`
*   :ref:`Contract Modification <FR-TENANT-003>`
*   :ref:`Control Plane Auditing <FR-LOG-003>`

.. _UC-TENANT-SUSPEND:

UC-TENANT-SUSPEND Tenant Suspension
-----------------------------------
**Actor**: :ref:`Platform Operator <ACT-OPS>`

**Description**:
The :ref:`Platform Operator <ACT-OPS>` suspends a tenant's access to the managed application, usually due to non-payment or policy violation.

**Trigger**:
The :ref:`Platform Operator <ACT-OPS>` selects "Suspend Tenant" in the **Operator Console**.

**Preconditions**:

1. The :ref:`Platform Operator <ACT-OPS>` is logged in.
2. The target tenant is currently Active.

**Postconditions**:

1. The :ref:`Tenant <DAT-TENANT>` status is updated to Suspended.
2. All :ref:`Users <DAT-USER>` under the tenant are immediately denied access.

**Scenario**:

1. The :ref:`Platform Operator <ACT-OPS>` searches for the tenant in the **Operator Console**.
2. The :ref:`Platform Operator <ACT-OPS>` selects the "Suspend" action.
3. The :ref:`Platform Operator <ACT-OPS>` provides a reason (optional).
4. The :ref:`Platform Operator <ACT-OPS>` confirms the action.
5. The :ref:`Control Plane <TERM-SYS-CP>` invokes the suspension logic.

**Related Requirements**:

*   :ref:`Tenant Status Management <FR-OPS-001>`
*   :ref:`Control Plane Auditing <FR-LOG-003>`

.. _UC-OPS-TENANT-DELETE:

UC-OPS-TENANT-DELETE Tenant Deletion
------------------------------------
**Actor**: :ref:`Platform Operator <ACT-OPS>`

**Description**:
The :ref:`Platform Operator <ACT-OPS>` permanently deletes a tenant and all associated data upon contract termination or deletion request.

**Trigger**:
The :ref:`Platform Operator <ACT-OPS>` selects "Delete Tenant" in the **Operator Console**.

**Preconditions**:

1. The :ref:`Platform Operator <ACT-OPS>` is logged in.
2. The target tenant exists.

**Postconditions**:

1. The :ref:`Tenant <DAT-TENANT>` enters a 30-day grace period (recoverable).
2. After the grace period, all tenant data is permanently deleted.

**Scenario**:

1. The :ref:`Platform Operator <ACT-OPS>` searches for the tenant in the **Operator Console**.
2. The :ref:`Platform Operator <ACT-OPS>` selects the "Delete" action.
3. The :ref:`Platform Operator <ACT-OPS>` confirms the action with explicit acknowledgment.
4. The :ref:`Control Plane <TERM-SYS-CP>` marks the tenant for deletion (30-day grace).
5. After the grace period, the :ref:`Control Plane <TERM-SYS-CP>` permanently deletes all related data.

**Related Requirements**:

*   :ref:`Tenant Deletion <FR-OPS-002>`
*   :ref:`Control Plane Auditing <FR-LOG-003>`
*   :ref:`Data Subject Rights <CON-COMP-001>`

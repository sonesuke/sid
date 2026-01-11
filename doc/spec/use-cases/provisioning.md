# Tenant Provisioning & Lifecycle

<a id="UC-PROV-001"></a>

## UC-PROV-001 Tenant Provisioning
**Actor**: [Platform Operator ](../actors/list.md#ACT-OPS)

**Description**:
The [Platform Operator ](../actors/list.md#ACT-OPS) creates a new tenant configuration and enables subscribed features, allowing the tenant to immediately access the [Managed Application ](../terminology/definitions.md#TERM-APP-TARGET).

**Trigger**:
A new customer subscription is confirmed.

**Preconditions**:

1. The [Platform Operator ](../actors/list.md#ACT-OPS) is logged in.

**Postconditions**:

1. A new tenant entity is created in the [Control Plane ](../terminology/definitions.md#TERM-SYS-CP).
2. Initial [Tenant User ](../actors/list.md#ACT-USER) (Role: Owner) is provisioned.
3. Feature flags corresponding to the subscription plan are active.

**Scenario**:

1. The [Platform Operator ](../actors/list.md#ACT-OPS) navigates to the **Operator Console**.
2. The [Platform Operator ](../actors/list.md#ACT-OPS) enters tenant details (Name, Domain, Plan) and the email address for the initial Owner.
3. The [Platform Operator ](../actors/list.md#ACT-OPS) selects the [Managed Application ](../terminology/definitions.md#TERM-APP-TARGET) to enable.
4. The [Platform Operator ](../actors/list.md#ACT-OPS) selects the "Provision" action.
5. The [Control Plane ](../terminology/definitions.md#TERM-SYS-CP) creates the tenant and the initial [Tenant User ](../actors/list.md#ACT-USER) (Role: Owner).
6. The [Control Plane ](../terminology/definitions.md#TERM-SYS-CP) enables access to the [Managed Application ](../terminology/definitions.md#TERM-APP-TARGET).

**Related Requirements**:

*   [Flag Configuration ](../functional-requirements/feature-flags.md#FR-FLAG-001)
*   [User Invitation ](../functional-requirements/tenant-admin.md#FR-TENANT-001)
*   [Contract Modification ](../functional-requirements/tenant-admin.md#FR-TENANT-003)
*   [Control Plane Auditing ](../functional-requirements/audit.md#FR-LOG-003)

<a id="UC-TENANT-SUSPEND"></a>

## UC-TENANT-SUSPEND Tenant Suspension
**Actor**: [Platform Operator ](../actors/list.md#ACT-OPS)

**Description**:
The [Platform Operator ](../actors/list.md#ACT-OPS) suspends a tenant's access to the managed application, usually due to non-payment or policy violation.

**Trigger**:
The [Platform Operator ](../actors/list.md#ACT-OPS) selects "Suspend Tenant" in the **Operator Console**.

**Preconditions**:

1. The [Platform Operator ](../actors/list.md#ACT-OPS) is logged in.
2. The target tenant is currently Active.

**Postconditions**:

1. The [Tenant ](../data-model/schema.md#DAT-TENANT) status is updated to Suspended.
2. All [Users ](../data-model/schema.md#DAT-USER) under the tenant are immediately denied access.

**Scenario**:

1. The [Platform Operator ](../actors/list.md#ACT-OPS) searches for the tenant in the **Operator Console**.
2. The [Platform Operator ](../actors/list.md#ACT-OPS) selects the "Suspend" action.
3. The [Platform Operator ](../actors/list.md#ACT-OPS) provides a reason (optional).
4. The [Platform Operator ](../actors/list.md#ACT-OPS) confirms the action.
5. The [Control Plane ](../terminology/definitions.md#TERM-SYS-CP) invokes the suspension logic.

**Related Requirements**:

*   [Tenant Status Management ](../functional-requirements/platform-ops.md#FR-OPS-001)
*   [Control Plane Auditing ](../functional-requirements/audit.md#FR-LOG-003)

<a id="UC-OPS-TENANT-DELETE"></a>

## UC-OPS-TENANT-DELETE Tenant Deletion
**Actor**: [Platform Operator ](../actors/list.md#ACT-OPS)

**Description**:
The [Platform Operator ](../actors/list.md#ACT-OPS) permanently deletes a tenant and all associated data upon contract termination or deletion request.

**Trigger**:
The [Platform Operator ](../actors/list.md#ACT-OPS) selects "Delete Tenant" in the **Operator Console**.

**Preconditions**:

1. The [Platform Operator ](../actors/list.md#ACT-OPS) is logged in.
2. The target tenant exists.

**Postconditions**:

1. The [Tenant ](../data-model/schema.md#DAT-TENANT) enters a 30-day grace period (recoverable).
2. After the grace period, all tenant data is permanently deleted.

**Scenario**:

1. The [Platform Operator ](../actors/list.md#ACT-OPS) searches for the tenant in the **Operator Console**.
2. The [Platform Operator ](../actors/list.md#ACT-OPS) selects the "Delete" action.
3. The [Platform Operator ](../actors/list.md#ACT-OPS) confirms the action with explicit acknowledgment.
4. The [Control Plane ](../terminology/definitions.md#TERM-SYS-CP) marks the tenant for deletion (30-day grace).
5. After the grace period, the [Control Plane ](../terminology/definitions.md#TERM-SYS-CP) permanently deletes all related data.

**Related Requirements**:

*   [Tenant Deletion ](../functional-requirements/platform-ops.md#FR-OPS-002)
*   [Control Plane Auditing ](../functional-requirements/audit.md#FR-LOG-003)
*   [Data Subject Rights ](../constraints-and-assumptions/index.md#CON-COMP-001)

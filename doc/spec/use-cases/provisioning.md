
# Tenant Provisioning & Lifecycle

<a id="UC-PROV-001"></a>

## UC-PROV-001 Tenant Provisioning

**Actor**: [ACT-OPS (Platform Operator)](../actors/platform-operator.md#ACT-OPS)

**Description**:
The [ACT-OPS (Platform Operator)](../actors/platform-operator.md#ACT-OPS) creates a new tenant configuration and enables subscribed features, allowing the tenant to immediately access the [TERM-APP-TARGET (Managed Application)](../terminology/definitions.md#TERM-APP-TARGET).

**Trigger**:
A new customer subscription is confirmed.

**Preconditions**:

1. The [ACT-OPS (Platform Operator)](../actors/platform-operator.md#ACT-OPS) is logged in.

**Postconditions**:

1. A new tenant entity is created in the [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP).
2. Initial [ACT-USER (Tenant User)](../actors/tenant-user.md#ACT-USER) (Role: Owner) is provisioned.
3. Feature flags corresponding to the subscription plan are active.

**Scenario**:

1. The [ACT-OPS (Platform Operator)](../actors/platform-operator.md#ACT-OPS) navigates to the **Operator Console**.
2. The [ACT-OPS (Platform Operator)](../actors/platform-operator.md#ACT-OPS) enters tenant details (Name, Domain, Plan) and the email address for the initial Owner.
3. The [ACT-OPS (Platform Operator)](../actors/platform-operator.md#ACT-OPS) selects the [TERM-APP-TARGET (Managed Application)](../terminology/definitions.md#TERM-APP-TARGET) to enable.
4. The [ACT-OPS (Platform Operator)](../actors/platform-operator.md#ACT-OPS) selects the "Provision" action.
5. The [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP) creates the tenant and the initial [ACT-USER (Tenant User)](../actors/tenant-user.md#ACT-USER) (Role: Owner).
6. The [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP) enables access to the [TERM-APP-TARGET (Managed Application)](../terminology/definitions.md#TERM-APP-TARGET).

**Related Requirements**:

* [FR-FLAG-001 (Flag Configuration)](../functional-requirements/feature-flags.md#FR-FLAG-001)

* [FR-TENANT-001 (User Invitation)](../functional-requirements/tenant-admin.md#FR-TENANT-001)
* [FR-TENANT-003 (Contract Modification)](../functional-requirements/tenant-admin.md#FR-TENANT-003)
* [FR-LOG-003 (Control Plane Auditing)](../functional-requirements/audit.md#FR-LOG-003)

<a id="UC-TENANT-SUSPEND"></a>

## UC-TENANT-SUSPEND Tenant Suspension

**Actor**: [ACT-OPS (Platform Operator)](../actors/platform-operator.md#ACT-OPS)

**Description**:
The [ACT-OPS (Platform Operator)](../actors/platform-operator.md#ACT-OPS) suspends a tenant's access to the managed application, usually due to non-payment or policy violation.

**Trigger**:
The [ACT-OPS (Platform Operator)](../actors/platform-operator.md#ACT-OPS) selects "Suspend Tenant" in the **Operator Console**.

**Preconditions**:

1. The [ACT-OPS (Platform Operator)](../actors/platform-operator.md#ACT-OPS) is logged in.
2. The target tenant is currently Active.

**Postconditions**:

1. The [DAT-TENANT (Tenants)](../data-model/schema.md#DAT-TENANT) status is updated to Suspended.
2. All [DAT-USER (Users)](../data-model/schema.md#DAT-USER) under the tenant are immediately denied access.

**Scenario**:

1. The [ACT-OPS (Platform Operator)](../actors/platform-operator.md#ACT-OPS) searches for the tenant in the **Operator Console**.
2. The [ACT-OPS (Platform Operator)](../actors/platform-operator.md#ACT-OPS) selects the "Suspend" action.
3. The [ACT-OPS (Platform Operator)](../actors/platform-operator.md#ACT-OPS) provides a reason (optional).
4. The [ACT-OPS (Platform Operator)](../actors/platform-operator.md#ACT-OPS) confirms the action.
5. The [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP) invokes the suspension logic.

**Related Requirements**:

* [FR-OPS-001 (Tenant Status Management)](../functional-requirements/platform-ops.md#FR-OPS-001)
* [FR-LOG-003 (Control Plane Auditing)](../functional-requirements/audit.md#FR-LOG-003)

<a id="UC-OPS-TENANT-DELETE"></a>

## UC-OPS-TENANT-DELETE Tenant Deletion

**Actor**: [ACT-OPS (Platform Operator)](../actors/platform-operator.md#ACT-OPS)

**Description**:
The [ACT-OPS (Platform Operator)](../actors/platform-operator.md#ACT-OPS) permanently deletes a tenant and all associated data upon contract termination or deletion request.

**Trigger**:
The [ACT-OPS (Platform Operator)](../actors/platform-operator.md#ACT-OPS) selects "Delete Tenant" in the **Operator Console**.

**Preconditions**:

1. The [ACT-OPS (Platform Operator)](../actors/platform-operator.md#ACT-OPS) is logged in.
2. The target tenant exists.

**Postconditions**:

1. The [DAT-TENANT (Tenants)](../data-model/schema.md#DAT-TENANT) enters a 30-day grace period (recoverable).
2. After the grace period, all tenant data is permanently deleted.

**Scenario**:

1. The [ACT-OPS (Platform Operator)](../actors/platform-operator.md#ACT-OPS) searches for the tenant in the **Operator Console**.
2. The [ACT-OPS (Platform Operator)](../actors/platform-operator.md#ACT-OPS) selects the "Delete" action.
3. The [ACT-OPS (Platform Operator)](../actors/platform-operator.md#ACT-OPS) confirms the action with explicit acknowledgment.
4. The [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP) marks the tenant for deletion (30-day grace).
5. After the grace period, the [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP) permanently deletes all related data.

**Related Requirements**:

* [FR-OPS-002 (Tenant Deletion)](../functional-requirements/platform-ops.md#FR-OPS-002)
* [FR-OPS-003 (Data Retention Enforcement)](../functional-requirements/platform-ops.md#FR-OPS-003)
* [FR-LOG-003 (Control Plane Auditing)](../functional-requirements/audit.md#FR-LOG-003)
* [FR-AUTH-006 (Password Policy Configuration)](../functional-requirements/auth.md#FR-AUTH-006)

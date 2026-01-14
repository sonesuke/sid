# System Deployment

<a id="UC-DEV-REGISTER"></a>

## UC-DEV-REGISTER Application Registration

**Actor**: [Developer](../actors/list.md#ACT-DEV)

**Description**:
The [Developer](../actors/list.md#ACT-DEV) registers the [Managed Application](../terminology/definitions.md#TERM-APP-TARGET) with the Control Plane to obtain credentials for API access. This is typically done as part of the initial system deployment.

**Trigger**:
The [Developer](../actors/list.md#ACT-DEV) initiates the "Register System" workflow (via CLI or script).

**Preconditions**:

1. The [Developer](../actors/list.md#ACT-DEV) has administrative access to the Control Plane infrastructure.

**Postconditions**:

1. A [Managed Application](../data-model/schema.md#DAT-APP) record is created.
2. An [API Access Key](../data-model/schema.md#DAT-KEY) is issued and returned to the [Developer](../actors/list.md#ACT-DEV).
3. The [Managed Application](../terminology/definitions.md#TERM-APP-TARGET) is configured with the key.

**Scenario**:

1. The [Developer](../actors/list.md#ACT-DEV) submits the application metadata (Name, Environment).
2. The [Control Plane](../terminology/definitions.md#TERM-SYS-CP) creates the application record.
3. The [Control Plane](../terminology/definitions.md#TERM-SYS-CP) generates a client ID and secret.
4. The [Control Plane](../terminology/definitions.md#TERM-SYS-CP) stores the hashed secret.
5. The [Control Plane](../terminology/definitions.md#TERM-SYS-CP) returns the ID and Secret to the [Developer](../actors/list.md#ACT-DEV).

**Related Requirements**:

* [Application Registration](../functional-requirements/system-ops.md#FR-SYS-001)
* [API Key Management](../functional-requirements/system-ops.md#FR-SYS-002)

<a id="UC-DEV-UPDATE"></a>

## UC-DEV-UPDATE Application Update

**Actor**: [Developer](../actors/list.md#ACT-DEV)

**Description**:
The [Developer](../actors/list.md#ACT-DEV) updates the configuration or status of a [Managed Application](../data-model/schema.md#DAT-APP). This includes disabling the application to prevent access.

**Trigger**:
The [Developer](../actors/list.md#ACT-DEV) initiates a deployment or CLI command to update the application.

**Preconditions**:

1. The [Developer](../actors/list.md#ACT-DEV) has valid administrative credentials.
2. The target [Managed Application](../data-model/schema.md#DAT-APP) exists.

**Postconditions**:

1. The [Managed Application](../data-model/schema.md#DAT-APP) record is updated.
2. If status is set to Disabled, all API access is blocked.

**Scenario**:

1. The [Developer](../actors/list.md#ACT-DEV) submits the update request (e.g., set status to Disabled).
2. The [Control Plane](../terminology/definitions.md#TERM-SYS-CP) validates the request.
3. The [Control Plane](../terminology/definitions.md#TERM-SYS-CP) updates the application record.
4. The [Control Plane](../terminology/definitions.md#TERM-SYS-CP) applies the new state (e.g., blocking incoming API calls).

**Related Requirements**:

* [Application Lifecycle Management](../functional-requirements/system-ops.md#FR-SYS-003)

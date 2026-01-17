# System Deployment

<a id="UC-DEV-REGISTER"></a>

## UC-DEV-REGISTER Application Registration

**Actor**: [ACT-DEV (Developer)](../actors/list.md#ACT-DEV)

**Description**:
The [ACT-DEV (Developer)](../actors/list.md#ACT-DEV) registers the [TERM-APP-TARGET (Managed Application)](../terminology/definitions.md#TERM-APP-TARGET) with the Control Plane to obtain credentials for API access. This is typically done as part of the initial system deployment.

**Trigger**:
The [ACT-DEV (Developer)](../actors/list.md#ACT-DEV) initiates the "Register System" workflow (via CLI or script).

**Preconditions**:

1. The [ACT-DEV (Developer)](../actors/list.md#ACT-DEV) has administrative access to the Control Plane infrastructure.

**Postconditions**:

1. A [DAT-APP (Managed Applications)](../data-model/schema.md#DAT-APP) record is created.
2. An [DAT-KEY (API Access Keys)](../data-model/schema.md#DAT-KEY) is issued and returned to the [ACT-DEV (Developer)](../actors/list.md#ACT-DEV).
3. The [TERM-APP-TARGET (Managed Application)](../terminology/definitions.md#TERM-APP-TARGET) is configured with the key.

**Scenario**:

1. The [ACT-DEV (Developer)](../actors/list.md#ACT-DEV) submits the application metadata (Name, Environment).
2. The [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP) creates the application record.
3. The [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP) generates a client ID and secret.
4. The [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP) stores the hashed secret.
5. The [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP) returns the ID and Secret to the [ACT-DEV (Developer)](../actors/list.md#ACT-DEV).

**Related Requirements**:

* [FR-SYS-001 (Application Registration)](../functional-requirements/system-ops.md#FR-SYS-001)
* [FR-SYS-002 (API Key Management)](../functional-requirements/system-ops.md#FR-SYS-002)

<a id="UC-DEV-UPDATE"></a>

## UC-DEV-UPDATE Application Update

**Actor**: [ACT-DEV (Developer)](../actors/list.md#ACT-DEV)

**Description**:
The [ACT-DEV (Developer)](../actors/list.md#ACT-DEV) updates the configuration or status of a [DAT-APP (Managed Applications)](../data-model/schema.md#DAT-APP). This includes disabling the application to prevent access.

**Trigger**:
The [ACT-DEV (Developer)](../actors/list.md#ACT-DEV) initiates a deployment or CLI command to update the application.

**Preconditions**:

1. The [ACT-DEV (Developer)](../actors/list.md#ACT-DEV) has valid administrative credentials.
2. The target [DAT-APP (Managed Applications)](../data-model/schema.md#DAT-APP) exists.

**Postconditions**:

1. The [DAT-APP (Managed Applications)](../data-model/schema.md#DAT-APP) record is updated.
2. If status is set to Disabled, all API access is blocked.

**Scenario**:

1. The [ACT-DEV (Developer)](../actors/list.md#ACT-DEV) submits the update request (e.g., set status to Disabled).
2. The [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP) validates the request.
3. The [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP) updates the application record.
4. The [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP) applies the new state (e.g., blocking incoming API calls).

**Related Requirements**:

* [FR-SYS-003 (Application Lifecycle Management)](../functional-requirements/system-ops.md#FR-SYS-003)

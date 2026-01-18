
# System Operations

<a id="UC-OPS-LOGIN"></a>

## UC-OPS-LOGIN Operator Login

**Actor**: [ACT-OPS (Platform Operator)](../actors/platform-operator.md#ACT-OPS)

**Description**:
The [ACT-OPS (Platform Operator)](../actors/platform-operator.md#ACT-OPS) logs in to the **Operator Console**. JIT provisioning occurs if it is their first login.

**Trigger**:
The [ACT-OPS (Platform Operator)](../actors/platform-operator.md#ACT-OPS) accesses the Operator Console URL.

**Preconditions**:

1. The [ACT-OPS (Platform Operator)](../actors/platform-operator.md#ACT-OPS) has a valid account in the external IdP.

**Postconditions**:

1. The operator is authenticated.
2. An operator user record exists in the system (JIT provisioned if new).

**Scenario**:

1. The operator navigates to the Console.
2. The operator is redirected to the IdP and authenticates.
3. The system validates the IdP token.
4. The system checks if the user record exists; if not, it creates one.
5. The operator is granted access.

**Related Requirements**:

* [FR-SYS-004 (Operator JIT Provisioning)](../functional-requirements/system-ops.md#FR-SYS-004)

<a id="UC-OPS-MONITOR"></a>

## UC-OPS-MONITOR System Monitoring

**Actor**: [ACT-OPS (Platform Operator)](../actors/platform-operator.md#ACT-OPS)

**Description**:
The [ACT-OPS (Platform Operator)](../actors/platform-operator.md#ACT-OPS) views system usage metrics to ensure platform health.

**Trigger**:
The operator navigates to the "Dashboard" in the Operator Console.

**Preconditions**:

1. Expenses/Usage data is being collected.

**Postconditions**:

1. Metrics are displayed.

**Scenario**:

1. The operator selects "System Metrics".
2. The system queries usage data.
3. The system displays graphs for CPU, Memory, and Tenant Count.

**Related Requirements**:

* [FR-SYS-005 (System Usage Metrics)](../functional-requirements/system-ops.md#FR-SYS-005)

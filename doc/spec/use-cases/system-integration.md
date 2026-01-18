# System Integration

This section describes the automated interactions between Managed Applications and the Control Plane.

<a id="UC-SYS-APP-AUTH"></a>

## UC-SYS-APP-AUTH Feature Flag Retrieval

**Actor**: [TERM-APP-TARGET (Managed Application)](../terminology/definitions.md#TERM-APP-TARGET) (System)

**Description**:
The [TERM-APP-TARGET (Managed Application)](../terminology/definitions.md#TERM-APP-TARGET) retrieves the active feature flags for its tenant to enable/disable functionality dynamically.

**Trigger**:
The [TERM-APP-TARGET (Managed Application)](../terminology/definitions.md#TERM-APP-TARGET) starts up or periodic refresh interval elapses.

**Postconditions**:

1. The [TERM-APP-TARGET (Managed Application)](../terminology/definitions.md#TERM-APP-TARGET) receives the current set of flags.

**Scenario**:

1. The [TERM-APP-TARGET (Managed Application)](../terminology/definitions.md#TERM-APP-TARGET) requests flags from the [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP).
2. The [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP) identifies the tenant (via keys or context).
3. The [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP) returns the flag configuration.

**Related Requirements**:

* [FR-FLAG-002 (Flag Delivery)](../functional-requirements/feature-flags.md#FR-FLAG-002)

<a id="UC-SYS-BILL-REPORT"></a>

## UC-SYS-BILL-REPORT Billing Event Reporting

**Actor**: [TERM-APP-TARGET (Managed Application)](../terminology/definitions.md#TERM-APP-TARGET) (System)

**Description**:
The [TERM-APP-TARGET (Managed Application)](../terminology/definitions.md#TERM-APP-TARGET) reports a billable event to the [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP) for tracking.

**Trigger**:
A user performs a billable action within the [TERM-APP-TARGET (Managed Application)](../terminology/definitions.md#TERM-APP-TARGET).

**Postconditions**:

1. The event is persisted in the [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP).

**Scenario**:

1. The [TERM-APP-TARGET (Managed Application)](../terminology/definitions.md#TERM-APP-TARGET) detects billable event.
2. The [TERM-APP-TARGET (Managed Application)](../terminology/definitions.md#TERM-APP-TARGET) sends event data to the [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP).
3. The [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP) validates and stores the event.

**Related Requirements**:

* [FR-BILL-001 (Billing Event Persistence)](../functional-requirements/billing.md#FR-BILL-001)
* [FR-BILL-002 (Billing Event Ingestion)](../functional-requirements/billing.md#FR-BILL-002)

<a id="UC-SYS-LOG-REPORT"></a>

## UC-SYS-LOG-REPORT Audit Log Reporting

**Actor**: [TERM-APP-TARGET (Managed Application)](../terminology/definitions.md#TERM-APP-TARGET) (System)

**Description**:
The [TERM-APP-TARGET (Managed Application)](../terminology/definitions.md#TERM-APP-TARGET) sends its security and operation logs to the [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP) for centralized auditing.

**Trigger**:
The [TERM-APP-TARGET (Managed Application)](../terminology/definitions.md#TERM-APP-TARGET) generates a log entry.

**Postconditions**:

1. The log entry is collected by the [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP).

**Scenario**:

1. The [TERM-APP-TARGET (Managed Application)](../terminology/definitions.md#TERM-APP-TARGET) generates a log.
2. The [TERM-APP-TARGET (Managed Application)](../terminology/definitions.md#TERM-APP-TARGET) streams/sends the log to the [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP).
3. The [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP) ingests the log.

**Related Requirements**:

* [FR-LOG-001 (Audit Log Collection)](../functional-requirements/audit.md#FR-LOG-001)

<a id="UC-SYS-BILL-EXPORT"></a>

## UC-SYS-BILL-EXPORT Billing Data Export

**Actor**: [ACT-BILLING (External Billing System)](../actors/billing-system.md#ACT-BILLING) (System)

**Description**:
The [ACT-BILLING (External Billing System)](../actors/billing-system.md#ACT-BILLING) retrieves billing events from the [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP) to generate invoices and perform reconciliation.

**Trigger**:
Scheduled job or on-demand request from the [ACT-BILLING (External Billing System)](../actors/billing-system.md#ACT-BILLING).

**Postconditions**:

1. The [ACT-BILLING (External Billing System)](../actors/billing-system.md#ACT-BILLING) receives the requested [DAT-BILL-EVENT (Billing Events)](../data-model/schema.md#DAT-BILL-EVENT).

**Scenario**:

1. The [ACT-BILLING (External Billing System)](../actors/billing-system.md#ACT-BILLING) requests billing events for a specified period/tenant.
2. The [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP) authenticates and authorizes the request.
3. The [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP) retrieves matching events from the data store.
4. The [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP) returns the event data to the [ACT-BILLING (External Billing System)](../actors/billing-system.md#ACT-BILLING).

**Related Requirements**:

* [FR-BILL-003 (Billing Data Export)](../functional-requirements/billing.md#FR-BILL-003)

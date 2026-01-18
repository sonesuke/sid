# Interface Requirements

This section defines the external interfaces provided by the system.

<a id="IF-BILL"></a>

## IF-BILL Billing Event API

**Type**: REST API
**Direction**: Bidirectional ([TERM-APP-TARGET (Managed Application)](../terminology/definitions.md#TERM-APP-TARGET) <-> [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP) / [ACT-BILLING (External Billing System)](../actors/billing-system.md#ACT-BILLING) <- [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP))
**Purpose**: To report billable operations from managed applications and to retrieve billing events for invoicing.
**Payload**: SHALL include Tenant ID, Timestamp, Event Type, and Quantity.

<a id="IF-LOG"></a>

## IF-LOG Audit Log API

**Type**: REST API
**Direction**: Input ([TERM-APP-TARGET (Managed Application)](../terminology/definitions.md#TERM-APP-TARGET) -> [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP))
**Purpose**: To report security and operational events for audit purposes.
**Payload**: SHALL include Timestamp, Actor ID, Event Type, Resource ID, Outcome, and IP Address.

<a id="IF-FLAG"></a>

## IF-FLAG Feature Flag API

**Type**: REST API
**Direction**: Output ([TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP) -> [TERM-APP-TARGET (Managed Application)](../terminology/definitions.md#TERM-APP-TARGET))
**Purpose**: To retrieve the active feature flags for a specific tenant.
**Caching**: Managed apps SHOULD cache this response to minimize latency.

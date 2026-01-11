# Interface Requirements

This section defines the external interfaces provided by the system.

<a id="API-BILL"></a>

## API-BILL Billing Event API
**Type**: REST API
**Direction**: Bidirectional ([TERM-APP-TARGET](../terminology/definitions.md#TERM-APP-TARGET) <-> [TERM-SYS-CP](../terminology/definitions.md#TERM-SYS-CP) / [ACT-BILLING](../actors/list.md#ACT-BILLING) <- [TERM-SYS-CP](../terminology/definitions.md#TERM-SYS-CP))
**Purpose**: To report billable operations from managed applications and to retrieve billing events for invoicing.
**Payload**: SHALL include Tenant ID, Timestamp, Event Type, and Quantity.

<a id="API-LOG"></a>

## API-LOG Audit Log API
**Type**: REST API
**Direction**: Input ([TERM-APP-TARGET](../terminology/definitions.md#TERM-APP-TARGET) -> [TERM-SYS-CP](../terminology/definitions.md#TERM-SYS-CP))
**Purpose**: To report security and operational events for audit purposes.
**Payload**: SHALL include Timestamp, Actor ID, Event Type, Resource ID, Outcome, and IP Address.


<a id="API-FLAG"></a>

## API-FLAG Feature Flag API
**Type**: REST API
**Direction**: Output ([TERM-SYS-CP](../terminology/definitions.md#TERM-SYS-CP) -> [TERM-APP-TARGET](../terminology/definitions.md#TERM-APP-TARGET))
**Purpose**: To retrieve the active feature flags for a specific tenant.
**Caching**: Managed apps SHOULD cache this response to minimize latency.




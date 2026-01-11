# Billing & Usage

<a id="FR-BILL-001"></a>

#### FR-BILL-001 Billing Event Persistence
The [TERM-SYS-CP](../terminology/definitions.md#TERM-SYS-CP) SHALL persistently record billable events triggers received via [FR-BILL-002](#FR-BILL-002) as [Billing Events ](../data-model/schema.md#DAT-BILL-EVENT).

**Realized by**:

*   [API-BILL](../interface-requirements/apis.md#API-BILL)

**Quality Attributes**:

*   [Encryption in Transit ](../non-functional-requirements/security.md#NFR-SEC-001)
*   [Encryption at Rest ](../non-functional-requirements/security.md#NFR-SEC-002)
*   [Data Residency ](../non-functional-requirements/data.md#NFR-DATA-001)
*   [Tenant Scalability ](../non-functional-requirements/capacity.md#NFR-CAP-001)
*   [Availability SLO ](../non-functional-requirements/availability.md#NFR-OPS-001)
*   [Backup and Redundancy ](../non-functional-requirements/availability.md#NFR-OPS-004)

**Error Conditions**:

*   [Internal Error ](../error-handling/system.md#ERR-SYS-500)
*   [Service Unavailable ](../error-handling/system.md#ERR-SYS-503)

<a id="FR-BILL-002"></a>

#### FR-BILL-002 Billing Event Ingestion
The system SHALL provide an API ([API-BILL](../interface-requirements/apis.md#API-BILL)) that allows [TERM-APP-TARGET](../terminology/definitions.md#TERM-APP-TARGET) to report billable events (corresponding to [Billing Events ](../data-model/schema.md#DAT-BILL-EVENT)).

**Realized by**:

*   [API-BILL](../interface-requirements/apis.md#API-BILL)

**Quality Attributes**:

*   [Encryption in Transit ](../non-functional-requirements/security.md#NFR-SEC-001)
*   [Key Management ](../non-functional-requirements/security.md#NFR-SEC-004)
*   [Availability SLO ](../non-functional-requirements/availability.md#NFR-OPS-001)
*   [Load Balancing and Failover ](../non-functional-requirements/availability.md#NFR-OPS-003)

**Error Conditions**:

*   [Invalid Credentials ](../error-handling/auth.md#ERR-AUTH-401)
*   [Invalid Input ](../error-handling/validation.md#ERR-VAL-400)
*   [Rate Limit Exceeded ](../error-handling/rate-limit.md#ERR-RATE-429)

<a id="FR-BILL-003"></a>

#### FR-BILL-003 Billing Data Export
The [TERM-SYS-CP](../terminology/definitions.md#TERM-SYS-CP) SHALL provide an interface for [External Billing Systems ](../actors/list.md#ACT-BILLING) to retrieve [Billing Events ](../data-model/schema.md#DAT-BILL-EVENT) for invoicing and reconciliation purposes.

**Realized by**:

*   [API-BILL](../interface-requirements/apis.md#API-BILL)

**Quality Attributes**:

*   [Encryption in Transit ](../non-functional-requirements/security.md#NFR-SEC-001)
*   [Key Management ](../non-functional-requirements/security.md#NFR-SEC-004)
*   [Least Privilege ](../non-functional-requirements/security.md#NFR-SEC-005)
*   [Data Residency ](../non-functional-requirements/data.md#NFR-DATA-001)
*   [Availability SLO ](../non-functional-requirements/availability.md#NFR-OPS-001)

**Error Conditions**:

*   [Invalid Credentials ](../error-handling/auth.md#ERR-AUTH-401)
*   [Access Denied ](../error-handling/auth.md#ERR-AUTH-403)
*   [Resource Not Found ](../error-handling/resource.md#ERR-RES-404)

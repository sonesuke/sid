# Billing & Usage

<a id="FR-BILL-001"></a>

## FR-BILL-001 Billing Event Persistence

The [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP) SHALL persistently record billable events triggers received via [FR-BILL-002 (Billing Event Ingestion)](#FR-BILL-002) as [DAT-BILL-EVENT (Billing Events)](../data-model/schema.md#DAT-BILL-EVENT).

**Realized by**:

* [API-BILL (Billing Event API)](../interface-requirements/apis.md#API-BILL)

**Quality Attributes**:

* [NFR-SEC-001 (Encryption in Transit)](../non-functional-requirements/security.md#NFR-SEC-001)
* [NFR-SEC-002 (Encryption at Rest)](../non-functional-requirements/security.md#NFR-SEC-002)
* [NFR-DATA-001 (Data Residency)](../non-functional-requirements/data.md#NFR-DATA-001)
* [NFR-CAP-001 (Tenant Scalability)](../non-functional-requirements/capacity.md#NFR-CAP-001)
* [NFR-OPS-001 (Service Level Objective)](../non-functional-requirements/availability.md#NFR-OPS-001)
* [NFR-OPS-004 (Backup and Redundancy)](../non-functional-requirements/availability.md#NFR-OPS-004)

**Error Conditions**:

* [ERR-SYS-500 (Internal Error)](../error-handling/system.md#ERR-SYS-500)
* [ERR-SYS-503 (Service Unavailable)](../error-handling/system.md#ERR-SYS-503)

<a id="FR-BILL-002"></a>

### FR-BILL-002 Billing Event Ingestion

The system SHALL provide an API ([API-BILL (Billing Event API)](../interface-requirements/apis.md#API-BILL)) that allows [TERM-APP-TARGET (Managed Application)](../terminology/definitions.md#TERM-APP-TARGET) to report billable events (corresponding to [DAT-BILL-EVENT (Billing Events)](../data-model/schema.md#DAT-BILL-EVENT)).

**Realized by**:

* [API-BILL (Billing Event API)](../interface-requirements/apis.md#API-BILL)

**Quality Attributes**:

* [NFR-SEC-001 (Encryption in Transit)](../non-functional-requirements/security.md#NFR-SEC-001)
* [NFR-SEC-004 (Key Management)](../non-functional-requirements/security.md#NFR-SEC-004)
* [NFR-OPS-001 (Service Level Objective)](../non-functional-requirements/availability.md#NFR-OPS-001)
* [NFR-OPS-003 (Load Balancing and Failover)](../non-functional-requirements/availability.md#NFR-OPS-003)

**Error Conditions**:

* [ERR-AUTH-401 (Invalid Credentials)](../error-handling/auth.md#ERR-AUTH-401)
* [ERR-VAL-400 (Invalid Input)](../error-handling/validation.md#ERR-VAL-400)
* [ERR-RATE-429 (Rate Limit Exceeded)](../error-handling/rate-limit.md#ERR-RATE-429)

<a id="FR-BILL-003"></a>

#### FR-BILL-003 Billing Data Export

The [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP) SHALL provide an interface for [ACT-BILLING (External Billing System)](../actors/list.md#ACT-BILLING) to retrieve [DAT-BILL-EVENT (Billing Events)](../data-model/schema.md#DAT-BILL-EVENT) for invoicing and reconciliation purposes.

**Realized by**:

* [API-BILL (Billing Event API)](../interface-requirements/apis.md#API-BILL)

**Quality Attributes**:

* [NFR-SEC-001 (Encryption in Transit)](../non-functional-requirements/security.md#NFR-SEC-001)
* [NFR-SEC-004 (Key Management)](../non-functional-requirements/security.md#NFR-SEC-004)
* [NFR-SEC-005 (Least Privilege)](../non-functional-requirements/security.md#NFR-SEC-005)
* [NFR-DATA-001 (Data Residency)](../non-functional-requirements/data.md#NFR-DATA-001)
* [NFR-OPS-001 (Service Level Objective)](../non-functional-requirements/availability.md#NFR-OPS-001)

**Error Conditions**:

* [ERR-AUTH-401 (Invalid Credentials)](../error-handling/auth.md#ERR-AUTH-401)
* [ERR-AUTH-403 (Access Denied)](../error-handling/auth.md#ERR-AUTH-403)
* [ERR-RES-404 (Resource Not Found)](../error-handling/resource.md#ERR-RES-404)

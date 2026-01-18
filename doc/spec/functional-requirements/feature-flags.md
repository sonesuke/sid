# Feature Flag Management

<a id="FR-FLAG-001"></a>

## FR-FLAG-001 Flag Configuration

The [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP) SHALL allow [ACT-OPS (Platform Operator)](../actors/platform-operator.md#ACT-OPS) to configure [DAT-FLAG (Feature Flags)](../data-model/schema.md#DAT-FLAG) for each [DAT-TENANT (Tenants)](../data-model/schema.md#DAT-TENANT).

**Realized by**:

* [IF-OPS-CONSOLE (Operator Console)](../interface-requirements/ui.md#IF-OPS-CONSOLE)

**Quality Attributes**:

* [NFR-SEC-001 (Encryption in Transit)](../non-functional-requirements/security.md#NFR-SEC-001)
* [NFR-SEC-005 (Least Privilege)](../non-functional-requirements/security.md#NFR-SEC-005)
* [NFR-CAP-001 (Tenant Scalability)](../non-functional-requirements/capacity.md#NFR-CAP-001)
* [NFR-OPS-001 (Service Level Objective)](../non-functional-requirements/availability.md#NFR-OPS-001)

**Error Conditions**:

* [ERR-AUTH-403 (Access Denied)](../error-handling/auth.md#ERR-AUTH-403)
* [ERR-RES-404 (Resource Not Found)](../error-handling/resource.md#ERR-RES-404)

<a id="FR-FLAG-002"></a>

### FR-FLAG-002 Flag Delivery

The system SHALL provide an interface via [IF-FLAG (Feature Flag API)](../interface-requirements/apis.md#IF-FLAG) for [TERM-APP-TARGET (Managed Application)](../terminology/definitions.md#TERM-APP-TARGET) to retrieve the current state of [DAT-FLAG (Feature Flags)](../data-model/schema.md#DAT-FLAG).

**Realized by**:

* [IF-FLAG (Feature Flag API)](../interface-requirements/apis.md#IF-FLAG)

**Quality Attributes**:

* [NFR-SEC-001 (Encryption in Transit)](../non-functional-requirements/security.md#NFR-SEC-001)
* [NFR-SEC-004 (Key Management)](../non-functional-requirements/security.md#NFR-SEC-004)
* [NFR-OPS-001 (Service Level Objective)](../non-functional-requirements/availability.md#NFR-OPS-001)
* [NFR-OPS-003 (Load Balancing and Failover)](../non-functional-requirements/availability.md#NFR-OPS-003)

**Error Conditions**:

* [ERR-AUTH-401 (Invalid Credentials)](../error-handling/auth.md#ERR-AUTH-401)
* [ERR-RATE-429 (Rate Limit Exceeded)](../error-handling/rate-limit.md#ERR-RATE-429)

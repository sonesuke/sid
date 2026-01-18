# System Operations

<a id="FR-SYS-001"></a>

## FR-SYS-001 Application Registration

The [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP) SHALL allow [ACT-DEV (Developer)](../actors/developer.md#ACT-DEV) to register a new [DAT-APP (Managed Applications)](../data-model/schema.md#DAT-APP).
The system SHALL generate a unique Application ID upon registration.

**Quality Attributes**:

* [NFR-SEC-001 (Encryption in Transit)](../non-functional-requirements/security.md#NFR-SEC-001)
* [NFR-SEC-004 (Key Management)](../non-functional-requirements/security.md#NFR-SEC-004)
* [NFR-SEC-005 (Least Privilege)](../non-functional-requirements/security.md#NFR-SEC-005)
* [NFR-OPS-001 (Service Level Objective)](../non-functional-requirements/availability.md#NFR-OPS-001)

**Error Conditions**:

* [ERR-AUTH-403 (Access Denied)](../error-handling/auth.md#ERR-AUTH-403)
* [ERR-VAL-400 (Invalid Input)](../error-handling/validation.md#ERR-VAL-400)
* [ERR-VAL-409 (Conflict)](../error-handling/validation.md#ERR-VAL-409)

<a id="FR-SYS-002"></a>

### FR-SYS-002 API Key Management

The [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP) SHALL allow [ACT-DEV (Developer)](../actors/developer.md#ACT-DEV) to issue [DAT-KEY (API Access Keys)](../data-model/schema.md#DAT-KEY) for a registered [DAT-APP (Managed Applications)](../data-model/schema.md#DAT-APP).
The system SHALL display the Client Secret only once upon issuance.
The system SHALL allow [ACT-DEV (Developer)](../actors/developer.md#ACT-DEV) to revoke existing keys.

**Quality Attributes**:

* [NFR-SEC-001 (Encryption in Transit)](../non-functional-requirements/security.md#NFR-SEC-001)
* [NFR-SEC-002 (Encryption at Rest)](../non-functional-requirements/security.md#NFR-SEC-002)
* [NFR-SEC-004 (Key Management)](../non-functional-requirements/security.md#NFR-SEC-004)
* [NFR-SEC-005 (Least Privilege)](../non-functional-requirements/security.md#NFR-SEC-005)
* [NFR-OPS-001 (Service Level Objective)](../non-functional-requirements/availability.md#NFR-OPS-001)

**Error Conditions**:

* [ERR-AUTH-403 (Access Denied)](../error-handling/auth.md#ERR-AUTH-403)
* [ERR-RES-404 (Resource Not Found)](../error-handling/resource.md#ERR-RES-404)

<a id="FR-SYS-003"></a>

#### FR-SYS-003 Application Lifecycle Management

The [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP) SHALL allow [ACT-DEV (Developer)](../actors/developer.md#ACT-DEV) to update the configuration of a [DAT-APP (Managed Applications)](../data-model/schema.md#DAT-APP).
The [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP) SHALL allow [ACT-DEV (Developer)](../actors/developer.md#ACT-DEV) to change the [DAT-APP (Managed Applications)](../data-model/schema.md#DAT-APP) (e.g., Disable) to block access.

**Quality Attributes**:

* [NFR-SEC-001 (Encryption in Transit)](../non-functional-requirements/security.md#NFR-SEC-001)
* [NFR-SEC-005 (Least Privilege)](../non-functional-requirements/security.md#NFR-SEC-005)
* [NFR-OPS-001 (Service Level Objective)](../non-functional-requirements/availability.md#NFR-OPS-001)

**Error Conditions**:

* [ERR-AUTH-403 (Access Denied)](../error-handling/auth.md#ERR-AUTH-403)
* [ERR-RES-404 (Resource Not Found)](../error-handling/resource.md#ERR-RES-404)

<a id="FR-SYS-004"></a>

#### FR-SYS-004 Operator JIT Provisioning

The [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP) SHALL automatically provision a [DAT-USER (Users)](../data-model/schema.md#DAT-USER) record for [ACT-OPS (Platform Operator)](../actors/platform-operator.md#ACT-OPS) upon their first successful authentication via the external Identity Provider.

* The provisioned user SHALL have ``tenant_id`` set to NULL (platform-level user).
* The user's ``id`` SHALL be used as ``actor_id`` in [DAT-LOG (Audit Logs)](../data-model/schema.md#DAT-LOG).
* Subsequent logins SHALL reuse the existing user record.

**Quality Attributes**:

* [NFR-SEC-001 (Encryption in Transit)](../non-functional-requirements/security.md#NFR-SEC-001)
* [NFR-SEC-005 (Least Privilege)](../non-functional-requirements/security.md#NFR-SEC-005)
* [NFR-OPS-001 (Service Level Objective)](../non-functional-requirements/availability.md#NFR-OPS-001)
* [NFR-MON-001 (Continuous Monitoring)](../non-functional-requirements/monitoring.md#NFR-MON-001)

**Error Conditions**:

* [ERR-AUTH-401 (Invalid Credentials)](../error-handling/auth.md#ERR-AUTH-401)
* [ERR-SYS-500 (Internal Error)](../error-handling/system.md#ERR-SYS-500)

<a id="FR-SYS-005"></a>

#### FR-SYS-005 System Health Monitoring

The [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP) SHALL provide a Dashboard or API for [ACT-OPS (Platform Operator)](../actors/platform-operator.md#ACT-OPS) to view the real-time health status of system components.

* Status SHALL include connectivity to downstream dependencies (DB, Identity Provider, Event Bus).
* Status SHALL include Error Rates and P99 Latency of key services.

**Quality Attributes**:

* [NFR-MON-001 (Continuous Monitoring)](../non-functional-requirements/monitoring.md#NFR-MON-001)
* [NFR-MON-002 (System Health Alerting)](../non-functional-requirements/monitoring.md#NFR-MON-002)
* [NFR-MON-003 (Synthetic Monitoring)](../non-functional-requirements/monitoring.md#NFR-MON-003)

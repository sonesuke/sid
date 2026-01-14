# System Operations

<a id="FR-SYS-001"></a>

## FR-SYS-001 Application Registration

The [TERM-SYS-CP](../terminology/definitions.md#TERM-SYS-CP) SHALL allow [ACT-DEV](../actors/list.md#ACT-DEV) to register a new [Managed Application](../data-model/schema.md#DAT-APP).
The system SHALL generate a unique Application ID upon registration.

**Quality Attributes**:

* [Encryption in Transit](../non-functional-requirements/security.md#NFR-SEC-001)
* [Key Management](../non-functional-requirements/security.md#NFR-SEC-004)
* [Least Privilege](../non-functional-requirements/security.md#NFR-SEC-005)
* [Availability SLO](../non-functional-requirements/availability.md#NFR-OPS-001)

**Error Conditions**:

* [Access Denied](../error-handling/auth.md#ERR-AUTH-403)
* [Invalid Input](../error-handling/validation.md#ERR-VAL-400)
* [Conflict](../error-handling/validation.md#ERR-VAL-409)

<a id="FR-SYS-002"></a>

### FR-SYS-002 API Key Management

The [TERM-SYS-CP](../terminology/definitions.md#TERM-SYS-CP) SHALL allow [ACT-DEV](../actors/list.md#ACT-DEV) to issue [API Access Keys](../data-model/schema.md#DAT-KEY) for a registered [Managed Application](../data-model/schema.md#DAT-APP).
The system SHALL display the Client Secret only once upon issuance.
The system SHALL allow [ACT-DEV](../actors/list.md#ACT-DEV) to revoke existing keys.

**Quality Attributes**:

* [Encryption in Transit](../non-functional-requirements/security.md#NFR-SEC-001)
* [Encryption at Rest](../non-functional-requirements/security.md#NFR-SEC-002)
* [Key Management](../non-functional-requirements/security.md#NFR-SEC-004)
* [Least Privilege](../non-functional-requirements/security.md#NFR-SEC-005)
* [Availability SLO](../non-functional-requirements/availability.md#NFR-OPS-001)

**Error Conditions**:

* [Access Denied](../error-handling/auth.md#ERR-AUTH-403)
* [Resource Not Found](../error-handling/resource.md#ERR-RES-404)

<a id="FR-SYS-003"></a>

#### FR-SYS-003 Application Lifecycle Management

The [TERM-SYS-CP](../terminology/definitions.md#TERM-SYS-CP) SHALL allow [ACT-DEV](../actors/list.md#ACT-DEV) to update the configuration of a [Managed Application](../data-model/schema.md#DAT-APP).
The [TERM-SYS-CP](../terminology/definitions.md#TERM-SYS-CP) SHALL allow [ACT-DEV](../actors/list.md#ACT-DEV) to change the [Status](../data-model/schema.md#DAT-APP) (e.g., Disable) to block access.

**Quality Attributes**:

* [Encryption in Transit](../non-functional-requirements/security.md#NFR-SEC-001)
* [Least Privilege](../non-functional-requirements/security.md#NFR-SEC-005)
* [Availability SLO](../non-functional-requirements/availability.md#NFR-OPS-001)

**Error Conditions**:

* [Access Denied](../error-handling/auth.md#ERR-AUTH-403)
* [Resource Not Found](../error-handling/resource.md#ERR-RES-404)

<a id="FR-SYS-004"></a>

#### FR-SYS-004 Operator JIT Provisioning

The [TERM-SYS-CP](../terminology/definitions.md#TERM-SYS-CP) SHALL automatically provision a [User](../data-model/schema.md#DAT-USER) record for [Platform Operators](../actors/list.md#ACT-OPS) upon their first successful authentication via the external Identity Provider.

* The provisioned user SHALL have ``tenant_id`` set to NULL (platform-level user).
* The user's ``id`` SHALL be used as ``actor_id`` in [Audit Logs](../data-model/schema.md#DAT-LOG).
* Subsequent logins SHALL reuse the existing user record.

**Quality Attributes**:

* [Encryption in Transit](../non-functional-requirements/security.md#NFR-SEC-001)
* [Least Privilege](../non-functional-requirements/security.md#NFR-SEC-005)
* [Availability SLO](../non-functional-requirements/availability.md#NFR-OPS-001)
* [Continuous Monitoring](../non-functional-requirements/monitoring.md#NFR-MON-001)

**Error Conditions**:

* [Invalid Credentials](../error-handling/auth.md#ERR-AUTH-401)
* [Internal Error](../error-handling/system.md#ERR-SYS-500)

<a id="FR-SYS-005"></a>

#### FR-SYS-005 System Health Monitoring

The [TERM-SYS-CP](../terminology/definitions.md#TERM-SYS-CP) SHALL provide a Dashboard or API for [Platform Operators](../actors/list.md#ACT-OPS) to view the real-time health status of system components.

* Status SHALL include connectivity to downstream dependencies (DB, Identity Provider, Event Bus).
* Status SHALL include Error Rates and P99 Latency of key services.

**Quality Attributes**:

* [Continuous Monitoring](../non-functional-requirements/monitoring.md#NFR-MON-001)
* [System Health Alerting](../non-functional-requirements/monitoring.md#NFR-MON-002)

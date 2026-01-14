# Audit & Logging

<a id="FR-LOG-001"></a>

## FR-LOG-001 Audit Log Collection

The [TERM-SYS-CP](../terminology/definitions.md#TERM-SYS-CP) SHALL collect security and operational logs from all components via [API-LOG](../interface-requirements/apis.md#API-LOG) and persist them as [Audit Logs](../data-model/schema.md#DAT-LOG).

**Realized by**:

* [API-LOG](../interface-requirements/apis.md#API-LOG)

**Quality Attributes**:

* [Encryption in Transit](../non-functional-requirements/security.md#NFR-SEC-001)
* [Encryption at Rest](../non-functional-requirements/security.md#NFR-SEC-002)
* [Data Residency](../non-functional-requirements/data.md#NFR-DATA-001)
* [Availability SLO](../non-functional-requirements/availability.md#NFR-OPS-001)
* [Backup and Redundancy](../non-functional-requirements/availability.md#NFR-OPS-004)
* [Continuous Monitoring](../non-functional-requirements/monitoring.md#NFR-MON-001)

**Error Conditions**:

* [Internal Error](../error-handling/system.md#ERR-SYS-500)
* [Service Unavailable](../error-handling/system.md#ERR-SYS-503)

<a id="FR-LOG-002"></a>

### FR-LOG-002 Audit Log Export

The [TERM-SYS-CP](../terminology/definitions.md#TERM-SYS-CP) SHALL allow [ACT-AUDIT](../actors/list.md#ACT-AUDIT) to export [Audit Logs](../data-model/schema.md#DAT-LOG) in CSV format.

**Realized by**:

* [Auditor Console](../interface-requirements/ui.md#IF-AUDIT-CONSOLE)

**Quality Attributes**:

* [Encryption in Transit](../non-functional-requirements/security.md#NFR-SEC-001)
* [Least Privilege](../non-functional-requirements/security.md#NFR-SEC-005)
* [Data Residency](../non-functional-requirements/data.md#NFR-DATA-001)
* [Availability SLO](../non-functional-requirements/availability.md#NFR-OPS-001)

**Error Conditions**:

* [Access Denied](../error-handling/auth.md#ERR-AUTH-403)
* [Internal Error](../error-handling/system.md#ERR-SYS-500)

<a id="FR-LOG-003"></a>

#### FR-LOG-003 Control Plane Auditing

The [TERM-SYS-CP](../terminology/definitions.md#TERM-SYS-CP) SHALL record its own state-changing operations (e.g., Tenant Provisioning, User Management) as [Audit Logs](../data-model/schema.md#DAT-LOG).

**Quality Attributes**:

* [Encryption at Rest](../non-functional-requirements/security.md#NFR-SEC-002)
* [Data Residency](../non-functional-requirements/data.md#NFR-DATA-001)
* [Availability SLO](../non-functional-requirements/availability.md#NFR-OPS-001)
* [Continuous Monitoring](../non-functional-requirements/monitoring.md#NFR-MON-001)

**Error Conditions**:

* [Internal Error](../error-handling/system.md#ERR-SYS-500)

# Audit & Logging

<a id="FR-LOG-001"></a>

## FR-LOG-001 Audit Log Collection

The [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP) SHALL collect security and operational logs from all components via [IF-LOG (Audit Log API)](../interface-requirements/apis.md#IF-LOG) and persist them as [DAT-LOG (Audit Logs)](../data-model/schema.md#DAT-LOG).

**Realized by**:

* [IF-LOG (Audit Log API)](../interface-requirements/apis.md#IF-LOG)

**Quality Attributes**:

* [NFR-SEC-001 (Encryption in Transit)](../non-functional-requirements/security.md#NFR-SEC-001)
* [NFR-SEC-002 (Encryption at Rest)](../non-functional-requirements/security.md#NFR-SEC-002)
* [NFR-DATA-001 (Data Residency)](../non-functional-requirements/data.md#NFR-DATA-001)
* [NFR-OPS-001 (Service Level Objective)](../non-functional-requirements/availability.md#NFR-OPS-001)
* [NFR-OPS-004 (Backup and Redundancy)](../non-functional-requirements/availability.md#NFR-OPS-004)
* [NFR-MON-001 (Continuous Monitoring)](../non-functional-requirements/monitoring.md#NFR-MON-001)

**Error Conditions**:

* [ERR-SYS-500 (Internal Error)](../error-handling/system.md#ERR-SYS-500)
* [ERR-SYS-503 (Service Unavailable)](../error-handling/system.md#ERR-SYS-503)

<a id="FR-LOG-002"></a>

### FR-LOG-002 Audit Log Export

The [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP) SHALL allow [ACT-AUDIT (Auditor)](../actors/list.md#ACT-AUDIT) to export [DAT-LOG (Audit Logs)](../data-model/schema.md#DAT-LOG) in CSV format.

**Realized by**:

* [IF-AUDIT-CONSOLE (Auditor Console)](../interface-requirements/ui.md#IF-AUDIT-CONSOLE)

**Quality Attributes**:

* [NFR-SEC-001 (Encryption in Transit)](../non-functional-requirements/security.md#NFR-SEC-001)
* [NFR-SEC-005 (Least Privilege)](../non-functional-requirements/security.md#NFR-SEC-005)
* [NFR-DATA-001 (Data Residency)](../non-functional-requirements/data.md#NFR-DATA-001)
* [NFR-OPS-001 (Service Level Objective)](../non-functional-requirements/availability.md#NFR-OPS-001)

**Error Conditions**:

* [ERR-AUTH-403 (Access Denied)](../error-handling/auth.md#ERR-AUTH-403)
* [ERR-SYS-500 (Internal Error)](../error-handling/system.md#ERR-SYS-500)

<a id="FR-LOG-003"></a>

#### FR-LOG-003 Control Plane Auditing

The [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP) SHALL record its own state-changing operations (e.g., Tenant Provisioning, User Management) as [DAT-LOG (Audit Logs)](../data-model/schema.md#DAT-LOG).

**Quality Attributes**:

* [NFR-SEC-002 (Encryption at Rest)](../non-functional-requirements/security.md#NFR-SEC-002)
* [NFR-DATA-001 (Data Residency)](../non-functional-requirements/data.md#NFR-DATA-001)
* [NFR-OPS-001 (Service Level Objective)](../non-functional-requirements/availability.md#NFR-OPS-001)
* [NFR-MON-001 (Continuous Monitoring)](../non-functional-requirements/monitoring.md#NFR-MON-001)

**Error Conditions**:

* [ERR-SYS-500 (Internal Error)](../error-handling/system.md#ERR-SYS-500)

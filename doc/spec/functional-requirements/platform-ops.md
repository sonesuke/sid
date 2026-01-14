# Platform Operations

<a id="FR-OPS-001"></a>

## FR-OPS-001 Tenant Status Management

The [TERM-SYS-CP](../terminology/definitions.md#TERM-SYS-CP) SHALL allow [ACT-OPS](../actors/list.md#ACT-OPS) to modify the status of a [Tenant](../data-model/schema.md#DAT-TENANT) (e.g., Active, Suspended).
When a [Tenant](../data-model/schema.md#DAT-TENANT) is Suspended, the system SHALL revoke access for all [Users](../data-model/schema.md#DAT-USER) associated with that tenant.

**Realized by**:

* [Operator Console](../interface-requirements/ui.md#IF-OPS-CONSOLE)

**Quality Attributes**:

* [Encryption in Transit](../non-functional-requirements/security.md#NFR-SEC-001)
* [Least Privilege](../non-functional-requirements/security.md#NFR-SEC-005)
* [Tenant Scalability](../non-functional-requirements/capacity.md#NFR-CAP-001)
* [Availability SLO](../non-functional-requirements/availability.md#NFR-OPS-001)

**Error Conditions**:

* [Access Denied](../error-handling/auth.md#ERR-AUTH-403)
* [Resource Not Found](../error-handling/resource.md#ERR-RES-404)

<a id="FR-OPS-002"></a>

### FR-OPS-002 Tenant Deletion

The [TERM-SYS-CP](../terminology/definitions.md#TERM-SYS-CP) SHALL allow [ACT-OPS](../actors/list.md#ACT-OPS) to permanently delete a [Tenant](../data-model/schema.md#DAT-TENANT) and all associated data upon contract termination or deletion request.

* Upon deletion request, the tenant SHALL enter a 30-day grace period (recoverable).
* After the grace period, all tenant data SHALL be permanently and irrecoverably deleted.
* Deleted data includes: [Users](../data-model/schema.md#DAT-USER), [Sessions](../data-model/schema.md#DAT-SESSION), [Audit Logs](../data-model/schema.md#DAT-LOG), [Billing Events](../data-model/schema.md#DAT-BILL-EVENT), and configuration.

**Constrained by**: [CON-COMP-001](../constraints-and-assumptions/index.md#CON-COMP-001)

**Realized by**:

* [Operator Console](../interface-requirements/ui.md#IF-OPS-CONSOLE)

**Quality Attributes**:

* [Encryption in Transit](../non-functional-requirements/security.md#NFR-SEC-001)
* [Least Privilege](../non-functional-requirements/security.md#NFR-SEC-005)
* [Availability SLO](../non-functional-requirements/availability.md#NFR-OPS-001)

**Error Conditions**:

* [Access Denied](../error-handling/auth.md#ERR-AUTH-403)
* [Resource Not Found](../error-handling/resource.md#ERR-RES-404)
* [Resource Gone](../error-handling/resource.md#ERR-RES-410)

<a id="FR-OPS-003"></a>

#### FR-OPS-003 Data Retention Enforcement

The [TERM-SYS-CP](../terminology/definitions.md#TERM-SYS-CP) SHALL automatically enforce data retention policies:

* [Audit Logs](../data-model/schema.md#DAT-LOG) SHALL be retained for a minimum of 7 years, then securely deleted.
* [Billing Events](../data-model/schema.md#DAT-BILL-EVENT) SHALL be retained for a minimum of 5 years, then securely deleted.

**Constrained by**: [CON-DATA-002](../constraints-and-assumptions/index.md#CON-DATA-002), [CON-DATA-003](../constraints-and-assumptions/index.md#CON-DATA-003)

**Realized by**:

* [TERM-SYS-CP](../terminology/definitions.md#TERM-SYS-CP) (automated process)

**Quality Attributes**:

* [Encryption at Rest](../non-functional-requirements/security.md#NFR-SEC-002)
* [Data Residency](../non-functional-requirements/data.md#NFR-DATA-001)
* [Availability SLO](../non-functional-requirements/availability.md#NFR-OPS-001)

**Error Conditions**:

* [Internal Error](../error-handling/system.md#ERR-SYS-500)

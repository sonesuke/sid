# Platform Operations

<a id="FR-OPS-001"></a>

## FR-OPS-001 Tenant Status Management

The [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP) SHALL allow [ACT-OPS (Platform Operator)](../actors/platform-operator.md#ACT-OPS) to modify the status of a [DAT-TENANT (Tenants)](../data-model/schema.md#DAT-TENANT) (e.g., Active, Suspended).
When a [DAT-TENANT (Tenants)](../data-model/schema.md#DAT-TENANT) is Suspended, the system SHALL revoke access for all [DAT-USER (Users)](../data-model/schema.md#DAT-USER) associated with that tenant.

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

<a id="FR-OPS-002"></a>

### FR-OPS-002 Tenant Deletion

The [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP) SHALL allow [ACT-OPS (Platform Operator)](../actors/platform-operator.md#ACT-OPS) to permanently delete a [DAT-TENANT (Tenants)](../data-model/schema.md#DAT-TENANT) and all associated data upon contract termination or deletion request.

* Upon deletion request, the tenant SHALL enter a 30-day grace period (recoverable).
* After the grace period, all tenant data SHALL be permanently and irrecoverably deleted.
* Deleted data includes: [DAT-USER (Users)](../data-model/schema.md#DAT-USER), [DAT-SESSION (User Sessions)](../data-model/schema.md#DAT-SESSION), [DAT-LOG (Audit Logs)](../data-model/schema.md#DAT-LOG), [DAT-BILL-EVENT (Billing Events)](../data-model/schema.md#DAT-BILL-EVENT), and configuration.

**Constrained by**: [CON-COMP-001 (Data Subject Rights)](../constraints-and-assumptions/index.md#CON-COMP-001)

**Realized by**:

* [IF-OPS-CONSOLE (Operator Console)](../interface-requirements/ui.md#IF-OPS-CONSOLE)

**Quality Attributes**:

* [NFR-SEC-001 (Encryption in Transit)](../non-functional-requirements/security.md#NFR-SEC-001)
* [NFR-SEC-005 (Least Privilege)](../non-functional-requirements/security.md#NFR-SEC-005)
* [NFR-OPS-001 (Service Level Objective)](../non-functional-requirements/availability.md#NFR-OPS-001)

**Error Conditions**:

* [ERR-AUTH-403 (Access Denied)](../error-handling/auth.md#ERR-AUTH-403)
* [ERR-RES-404 (Resource Not Found)](../error-handling/resource.md#ERR-RES-404)
* [ERR-RES-410 (Resource Gone)](../error-handling/resource.md#ERR-RES-410)

<a id="FR-OPS-003"></a>

#### FR-OPS-003 Data Retention Enforcement

The [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP) SHALL automatically enforce data retention policies:

* [DAT-LOG (Audit Logs)](../data-model/schema.md#DAT-LOG) SHALL be retained for a minimum of 7 years, then securely deleted.
* [DAT-BILL-EVENT (Billing Events)](../data-model/schema.md#DAT-BILL-EVENT) SHALL be retained for a minimum of 5 years, then securely deleted.

**Constrained by**: [CON-DATA-002 (Audit Log Retention)](../constraints-and-assumptions/index.md#CON-DATA-002), [CON-DATA-003 (Billing Data Retention)](../constraints-and-assumptions/index.md#CON-DATA-003)

**Realized by**:

* [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP) (automated process)

**Quality Attributes**:

* [NFR-SEC-002 (Encryption at Rest)](../non-functional-requirements/security.md#NFR-SEC-002)
* [NFR-DATA-001 (Data Residency)](../non-functional-requirements/data.md#NFR-DATA-001)
* [NFR-OPS-001 (Service Level Objective)](../non-functional-requirements/availability.md#NFR-OPS-001)

**Error Conditions**:

* [ERR-SYS-500 (Internal Error)](../error-handling/system.md#ERR-SYS-500)

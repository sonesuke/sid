# Audit Management

<a id="UC-AUDIT-EXPORT"></a>

## UC-AUDIT-EXPORT Audit Log Export

**Actor**: [ACT-AUDIT (Auditor)](../actors/auditor.md#ACT-AUDIT)

**Description**:
The [ACT-AUDIT (Auditor)](../actors/auditor.md#ACT-AUDIT) exports system audit logs for compliance review.

**Trigger**:
The [ACT-AUDIT (Auditor)](../actors/auditor.md#ACT-AUDIT) selects "Export Logs" within the **Auditor Console**.

**Preconditions**:

1. The [ACT-AUDIT (Auditor)](../actors/auditor.md#ACT-AUDIT) is logged in with Auditor privileges.

**Postconditions**:

1. A CSV file containing the requested logs is downloaded to the [ACT-AUDIT (Auditor)](../actors/auditor.md#ACT-AUDIT)'s device.

**Scenario**:

1. The [ACT-AUDIT (Auditor)](../actors/auditor.md#ACT-AUDIT) navigates to the "Audit Logs" view in the **Auditor Console**.
2. The [ACT-AUDIT (Auditor)](../actors/auditor.md#ACT-AUDIT) selects the date range and filters for the export.
3. The [ACT-AUDIT (Auditor)](../actors/auditor.md#ACT-AUDIT) initiates the download.
4. The [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP) queries the log storage.
5. The [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP) formats the data as CSV and streams the response.

**Related Requirements**:

* [FR-LOG-001 (Audit Log Collection)](../functional-requirements/audit.md#FR-LOG-001)
* [FR-LOG-002 (Audit Log Export)](../functional-requirements/audit.md#FR-LOG-002)

<a id="UC-AUDIT-RECORD-CP"></a>

## UC-AUDIT-RECORD-CP Control Plane Event Recording

**Actor**: [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP)

**Description**:
The [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP) records internal state changes (e.g., provisioning, user management) as audit logs to ensure traceability of operator and admin actions.

**Trigger**:
A state-changing operation is successfully completed by any Actor.

**Preconditions**:

1. The operation (e.g., Tenant Provisioning, User Deletion) has succeeded.

**Postconditions**:

1. An audit log entry describing the event is persisted.

**Scenario**:

1. An Actor (Operator, Tenant Owner) performs an action (e.g., "Provision Tenant").
2. The [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP) executes the detailed business logic.
3. The [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP) generates an audit log event containing Actor ID, Action, Resource, and Timestamp.
4. The [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP) persists the log entry.

**Related Requirements**:

* [FR-LOG-003 (Control Plane Auditing)](../functional-requirements/audit.md#FR-LOG-003)

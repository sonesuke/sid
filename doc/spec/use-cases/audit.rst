Audit Management
================

.. _UC-AUDIT-EXPORT:

UC-AUDIT-EXPORT Audit Log Export
--------------------------------
**Actor**: :ref:`Auditor <ACT-AUDIT>`

**Description**:
The :ref:`Auditor <ACT-AUDIT>` exports system audit logs for compliance review.

**Trigger**:
The :ref:`Auditor <ACT-AUDIT>` selects "Export Logs" within the **Auditor Console**.

**Preconditions**:

1. The :ref:`Auditor <ACT-AUDIT>` is logged in with Auditor privileges.

**Postconditions**:

1. A CSV file containing the requested logs is downloaded to the :ref:`Auditor <ACT-AUDIT>`'s device.

**Scenario**:

1. The :ref:`Auditor <ACT-AUDIT>` navigates to the "Audit Logs" view in the **Auditor Console**.
2. The :ref:`Auditor <ACT-AUDIT>` selects the date range and filters for the export.
3. The :ref:`Auditor <ACT-AUDIT>` initiates the download.
3. The :ref:`Control Plane <TERM-SYS-CP>` queries the log storage.
4. The :ref:`Control Plane <TERM-SYS-CP>` formats the data as CSV and streams the response.

**Related Requirements**:

*   :ref:`Audit Log Collection <FR-LOG-001>`
*   :ref:`Audit Log Export <FR-LOG-002>`

.. _UC-AUDIT-RECORD-CP:

UC-AUDIT-RECORD-CP Control Plane Event Recording
------------------------------------------------
**Actor**: :ref:`Control Plane <TERM-SYS-CP>`

**Description**:
The :ref:`Control Plane <TERM-SYS-CP>` records internal state changes (e.g., provisioning, user management) as audit logs to ensure traceability of operator and admin actions.

**Trigger**:
A state-changing operation is successfully completed by any Actor.

**Preconditions**:

1. The operation (e.g., Tenant Provisioning, User Deletion) has succeeded.

**Postconditions**:

1. An audit log entry describing the event is persisted.

**Scenario**:

1. An Actor (Operator, Tenant Owner) performs an action (e.g., "Provision Tenant").
2. The :ref:`Control Plane <TERM-SYS-CP>` executes the detailed business logic.
3. The :ref:`Control Plane <TERM-SYS-CP>` generates an audit log event containing Actor ID, Action, Resource, and Timestamp.
4. The :ref:`Control Plane <TERM-SYS-CP>` persists the log entry.

**Related Requirements**:

*   :ref:`Control Plane Auditing <FR-LOG-003>`


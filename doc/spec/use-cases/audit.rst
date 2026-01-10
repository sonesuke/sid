Audit Management
================

.. _UC-AUDIT-EXPORT:

UC-AUDIT-EXPORT Audit Log Export
--------------------------------
**Actor**: :ref:`ACT-AUDIT`

**Description**:
The :ref:`Auditor <ACT-AUDIT>` exports system audit logs for compliance review.

**Trigger**:
The :ref:`Auditor <ACT-AUDIT>` selects "Export Logs" within the :ref:`IF-AUDIT-CONSOLE`.

**Preconditions**:
1. The :ref:`Auditor <ACT-AUDIT>` is logged in with Auditor privileges.

**Postconditions**:
1. A CSV file containing the requested logs is downloaded to the :ref:`Auditor <ACT-AUDIT>`'s device.

**Scenario**:
1. The :ref:`Auditor <ACT-AUDIT>` navigates to the "Audit Logs" view in the :ref:`IF-AUDIT-CONSOLE`.
2. The :ref:`Auditor <ACT-AUDIT>` selects the date range and filters for the export.
3. The :ref:`Auditor <ACT-AUDIT>` initiates the download.
3. The :ref:`Control Plane <TERM-SYS-CP>` queries the log storage.
4. The :ref:`Control Plane <TERM-SYS-CP>` formats the data as CSV and streams the response.

**Related Requirements**:
*   :ref:`FR-LOG-001` (Collection)
*   :ref:`FR-LOG-002` (Export)

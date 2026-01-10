Audit Management
================

.. _UC-AUDIT-EXPORT:

UC-AUDIT-EXPORT Audit Log Export
--------------------------------
**Actor**: :ref:`ACT-AUDIT`

**Description**:
An Auditor exports system audit logs for compliance review.

**Trigger**:
Auditor selects "Export Logs".

**Preconditions**:
1. Actor is logged in with Auditor privileges.

**Postconditions**:
1. A CSV file containing the requested logs is downloaded to the actor's device.

**Scenario**:
1. Auditor selects the date range and filters for the export.
2. Auditor initiates the download.
3. System queries the log storage.
4. System formats the data as CSV and streams the response.

**Related Requirements**:
*   :ref:`FR-LOG-001` (Collection)
*   :ref:`FR-LOG-002` (Export)

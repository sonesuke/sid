System Integration
==================

This section describes the automated interactions between Managed Applications and the Control Plane.

.. _UC-SYS-APP-AUTH:

UC-SYS-APP-AUTH Feature Flag Retrieval
--------------------------------------
**Actor**: :ref:`TERM-APP-TARGET` (System)

**Description**:
A Managed Application retrieves the active feature flags for its tenant to enable/disable functionality dynamically.

**Trigger**:
Application starts up or periodic refresh interval elapses.

**Postconditions**:
1. Application receives the current set of flags.

**Scenario**:
1. Application requests flags from Control Plane (API).
2. Control Plane identifies the tenant (via keys or context).
3. Control Plane returns the flag configuration.

**Related Requirements**:
*   :ref:`FR-FLAG-002`

.. _UC-SYS-BILL-REPORT:

UC-SYS-BILL-REPORT Billing Event Reporting
------------------------------------------
**Actor**: :ref:`TERM-APP-TARGET` (System)

**Description**:
A Managed Application reports a billable event to the Control Plane for tracking.

**Trigger**:
A user performs a billable action within the application.

**Postconditions**:
1. The event is persisted in the Control Plane.

**Scenario**:
1. Application detects billable event.
2. Application sends event data to Control Plane API.
3. Control Plane validates and stores the event.

**Related Requirements**:
*   :ref:`FR-BILL-001`
*   :ref:`FR-BILL-002`

.. _UC-SYS-LOG-REPORT:

UC-SYS-LOG-REPORT Audit Log Reporting
-------------------------------------
**Actor**: :ref:`TERM-APP-TARGET` (System)

**Description**:
A Managed Application sends its security and operation logs to the Control Plane for centralized auditing.

**Trigger**:
Application generates a log entry.

**Postconditions**:
1. The log entry is collected by the Control Plane.

**Scenario**:
1. Application generates a log.
2. Application streams/sends the log to Control Plane API.
3. Control Plane ingests the log.

**Related Requirements**:
*   :ref:`FR-LOG-001`

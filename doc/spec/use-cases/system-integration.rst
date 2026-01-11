System Integration
==================

This section describes the automated interactions between Managed Applications and the Control Plane.

.. _UC-SYS-APP-AUTH:

UC-SYS-APP-AUTH Feature Flag Retrieval
--------------------------------------
**Actor**: :ref:`Managed Application <TERM-APP-TARGET>` (System)

**Description**:
The :ref:`Managed Application <TERM-APP-TARGET>` retrieves the active feature flags for its tenant to enable/disable functionality dynamically.

**Trigger**:
The :ref:`Managed Application <TERM-APP-TARGET>` starts up or periodic refresh interval elapses.

**Postconditions**:

1. The :ref:`Managed Application <TERM-APP-TARGET>` receives the current set of flags.

**Scenario**:

1. The :ref:`Managed Application <TERM-APP-TARGET>` requests flags from the :ref:`Control Plane <TERM-SYS-CP>`.
2. The :ref:`Control Plane <TERM-SYS-CP>` identifies the tenant (via keys or context).
3. The :ref:`Control Plane <TERM-SYS-CP>` returns the flag configuration.

**Related Requirements**:

*   :ref:`Flag Delivery <FR-FLAG-002>`

.. _UC-SYS-BILL-REPORT:

UC-SYS-BILL-REPORT Billing Event Reporting
------------------------------------------
**Actor**: :ref:`Managed Application <TERM-APP-TARGET>` (System)

**Description**:
The :ref:`Managed Application <TERM-APP-TARGET>` reports a billable event to the :ref:`Control Plane <TERM-SYS-CP>` for tracking.

**Trigger**:
A user performs a billable action within the :ref:`Managed Application <TERM-APP-TARGET>`.

**Postconditions**:

1. The event is persisted in the :ref:`Control Plane <TERM-SYS-CP>`.

**Scenario**:

1. The :ref:`Managed Application <TERM-APP-TARGET>` detects billable event.
2. The :ref:`Managed Application <TERM-APP-TARGET>` sends event data to the :ref:`Control Plane <TERM-SYS-CP>`.
3. The :ref:`Control Plane <TERM-SYS-CP>` validates and stores the event.

**Related Requirements**:

*   :ref:`Billing Event Persistence <FR-BILL-001>`
*   :ref:`Billing Event Ingestion <FR-BILL-002>`

.. _UC-SYS-LOG-REPORT:

UC-SYS-LOG-REPORT Audit Log Reporting
-------------------------------------
**Actor**: :ref:`Managed Application <TERM-APP-TARGET>` (System)

**Description**:
The :ref:`Managed Application <TERM-APP-TARGET>` sends its security and operation logs to the :ref:`Control Plane <TERM-SYS-CP>` for centralized auditing.

**Trigger**:
The :ref:`Managed Application <TERM-APP-TARGET>` generates a log entry.

**Postconditions**:

1. The log entry is collected by the :ref:`Control Plane <TERM-SYS-CP>`.

**Scenario**:

1. The :ref:`Managed Application <TERM-APP-TARGET>` generates a log.
2. The :ref:`Managed Application <TERM-APP-TARGET>` streams/sends the log to the :ref:`Control Plane <TERM-SYS-CP>`.
3. The :ref:`Control Plane <TERM-SYS-CP>` ingests the log.

**Related Requirements**:

*   :ref:`Audit Log Collection <FR-LOG-001>`

.. _UC-SYS-BILL-EXPORT:

UC-SYS-BILL-EXPORT Billing Data Export
--------------------------------------
**Actor**: :ref:`External Billing System <ACT-BILLING>` (System)

**Description**:
The :ref:`External Billing System <ACT-BILLING>` retrieves billing events from the :ref:`Control Plane <TERM-SYS-CP>` to generate invoices and perform reconciliation.

**Trigger**:
Scheduled job or on-demand request from the :ref:`External Billing System <ACT-BILLING>`.

**Postconditions**:

1. The :ref:`External Billing System <ACT-BILLING>` receives the requested :ref:`Billing Events <DAT-BILL-EVENT>`.

**Scenario**:

1. The :ref:`External Billing System <ACT-BILLING>` requests billing events for a specified period/tenant.
2. The :ref:`Control Plane <TERM-SYS-CP>` authenticates and authorizes the request.
3. The :ref:`Control Plane <TERM-SYS-CP>` retrieves matching events from the data store.
4. The :ref:`Control Plane <TERM-SYS-CP>` returns the event data to the :ref:`External Billing System <ACT-BILLING>`.

**Related Requirements**:

*   :ref:`Billing Data Export <FR-BILL-003>`

Interface Requirements
======================

This section defines the external interfaces provided by the system.

.. _API-BILL:

API-BILL Billing Event API
--------------------------
**Type**: REST API
**Direction**: Input (Managed App -> Control Plane)
**Purpose**: To report billable operations performed within the managed SaaS applications.
**Payload**: SHALL include Tenant ID, Timestamp, Event Type, and Quantity.

.. _API-FLAG:

API-FLAG Feature Flag API
-------------------------
**Type**: REST API
**Direction**: Output (Control Plane -> Managed App)
**Purpose**: To retrieve the active feature flags for a specific tenant.
**Caching**: Managed apps SHOULD cache this response to minimize latency.

.. _IF-AUDIT-EXPORT:

IF-AUDIT-EXPORT CSV Export Interface
------------------------------------
**Type**: UI / Download
**User**: :ref:`ACT-AUDIT`
**Format**: Comma-Separated Values (CSV)
**Fields**: Timestamp, Actor ID, Event Type, Resource ID, Outcome, IP Address.

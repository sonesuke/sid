Interface Requirements
======================

This section defines the external interfaces provided by the system.

.. _API-BILL:

API-BILL Billing Event API
--------------------------
**Type**: REST API
**Direction**: Bidirectional (:ref:`TERM-APP-TARGET` <-> :ref:`TERM-SYS-CP` / :ref:`ACT-BILLING` <- :ref:`TERM-SYS-CP`)
**Purpose**: To report billable operations from managed applications and to retrieve billing events for invoicing.
**Payload**: SHALL include Tenant ID, Timestamp, Event Type, and Quantity.

.. _API-LOG:

API-LOG Audit Log API
---------------------
**Type**: REST API
**Direction**: Input (:ref:`TERM-APP-TARGET` -> :ref:`TERM-SYS-CP`)
**Purpose**: To report security and operational events for audit purposes.
**Payload**: SHALL include Timestamp, Actor ID, Event Type, Resource ID, Outcome, and IP Address.


.. _API-FLAG:

API-FLAG Feature Flag API
-------------------------
**Type**: REST API
**Direction**: Output (:ref:`TERM-SYS-CP` -> :ref:`TERM-APP-TARGET`)
**Purpose**: To retrieve the active feature flags for a specific tenant.
**Caching**: Managed apps SHOULD cache this response to minimize latency.




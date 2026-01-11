Billing & Usage
===============

.. _FR-BILL-001:

FR-BILL-001 Billing Event Persistence
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The :ref:`TERM-SYS-CP` SHALL persistently record billable events triggers received via :ref:`FR-BILL-002` as :ref:`Billing Events <DAT-BILL-EVENT>`.

**Realized by**: :ref:`API-BILL`

.. _FR-BILL-002:

FR-BILL-002 Billing Event Ingestion
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The system SHALL provide an API (:ref:`API-BILL`) that allows :ref:`TERM-APP-TARGET` to report billable events (corresponding to :ref:`Billing Events <DAT-BILL-EVENT>`).

**Realized by**: :ref:`API-BILL`

.. _FR-BILL-003:

FR-BILL-003 Billing Data Export
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The :ref:`TERM-SYS-CP` SHALL provide an interface for :ref:`External Billing Systems <ACT-BILLING>` to retrieve :ref:`Billing Events <DAT-BILL-EVENT>` for invoicing and reconciliation purposes.

**Realized by**: :ref:`API-BILL`

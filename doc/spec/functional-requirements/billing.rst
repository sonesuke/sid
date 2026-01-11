Billing & Usage
===============

.. _FR-BILL-001:

FR-BILL-001 Billing Event Persistence
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The :ref:`TERM-SYS-CP` SHALL persistently record billable events triggers received via :ref:`FR-BILL-002` as :ref:`Billing Events <DAT-BILL-EVENT>`.

**Realized by**:

*   :ref:`API-BILL`

**Quality Attributes**:

*   :ref:`Encryption in Transit <NFR-SEC-001>`
*   :ref:`Encryption at Rest <NFR-SEC-002>`
*   :ref:`Data Residency <NFR-DATA-001>`
*   :ref:`Tenant Scalability <NFR-CAP-001>`
*   :ref:`Availability SLO <NFR-OPS-001>`
*   :ref:`Backup and Redundancy <NFR-OPS-004>`

.. _FR-BILL-002:

FR-BILL-002 Billing Event Ingestion
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The system SHALL provide an API (:ref:`API-BILL`) that allows :ref:`TERM-APP-TARGET` to report billable events (corresponding to :ref:`Billing Events <DAT-BILL-EVENT>`).

**Realized by**:

*   :ref:`API-BILL`

**Quality Attributes**:

*   :ref:`Encryption in Transit <NFR-SEC-001>`
*   :ref:`Key Management <NFR-SEC-004>`
*   :ref:`Availability SLO <NFR-OPS-001>`
*   :ref:`Load Balancing and Failover <NFR-OPS-003>`

.. _FR-BILL-003:

FR-BILL-003 Billing Data Export
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The :ref:`TERM-SYS-CP` SHALL provide an interface for :ref:`External Billing Systems <ACT-BILLING>` to retrieve :ref:`Billing Events <DAT-BILL-EVENT>` for invoicing and reconciliation purposes.

**Realized by**:

*   :ref:`API-BILL`

**Quality Attributes**:

*   :ref:`Encryption in Transit <NFR-SEC-001>`
*   :ref:`Key Management <NFR-SEC-004>`
*   :ref:`Least Privilege <NFR-SEC-005>`
*   :ref:`Data Residency <NFR-DATA-001>`
*   :ref:`Availability SLO <NFR-OPS-001>`

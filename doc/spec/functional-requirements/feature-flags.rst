Feature Flag Management
=======================

.. _FR-FLAG-001:

FR-FLAG-001 Flag Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The :ref:`TERM-SYS-CP` SHALL allow :ref:`ACT-OPS` to configure :ref:`Feature Flags <DAT-FLAG>` for each :ref:`Tenant <DAT-TENANT>`.

**Realized by**: :ref:`Operator Console <IF-OPS-CONSOLE>`

.. _FR-FLAG-002:

FR-FLAG-002 Flag Delivery
^^^^^^^^^^^^^^^^^^^^^^^^^
The system SHALL provide an interface via :ref:`API-FLAG` for :ref:`TERM-APP-TARGET` to retrieve the current state of :ref:`Feature Flags <DAT-FLAG>`.

**Realized by**: :ref:`API-FLAG`

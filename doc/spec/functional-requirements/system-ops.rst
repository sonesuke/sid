System Operations
=================

.. _FR-SYS-001:

FR-SYS-001 Application Registration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The :ref:`TERM-SYS-CP` SHALL allow :ref:`ACT-DEV` to register a new :ref:`Managed Application <DAT-APP>`.
The system SHALL generate a unique Application ID upon registration.

.. _FR-SYS-002:

FR-SYS-002 API Key Management
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The :ref:`TERM-SYS-CP` SHALL allow :ref:`ACT-DEV` to issue :ref:`API Access Keys <DAT-KEY>` for a registered :ref:`Managed Application <DAT-APP>`.
The system SHALL display the Client Secret only once upon issuance.
The system SHALL allow :ref:`ACT-DEV` to revoke existing keys.

.. _FR-SYS-003:

FR-SYS-003 Application Lifecycle Management
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The :ref:`TERM-SYS-CP` SHALL allow :ref:`ACT-DEV` to update the configuration of a :ref:`Managed Application <DAT-APP>`.
The :ref:`TERM-SYS-CP` SHALL allow :ref:`ACT-DEV` to change the :ref:`Status <DAT-APP>` (e.g., Disable) to block access.

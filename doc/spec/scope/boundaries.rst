Scope
=====

This section defines the functionalities that are In-Scope and explicitly Out-of-Scope for the project.

In-Scope
--------

.. _FR-AUTH:

Authentication (FR-AUTH)
^^^^^^^^^^^^^^^^^^^^^^^^
The system SHALL provide a centralized authentication mechanism (issuance of tokens) for all managed SaaS applications.

.. _FR-FLAG:

Feature Flag Management (FR-FLAG)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The system SHALL provide a mechanism to deliver feature flags to applications, enabling dynamic control of functionality.

.. _FR-LOG:

Logging and Auditing (FR-LOG)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The system SHALL collect operational logs and provide them to Auditors.
The system SHALL record billable operational events.

Out-of-Scope
------------

Payment Processing
^^^^^^^^^^^^^^^^^^
The system SHALL NOT handle handling of actual payments (e.g., credit card transactions) or invoice generation. This is delegated to an external billing system.

Platform Operator Management
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The management of :ref:`Platform Operator <ACT-OPS>` accounts (registration, deletion, identity management) and their authentication to the :ref:`Control Plane <TERM-SYS-CP>` (:ref:`IF-OPS-CONSOLE`) is Out-of-Scope for this specification.
These functions are delegated to an external Identity Provider (IdP) and managed by an external team. The system assumes a valid identity is provided via the IdP integration.

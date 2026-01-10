Functional Requirements
=======================

This section defines the Functional Requirements (FR) of the system.

Authentication & Authorization
------------------------------

.. _FR-AUTH-001:

FR-AUTH-001 Supported Authentication Methods
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The :ref:`TERM-SYS-CP` SHALL support the following authentication methods for Tenant Users:
*   OpenID Connect (OIDC)
*   Password-based authentication

.. _FR-AUTH-002:

FR-AUTH-002 SAML Exclusion
^^^^^^^^^^^^^^^^^^^^^^^^^^
The :ref:`TERM-SYS-CP` SHALL NOT support SAML authentication.

.. _FR-AUTH-003:

FR-AUTH-003 Tenant SSO Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The :ref:`TERM-SYS-CP` SHALL allow a Tenant Owner (role of :ref:`ACT-USER`) to register an external Identity Provider (IdP) for Single Sign-On (SSO).

Tenant Administration
---------------------

.. _FR-TENANT-001:

FR-TENANT-001 User Invitation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The :ref:`TERM-SYS-CP` SHALL allow Tenant Owners and Administrators to invite new users to their tenant.

.. _FR-TENANT-002:

FR-TENANT-002 User Deletion
^^^^^^^^^^^^^^^^^^^^^^^^^^^
The :ref:`TERM-SYS-CP` SHALL allow Tenant Owners and Administrators to delete users from their tenant.

.. _FR-TENANT-003:

FR-TENANT-003 Contract Modification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The :ref:`TERM-SYS-CP` SHALL allow only Tenant Owners to modify the tenant's subscription contract.

Feature Flag Management
-----------------------

.. _FR-FLAG-001:

FR-FLAG-001 Flag Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The :ref:`TERM-SYS-CP` SHALL allow :ref:`ACT-OPS` to configure feature flags for each tenant.

.. _FR-FLAG-002:

FR-FLAG-002 Flag Delivery
^^^^^^^^^^^^^^^^^^^^^^^^^
The system SHALL provide an interface for :ref:`TERM-APP-TARGET` to retrieve the current state of feature flags.

Billing & Usage
---------------

.. _FR-BILL-001:

FR-BILL-001 Billing Event Persistence
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The :ref:`TERM-SYS-CP` SHALL persistently record billable events triggers received via :ref:`FR-BILL-002`.

.. _FR-BILL-002:

FR-BILL-002 Billing Event Ingestion
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The system SHALL provide an API (:ref:`API-BILL`) that allows :ref:`TERM-APP-TARGET` to report billable events.

Audit & Logging
---------------

.. _FR-LOG-001:

FR-LOG-001 Audit Log Collection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The :ref:`TERM-SYS-CP` SHALL collect security and operational logs from all components via :ref:`API-LOG`.

.. _FR-LOG-002:

FR-LOG-002 Audit Log Export
^^^^^^^^^^^^^^^^^^^^^^^^^^^
The :ref:`TERM-SYS-CP` SHALL allow :ref:`ACT-AUDIT` to export audit logs in CSV format.

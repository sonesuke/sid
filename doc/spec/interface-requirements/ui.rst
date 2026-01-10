User Interfaces
===============

This section defines the primary User Interfaces (UI) provided by the Control Plane.

.. _IF-OPS-CONSOLE:

IF-OPS-CONSOLE Operator Console
-------------------------------
**User**: :ref:`ACT-OPS`
**Description**:
The administrative web portal for Platform Operators.
Provides capabilities for tenant provisioning, feature flag management, and system monitoring.

.. _IF-TENANT-CONSOLE:

IF-TENANT-CONSOLE Tenant Administration Console
-----------------------------------------------
**User**: :ref:`ACT-USER` (Owner, Admin)
**Description**:
The self-service web portal for Tenant Administrators.
Allows management of users, invitations, SSO configuration, and subscription viewing.

.. _IF-LOGIN-UI:

IF-LOGIN-UI Universal Login Page
--------------------------------
**User**: :ref:`ACT-USER`, :ref:`ACT-OPS`, :ref:`ACT-AUDIT`
**Description**:
The centralized login page presented to all users.
Supports input for Email/Password and redirects for SSO/OIDC authentication.

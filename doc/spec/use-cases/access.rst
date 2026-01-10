Access Management
=================

.. _UC-LOGIN:

UC-LOGIN Tenant User Login
--------------------------
**Actor**: :ref:`ACT-USER`

**Description**:
The :ref:`Tenant User <ACT-USER>` logs in to the system or a managed application using their credentials or an external IdP.

**Trigger**:
The :ref:`Tenant User <ACT-USER>` attempts to access a protected resource.

**Preconditions**:
1. The :ref:`Tenant User <ACT-USER>` account exists and is active.

**Postconditions**:
1. The :ref:`Tenant User <ACT-USER>` receives an authentication token.
2. The :ref:`Tenant User <ACT-USER>` gains access to the application.

**Scenario**:
1. The :ref:`Tenant User <ACT-USER>` navigates to the :ref:`IF-LOGIN-UI`.
2. The :ref:`Tenant User <ACT-USER>` selects authentication method (Password or SSO).
3. If Password: The :ref:`Tenant User <ACT-USER>` enters email and password.
4. If SSO: The :ref:`Tenant User <ACT-USER>` is redirected to IdP and authenticates.
5. System validates credentials.
6. System issues an authentication token.

**Related Requirements**:
*   :ref:`FR-AUTH-001`

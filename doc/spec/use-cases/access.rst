Access Management
=================

.. _UC-LOGIN:

UC-LOGIN Tenant User Login
--------------------------
**Actor**: :ref:`ACT-USER`

**Description**:
A Tenant User logs in to the system or a managed application using their credentials or an external IdP.

**Trigger**:
User attempts to access a protected resource.

**Preconditions**:
1. User account exists and is active.

**Postconditions**:
1. User receives an authentication token.
2. User gains access to the application.

**Scenario**:
1. User navigates to the :ref:`IF-LOGIN-UI`.
2. User selects authentication method (Password or SSO).
3. If Password: User enters email and password.
4. If SSO: User is redirected to IdP and authenticates.
5. System validates credentials.
6. System issues an authentication token.

**Related Requirements**:
*   :ref:`FR-AUTH-001`

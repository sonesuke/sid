Access Management
=================

.. _UC-LOGIN:

UC-LOGIN Tenant User Login
--------------------------
**Actor**: :ref:`Tenant User <ACT-USER>`

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

1. The :ref:`Tenant User <ACT-USER>` navigates to the **Universal Login Page**.
2. The :ref:`Tenant User <ACT-USER>` selects authentication method (Password or SSO).
3. If Password: The :ref:`Tenant User <ACT-USER>` enters email and password.
4. If SSO: The :ref:`Tenant User <ACT-USER>` is redirected to IdP and authenticates.
5. The :ref:`Control Plane <TERM-SYS-CP>` validates credentials.
6. The :ref:`Control Plane <TERM-SYS-CP>` issues an authentication token.

3. **Related Requirements**:

*   :ref:`Supported Authentication Methods <FR-AUTH-001>`
*   :ref:`Session Management <FR-AUTH-005>`

.. _UC-LOGOUT:

UC-LOGOUT Tenant User Logout
----------------------------
**Actor**: :ref:`Tenant User <ACT-USER>`

**Description**:
The :ref:`Tenant User <ACT-USER>` explicitly terminates their session to secure their access.

**Trigger**:
The :ref:`Tenant User <ACT-USER>` selects "Logout" in the **Universal Login Page** or Managed Application.

**Preconditions**:

1. The :ref:`Tenant User <ACT-USER>` has an active :ref:`Session <DAT-SESSION>`.

**Postconditions**:

1. The :ref:`Session <DAT-SESSION>` is invalidated.
2. The user is redirected to the public login page.

**Scenario**:

1. The :ref:`Tenant User <ACT-USER>` initiates the logout action.
2. The :ref:`Control Plane <TERM-SYS-CP>` invalidates the session token.
3. The :ref:`Control Plane <TERM-SYS-CP>` redirects the user.

**Related Requirements**:

*   :ref:`Session Management <FR-AUTH-005>`
*   :ref:`Control Plane Auditing <FR-LOG-003>`

.. _UC-AUTH-RESET:

UC-AUTH-RESET Password Reset
----------------------------
**Actor**: :ref:`Tenant User <ACT-USER>`

**Description**:
The :ref:`Tenant User <ACT-USER>` initiates a password reset flow when they have forgotten their credentials.

**Trigger**:
The :ref:`Tenant User <ACT-USER>` selects "Forgot Password" on the **Universal Login Page**.

**Preconditions**:

1. The :ref:`Tenant User <ACT-USER>` has a registered account with an email address.
2. The account is configured for password authentication.

**Postconditions**:

1. The :ref:`Tenant User <ACT-USER>` has updated their credential.
2. All existing :ref:`Sessions <DAT-SESSION>` are invalidated.

**Scenario**:

1. The :ref:`Tenant User <ACT-USER>` enters their email address on the **Universal Login Page**.
2. The :ref:`Control Plane <TERM-SYS-CP>` sends a password reset link/token to the email.
3. The :ref:`Tenant User <ACT-USER>` clicks the link and enters a new password.
4. The :ref:`Control Plane <TERM-SYS-CP>` updates the credential store.
5. The :ref:`Control Plane <TERM-SYS-CP>` invalidates all active sessions for the user.

**Related Requirements**:

*   :ref:`Password Reset <FR-AUTH-004>`
*   :ref:`Control Plane Auditing <FR-LOG-003>`

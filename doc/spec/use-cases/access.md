# Access Management

<a id="UC-LOGIN"></a>

## UC-LOGIN Tenant User Login

**Actor**: [ACT-USER (Tenant User)](../actors/list.md#ACT-USER)

**Description**:
The [ACT-USER (Tenant User)](../actors/list.md#ACT-USER) logs in to the system or a managed application using their credentials or an external IdP.

**Trigger**:
The [ACT-USER (Tenant User)](../actors/list.md#ACT-USER) attempts to access a protected resource.

**Preconditions**:

1. The [ACT-USER (Tenant User)](../actors/list.md#ACT-USER) account exists and is active.

**Postconditions**:

1. The [ACT-USER (Tenant User)](../actors/list.md#ACT-USER) receives an authentication token.
2. The [ACT-USER (Tenant User)](../actors/list.md#ACT-USER) gains access to the application.

**Scenario**:

1. The [ACT-USER (Tenant User)](../actors/list.md#ACT-USER) navigates to the **Universal Login Page**.
2. The [ACT-USER (Tenant User)](../actors/list.md#ACT-USER) selects authentication method (Password or SSO).
3. If Password: The [ACT-USER (Tenant User)](../actors/list.md#ACT-USER) enters email and password.
4. If SSO: The [ACT-USER (Tenant User)](../actors/list.md#ACT-USER) is redirected to IdP and authenticates.
5. The [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP) validates credentials.
6. The [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP) issues an authentication token.

**Related Requirements**:

* [FR-AUTH-001 (Supported Authentication Methods)](../functional-requirements/auth.md#FR-AUTH-001)
* [FR-AUTH-005 (Session Management)](../functional-requirements/auth.md#FR-AUTH-005)
* [FR-AUTH (Authentication)](../scope/boundaries.md#FR-AUTH)

<a id="UC-LOGOUT"></a>

## UC-LOGOUT Tenant User Logout

**Actor**: [ACT-USER (Tenant User)](../actors/list.md#ACT-USER)

**Description**:
The [ACT-USER (Tenant User)](../actors/list.md#ACT-USER) explicitly terminates their session to secure their access.

**Trigger**:
The [ACT-USER (Tenant User)](../actors/list.md#ACT-USER) selects "Logout" in the **Universal Login Page** or Managed Application.

**Preconditions**:

1. The [ACT-USER (Tenant User)](../actors/list.md#ACT-USER) has an active [DAT-SESSION (User Sessions)](../data-model/schema.md#DAT-SESSION).

**Postconditions**:

1. The [DAT-SESSION (User Sessions)](../data-model/schema.md#DAT-SESSION) is invalidated.
2. The user is redirected to the public login page.

**Scenario**:

1. The [ACT-USER (Tenant User)](../actors/list.md#ACT-USER) initiates the logout action.
2. The [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP) invalidates the session token.
3. The [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP) redirects the user.

**Related Requirements**:

* [FR-AUTH-005 (Session Management)](../functional-requirements/auth.md#FR-AUTH-005)
* [FR-LOG-003 (Control Plane Auditing)](../functional-requirements/audit.md#FR-LOG-003)

<a id="UC-AUTH-RESET"></a>

## UC-AUTH-RESET Password Reset

**Actor**: [ACT-USER (Tenant User)](../actors/list.md#ACT-USER)

**Description**:
The [ACT-USER (Tenant User)](../actors/list.md#ACT-USER) initiates a password reset flow when they have forgotten their credentials.

**Trigger**:
The [ACT-USER (Tenant User)](../actors/list.md#ACT-USER) selects "Forgot Password" on the **Universal Login Page**.

**Preconditions**:

1. The [ACT-USER (Tenant User)](../actors/list.md#ACT-USER) has a registered account with an email address.
2. The account is configured for password authentication.

**Postconditions**:

1. The [ACT-USER (Tenant User)](../actors/list.md#ACT-USER) has updated their credential.
2. All existing [DAT-SESSION (User Sessions)](../data-model/schema.md#DAT-SESSION) are invalidated.

**Scenario**:

1. The [ACT-USER (Tenant User)](../actors/list.md#ACT-USER) enters their email address on the **Universal Login Page**.
2. The [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP) sends a password reset link/token to the email.
3. The [ACT-USER (Tenant User)](../actors/list.md#ACT-USER) clicks the link and enters a new password.
4. The [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP) updates the credential store.
5. The [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP) invalidates all active sessions for the user.

**Related Requirements**:

* [FR-AUTH-004 (Password Reset)](../functional-requirements/auth.md#FR-AUTH-004)
* [FR-LOG-003 (Control Plane Auditing)](../functional-requirements/audit.md#FR-LOG-003)

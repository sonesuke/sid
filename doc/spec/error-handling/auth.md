# Authentication & Authorization Errors

<a id="ERR-AUTH-401"></a>

## ERR-AUTH-401 Invalid Credentials
**Description**:
Authentication failed due to invalid credentials.

**Triggers**:

*   Incorrect password
*   Invalid or expired authentication token
*   Unknown username/email

**Outcome**:

*   Authentication is denied
*   No session is established

**Constraints**:

*   [Error Disclosure ](../constraints-and-assumptions/index.md#CON-SEC-009)

<a id="ERR-AUTH-403"></a>

## ERR-AUTH-403 Access Denied
**Description**:
An authenticated user attempted an operation they are not authorized to perform.

**Triggers**:

*   Insufficient role or permissions
*   Attempting to access another tenant's resources
*   Disabled user account

**Outcome**:

*   Operation is rejected
*   No state change occurs

**Constraints**:

*   [Error Disclosure ](../constraints-and-assumptions/index.md#CON-SEC-009)

<a id="ERR-AUTH-440"></a>

## ERR-AUTH-440 Session Expired
**Description**:
The user's session has expired or been invalidated.

**Triggers**:

*   Session timeout
*   Administrative session revocation
*   Password change
*   User deletion or disabling

**Outcome**:

*   Current operation is rejected
*   User must re-authenticate

<a id="ERR-AUTH-461"></a>

## ERR-AUTH-461 MFA Required
**Description**:
Multi-factor authentication is required but not provided.

**Triggers**:

*   MFA is enabled for the user/tenant
*   Adaptive authentication detected elevated risk

**Outcome**:

*   Authentication flow pauses
*   User is prompted for MFA verification

**Constraints**:

*   [MFA ](../constraints-and-assumptions/index.md#CON-SEC-005)

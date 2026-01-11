Authentication & Authorization Errors
=====================================

.. _ERR-AUTH-401:

ERR-AUTH-401 Invalid Credentials
--------------------------------
**Description**:
Authentication failed due to invalid credentials.

**Triggers**:

*   Incorrect password
*   Invalid or expired authentication token
*   Unknown username/email

**Outcome**:

*   Authentication is denied
*   No session is established


**Related Requirements**:

*   :ref:`FR-AUTH-001`
*   :ref:`FR-AUTH-004`

**Constraints**:

*   :ref:`CON-SEC-009`

.. _ERR-AUTH-403:

ERR-AUTH-403 Access Denied
--------------------------
**Description**:
An authenticated user attempted an operation they are not authorized to perform.

**Triggers**:

*   Insufficient role or permissions
*   Attempting to access another tenant's resources
*   Disabled user account

**Outcome**:

*   Operation is rejected
*   No state change occurs

**Related Requirements**:

*   :ref:`FR-AUTH-005`
*   :ref:`FR-TENANT-004`
*   :ref:`FR-TENANT-006`

**Constraints**:

*   :ref:`CON-SEC-009`

.. _ERR-AUTH-440:

ERR-AUTH-440 Session Expired
----------------------------
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

**Related Requirements**:

*   :ref:`FR-AUTH-005`
*   :ref:`FR-TENANT-002`
*   :ref:`FR-TENANT-006`

.. _ERR-AUTH-461:

ERR-AUTH-461 MFA Required
-------------------------
**Description**:
Multi-factor authentication is required but not provided.

**Triggers**:

*   MFA is enabled for the user/tenant
*   Adaptive authentication detected elevated risk

**Outcome**:

*   Authentication flow pauses
*   User is prompted for MFA verification

**Related Requirements**:

*   :ref:`FR-AUTH-001`

**Constraints**:

*   :ref:`CON-SEC-005`

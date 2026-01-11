Tenant Administration
=====================

.. _UC-TENANT-USER-DELETE:

UC-TENANT-USER-DELETE User Deletion
-----------------------------------
**Actor**: :ref:`Tenant User <ACT-USER>` (Role: Owner, Administrator)

**Description**:
The :ref:`Tenant User <ACT-USER>` (Role: Owner or Administrator) removes a user from the tenant organization.

**Trigger**:
The :ref:`Tenant User <ACT-USER>` selects "Delete User" in the **Tenant Administration Console**.

**Preconditions**:

1. The :ref:`Tenant User <ACT-USER>` is logged in with sufficient privileges.
2. Target user exists.

**Postconditions**:

1. Target user is removed from authentication and cannot access applications.
2. All active :ref:`Sessions <DAT-SESSION>` for the user are invalidated.

**Scenario**:

1. The :ref:`Tenant User <ACT-USER>` selects the user to remove.
2. The :ref:`Tenant User <ACT-USER>` confirms deletion.
3. The :ref:`Control Plane <TERM-SYS-CP>` removes the user.
4. The :ref:`Control Plane <TERM-SYS-CP>` invalidates existing sessions.

**Related Requirements**:

*   :ref:`User Deletion <FR-TENANT-002>`
*   :ref:`Control Plane Auditing <FR-LOG-003>`

.. _UC-TENANT-USER-UPDATE:

UC-TENANT-USER-UPDATE User Role Update
--------------------------------------
**Actor**: :ref:`Tenant User <ACT-USER>` (Role: Owner, Administrator)

**Description**:
The :ref:`Tenant User <ACT-USER>` (Role: Owner or Administrator) modifies the role of an existing user within the tenant organization.

**Trigger**:
The :ref:`Tenant User <ACT-USER>` selects "Edit Role" in the **Tenant Administration Console**.

**Preconditions**:

1. The :ref:`Tenant User <ACT-USER>` is logged in with sufficient privileges.
2. Target user exists.

**Postconditions**:

1. Target user's role is updated.
2. All active :ref:`Sessions <DAT-SESSION>` for the user are invalidated.

**Scenario**:

1. The :ref:`Tenant User <ACT-USER>` selects the user to update.
2. The :ref:`Tenant User <ACT-USER>` selects the new role.
3. The :ref:`Tenant User <ACT-USER>` saves the changes.
4. The :ref:`Control Plane <TERM-SYS-CP>` validates the permissions (e.g., cannot downgrade own role if last Owner).
5. The :ref:`Control Plane <TERM-SYS-CP>` updates the user record.
6. The :ref:`Control Plane <TERM-SYS-CP>` invalidates existing sessions to enforce new permissions.

**Related Requirements**:

*   :ref:`User Role Management <FR-TENANT-004>`
*   :ref:`Control Plane Auditing <FR-LOG-003>`

.. _UC-TENANT-USER-STATUS-UPDATE:

UC-TENANT-USER-STATUS-UPDATE User Status Update
-----------------------------------------------
**Actor**: :ref:`Tenant User <ACT-USER>` (Role: Owner, Administrator)

**Description**:
The :ref:`Tenant User <ACT-USER>` (Role: Owner or Administrator) changes the status of a user (e.g., to Disabled to block access).

**Trigger**:
The :ref:`Tenant User <ACT-USER>` selects "Disable User" or "Enable User" in the **Tenant Administration Console**.

**Preconditions**:

1. The :ref:`Tenant User <ACT-USER>` is logged in with sufficient privileges.
2. Target user exists.

**Postconditions**:

1. Target user's status is updated.
2. If Disabled, all active :ref:`Sessions <DAT-SESSION>` for the user are invalidated.

**Scenario**:

1. The :ref:`Tenant User <ACT-USER>` selects the user to update.
2. The :ref:`Tenant User <ACT-USER>` toggles the status (e.g., Active to Disabled).
3. The :ref:`Tenant User <ACT-USER>` saves the changes.
4. The :ref:`Control Plane <TERM-SYS-CP>` validates the action.
5. The :ref:`Control Plane <TERM-SYS-CP>` updates the user record.
6. The :ref:`Control Plane <TERM-SYS-CP>` invalidates sessions if required.

**Related Requirements**:

*   :ref:`User Status Management <FR-TENANT-006>`
*   :ref:`Control Plane Auditing <FR-LOG-003>`

.. _UC-TENANT-SESSION-REVOKE:

UC-TENANT-SESSION-REVOKE Session Revocation
-------------------------------------------
**Actor**: :ref:`Tenant User <ACT-USER>` (Role: Owner, Administrator)

**Description**:
The :ref:`Tenant User <ACT-USER>` (Role: Owner or Administrator) invalidates a specific user's active sessions to force re-authentication.

**Trigger**:
The :ref:`Tenant User <ACT-USER>` selects "Revoke Sessions" for a user in the **Tenant Administration Console**.

**Preconditions**:

1. The :ref:`Tenant User <ACT-USER>` is logged in with sufficient privileges.
2. The target :ref:`User <DAT-USER>` exists.

**Postconditions**:

1. All active :ref:`Sessions <DAT-SESSION>` for the target User are invalidated.
2. The target User is required to log in again.

**Scenario**:

1. The :ref:`Tenant User <ACT-USER>` identifies the target user in the **Tenant Administration Console**.
2. The :ref:`Tenant User <ACT-USER>` initiates the session revocation.
3. The :ref:`Control Plane <TERM-SYS-CP>` invalidates all tokens associated with the user.

**Related Requirements**:

*   :ref:`Session Management <FR-AUTH-005>`
*   :ref:`Control Plane Auditing <FR-LOG-003>`

.. _UC-TENANT-INVITE:

UC-TENANT-INVITE User Invitation
--------------------------------
**Actor**: :ref:`Tenant User <ACT-USER>` (Role: Owner, Administrator)

**Description**:
The :ref:`Tenant User <ACT-USER>` (Role: Owner or Administrator) invites a new user to join their tenant organization. The invited user receives an email to set up their account.

**Trigger**:
The :ref:`Tenant User <ACT-USER>` selects "Invite User" in the **Tenant Administration Console**.

**Preconditions**:

1. The :ref:`Tenant User <ACT-USER>` is logged in with Owner or Administrator role.
2. The invited email address does not already exist in the tenant.

**Postconditions**:

1. An invitation email is sent to the specified address.
2. A user record is created with "Invited" status.

**Scenario**:

1. The :ref:`Tenant User <ACT-USER>` enters the email address and role (Admin or User) of the new user.
2. The :ref:`Tenant User <ACT-USER>` submits the invitation.
3. The :ref:`Control Plane <TERM-SYS-CP>` validates the input and permissions.
4. The :ref:`Control Plane <TERM-SYS-CP>` sends the invitation email.

**Related Requirements**:

*   :ref:`User Invitation <FR-TENANT-001>`
*   :ref:`Control Plane Auditing <FR-LOG-003>`

.. _UC-TENANT-SSO:

UC-TENANT-SSO SSO Configuration
-------------------------------
**Actor**: :ref:`Tenant User <ACT-USER>` (Role: Owner)

**Description**:
The :ref:`Tenant User <ACT-USER>` (Role: Owner) configures an external Identity Provider (OIDC) to enable Single Sign-On for their users.

**Trigger**:
The :ref:`Tenant User <ACT-USER>` initiates "SSO Setup" in the **Tenant Administration Console**.

**Preconditions**:

1. The :ref:`Tenant User <ACT-USER>` is logged in with Owner role.
2. The :ref:`Tenant User <ACT-USER>` has the necessary metadata (Client ID, Issuer URL) from their IdP.

**Postconditions**:

1. The tenant is configured to use the specified IdP.
2. Subsequent logins from this tenant's domain can use SSO.

**Scenario**:

1. The :ref:`Tenant User <ACT-USER>` enters IdP details (Issuer URL, Client ID, Client Secret).
2. The :ref:`Control Plane <TERM-SYS-CP>` verifies the IdP configuration (discovery).
3. The :ref:`Control Plane <TERM-SYS-CP>` saves the configuration.

**Related Requirements**:

*   :ref:`Tenant SSO Configuration <FR-AUTH-003>`
*   :ref:`Control Plane Auditing <FR-LOG-003>`

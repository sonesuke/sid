Tenant Administration
=====================

.. _UC-TENANT-USER-DELETE:

UC-TENANT-USER-DELETE User Deletion
-----------------------------------
**Actor**: :ref:`ACT-USER` (Role: Owner, Administrator)

**Description**:
The :ref:`Tenant User <ACT-USER>` (Role: Owner or Administrator) removes a user from the tenant organization.

**Trigger**:
The :ref:`Tenant User <ACT-USER>` selects "Delete User" in the :ref:`IF-TENANT-CONSOLE`.

**Preconditions**:
**Preconditions**:
1. The :ref:`Tenant User <ACT-USER>` is logged in with sufficient privileges.
2. Target user exists.

**Postconditions**:
1. Target :ref:`User <DAT-USER>` is removed from authentication and cannot access applications.

**Scenario**:
1. The :ref:`Tenant User <ACT-USER>` selects the user to remove.
2. The :ref:`Tenant User <ACT-USER>` confirms deletion.
3. The :ref:`Control Plane <TERM-SYS-CP>` removes the user.

**Related Requirements**:
*   :ref:`FR-TENANT-002`
*   :ref:`FR-LOG-003`

.. _UC-TENANT-USER-UPDATE:

UC-TENANT-USER-UPDATE User Role Update
--------------------------------------
**Actor**: :ref:`ACT-USER` (Role: Owner, Administrator)

**Description**:
The :ref:`Tenant User <ACT-USER>` (Role: Owner or Administrator) modifies the role of an existing user within the tenant organization.

**Trigger**:
The :ref:`Tenant User <ACT-USER>` selects "Edit Role" in the :ref:`IF-TENANT-CONSOLE`.

**Preconditions**:
1. The :ref:`Tenant User <ACT-USER>` is logged in with sufficient privileges.
2. Target user exists.

**Postconditions**:
1. Target :ref:`User's <DAT-USER>` :ref:`role <DAT-ROLE>` is updated.
2. Target user's permissions are immediately adjusted.

**Scenario**:
1. The :ref:`Tenant User <ACT-USER>` selects the user to update.
2. The :ref:`Tenant User <ACT-USER>` selects the new role.
3. The :ref:`Tenant User <ACT-USER>` saves the changes.
4. The :ref:`Control Plane <TERM-SYS-CP>` validates the permissions (e.g., cannot downgrade own role if last Owner).
5. The :ref:`Control Plane <TERM-SYS-CP>` updates the user record.

**Related Requirements**:
*   :ref:`FR-TENANT-004`
*   :ref:`FR-LOG-003`

.. _UC-TENANT-INVITE:

UC-TENANT-INVITE User Invitation
--------------------------------
**Actor**: :ref:`ACT-USER` (Role: Owner, Administrator)

**Description**:
The :ref:`Tenant User <ACT-USER>` (Role: Owner or Administrator) invites a new user to join their tenant organization. The invited user receives an email to set up their account.

**Trigger**:
The :ref:`Tenant User <ACT-USER>` selects "Invite User" in the :ref:`IF-TENANT-CONSOLE`.

**Preconditions**:
1. The :ref:`Tenant User <ACT-USER>` is logged in with Owner or Administrator role.
2. The invited email address does not already exist in the tenant.

**Postconditions**:
1. An invitation email is sent to the specified address.
2. A :ref:`User <DAT-USER>` record is created with "Invited" :ref:`status <DAT-USER>`.

**Scenario**:
1. The :ref:`Tenant User <ACT-USER>` enters the email address and role (Admin or User) of the new user.
2. The :ref:`Tenant User <ACT-USER>` submits the invitation.
3. The :ref:`Control Plane <TERM-SYS-CP>` validates the input and permissions.
4. The :ref:`Control Plane <TERM-SYS-CP>` sends the invitation email.

**Related Requirements**:
*   :ref:`FR-TENANT-001`
*   :ref:`FR-LOG-003`

.. _UC-TENANT-SSO:

UC-TENANT-SSO SSO Configuration
-------------------------------
**Actor**: :ref:`ACT-USER` (Role: Owner)

**Description**:
The :ref:`Tenant User <ACT-USER>` (Role: Owner) configures an external Identity Provider (OIDC) to enable Single Sign-On for their users.

**Trigger**:
The :ref:`Tenant User <ACT-USER>` initiates "SSO Setup" in the :ref:`IF-TENANT-CONSOLE`.

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
*   :ref:`FR-AUTH-003`
*   :ref:`FR-LOG-003`

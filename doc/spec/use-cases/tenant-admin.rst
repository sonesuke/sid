Tenant Administration
=====================

.. _UC-TENANT-INVITE:

UC-TENANT-INVITE User Invitation
--------------------------------
**Actor**: :ref:`ACT-USER` (Role: Owner, Administrator)

**Description**:
A Tenant Owner or Administrator invites a new user to join their tenant organization. The invited user receives an email to set up their account.

**Trigger**:
Actor selects "Invite User" in the administration console.

**Preconditions**:
1. Actor is logged in as Owner or Administrator.
2. The invited email address does not already exist in the tenant.

**Postconditions**:
1. An invitation email is sent to the specified address.
2. A user record is created with "Invited" status.

**Scenario**:
1. Actor enters the email address and role (Admin or User) of the new user.
2. Actor submits the invitation.
3. System validates the input and permissions.
4. System sends the invitation email.

**Related Requirements**:
*   :ref:`FR-TENANT-001`

.. _UC-TENANT-SSO:

UC-TENANT-SSO SSO Configuration
-------------------------------
**Actor**: :ref:`ACT-USER` (Role: Owner)

**Description**:
A Tenant Owner configures an external Identity Provider (OIDC) to enable Single Sign-On for their users.

**Trigger**:
Owner initiates "SSO Setup".

**Preconditions**:
1. Actor is logged in as Owner.
2. Actor has the necessary metadata (Client ID, Issuer URL) from their IdP.

**Postconditions**:
1. The tenant is configured to use the specified IdP.
2. Subsequent logins from this tenant's domain can use SSO.

**Scenario**:
1. Owne enters IdP details (Issuer URL, Client ID, Client Secret).
2. System verifies the IdP configuration (discovery).
3. System saves the configuration.

**Related Requirements**:
*   :ref:`FR-AUTH-003`

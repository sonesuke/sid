# Tenant Administration

<a id="UC-TENANT-USER-DELETE"></a>

## UC-TENANT-USER-DELETE User Deletion

**Actor**: [ACT-USER (Tenant User)](../actors/list.md#ACT-USER) (Role: Owner, Administrator)

**Description**:
The [ACT-USER (Tenant User)](../actors/list.md#ACT-USER) (Role: Owner or Administrator) removes a user from the tenant organization.

**Trigger**:
The [ACT-USER (Tenant User)](../actors/list.md#ACT-USER) selects "Delete User" in the **Tenant Administration Console**.

**Preconditions**:

1. The [ACT-USER (Tenant User)](../actors/list.md#ACT-USER) is logged in with sufficient privileges.
2. Target user exists.

**Postconditions**:

1. Target user is removed from authentication and cannot access applications.
2. All active [DAT-SESSION (User Sessions)](../data-model/schema.md#DAT-SESSION) for the user are invalidated.

**Scenario**:

1. The [ACT-USER (Tenant User)](../actors/list.md#ACT-USER) selects the user to remove.
2. The [ACT-USER (Tenant User)](../actors/list.md#ACT-USER) confirms deletion.
3. The [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP) removes the user.
4. The [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP) invalidates existing sessions.

**Related Requirements**:

* [FR-TENANT-002 (User Deletion)](../functional-requirements/tenant-admin.md#FR-TENANT-002)
* [FR-LOG-003 (Control Plane Auditing)](../functional-requirements/audit.md#FR-LOG-003)

<a id="UC-TENANT-USER-UPDATE"></a>

## UC-TENANT-USER-UPDATE User Role Update

**Actor**: [ACT-USER (Tenant User)](../actors/list.md#ACT-USER) (Role: Owner, Administrator)

**Description**:
The [ACT-USER (Tenant User)](../actors/list.md#ACT-USER) (Role: Owner or Administrator) modifies the role of an existing user within the tenant organization.

**Trigger**:
The [ACT-USER (Tenant User)](../actors/list.md#ACT-USER) selects "Edit Role" in the **Tenant Administration Console**.

**Preconditions**:

1. The [ACT-USER (Tenant User)](../actors/list.md#ACT-USER) is logged in with sufficient privileges.
2. Target user exists.

**Postconditions**:

1. Target user's role is updated.
2. All active [DAT-SESSION (User Sessions)](../data-model/schema.md#DAT-SESSION) for the user are invalidated.

**Scenario**:

1. The [ACT-USER (Tenant User)](../actors/list.md#ACT-USER) selects the user to update.
2. The [ACT-USER (Tenant User)](../actors/list.md#ACT-USER) selects the new role.
3. The [ACT-USER (Tenant User)](../actors/list.md#ACT-USER) saves the changes.
4. The [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP) validates the permissions (e.g., cannot downgrade own role if last Owner).
5. The [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP) updates the user record.
6. The [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP) invalidates existing sessions to enforce new permissions.

**Related Requirements**:

* [FR-TENANT-004 (User Role Management)](../functional-requirements/tenant-admin.md#FR-TENANT-004)
* [FR-LOG-003 (Control Plane Auditing)](../functional-requirements/audit.md#FR-LOG-003)

<a id="UC-TENANT-USER-STATUS-UPDATE"></a>

## UC-TENANT-USER-STATUS-UPDATE User Status Update

**Actor**: [ACT-USER (Tenant User)](../actors/list.md#ACT-USER) (Role: Owner, Administrator)

**Description**:
The [ACT-USER (Tenant User)](../actors/list.md#ACT-USER) (Role: Owner or Administrator) changes the status of a user (e.g., to Disabled to block access).

**Trigger**:
The [ACT-USER (Tenant User)](../actors/list.md#ACT-USER) selects "Disable User" or "Enable User" in the **Tenant Administration Console**.

**Preconditions**:

1. The [ACT-USER (Tenant User)](../actors/list.md#ACT-USER) is logged in with sufficient privileges.
2. Target user exists.

**Postconditions**:

1. Target user's status is updated.
2. If Disabled, all active [DAT-SESSION (User Sessions)](../data-model/schema.md#DAT-SESSION) for the user are invalidated.

**Scenario**:

1. The [ACT-USER (Tenant User)](../actors/list.md#ACT-USER) selects the user to update.
2. The [ACT-USER (Tenant User)](../actors/list.md#ACT-USER) toggles the status (e.g., Active to Disabled).
3. The [ACT-USER (Tenant User)](../actors/list.md#ACT-USER) saves the changes.
4. The [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP) validates the action.
5. The [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP) updates the user record.
6. The [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP) invalidates sessions if required.

**Related Requirements**:

* [FR-TENANT-006 (User Status Management)](../functional-requirements/tenant-admin.md#FR-TENANT-006)
* [FR-LOG-003 (Control Plane Auditing)](../functional-requirements/audit.md#FR-LOG-003)

<a id="UC-TENANT-SESSION-REVOKE"></a>

## UC-TENANT-SESSION-REVOKE Session Revocation

**Actor**: [ACT-USER (Tenant User)](../actors/list.md#ACT-USER) (Role: Owner, Administrator)

**Description**:
The [ACT-USER (Tenant User)](../actors/list.md#ACT-USER) (Role: Owner or Administrator) invalidates a specific user's active sessions to force re-authentication.

**Trigger**:
The [ACT-USER (Tenant User)](../actors/list.md#ACT-USER) selects "Revoke Sessions" for a user in the **Tenant Administration Console**.

**Preconditions**:

1. The [ACT-USER (Tenant User)](../actors/list.md#ACT-USER) is logged in with sufficient privileges.
2. The target [DAT-USER (Users)](../data-model/schema.md#DAT-USER) exists.

**Postconditions**:

1. All active [DAT-SESSION (User Sessions)](../data-model/schema.md#DAT-SESSION) for the target User are invalidated.
2. The target User is required to log in again.

**Scenario**:

1. The [ACT-USER (Tenant User)](../actors/list.md#ACT-USER) identifies the target user in the **Tenant Administration Console**.
2. The [ACT-USER (Tenant User)](../actors/list.md#ACT-USER) initiates the session revocation.
3. The [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP) invalidates all tokens associated with the user.

**Related Requirements**:

* [FR-AUTH-005 (Session Management)](../functional-requirements/auth.md#FR-AUTH-005)
* [FR-LOG-003 (Control Plane Auditing)](../functional-requirements/audit.md#FR-LOG-003)

<a id="UC-TENANT-INVITE"></a>

## UC-TENANT-INVITE User Invitation

**Actor**: [ACT-USER (Tenant User)](../actors/list.md#ACT-USER) (Role: Owner, Administrator)

**Description**:
The [ACT-USER (Tenant User)](../actors/list.md#ACT-USER) (Role: Owner or Administrator) invites a new user to join their tenant organization. The invited user receives an email to set up their account.

**Trigger**:
The [ACT-USER (Tenant User)](../actors/list.md#ACT-USER) selects "Invite User" in the **Tenant Administration Console**.

**Preconditions**:

1. The [ACT-USER (Tenant User)](../actors/list.md#ACT-USER) is logged in with Owner or Administrator role.
2. The invited email address does not already exist in the tenant.

**Postconditions**:

1. An invitation email is sent to the specified address.
2. A user record is created with "Invited" status.

**Scenario**:

1. The [ACT-USER (Tenant User)](../actors/list.md#ACT-USER) enters the email address and role (Admin or User) of the new user.
2. The [ACT-USER (Tenant User)](../actors/list.md#ACT-USER) submits the invitation.
3. The [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP) validates the input and permissions.
4. The [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP) sends the invitation email.

**Related Requirements**:

* [FR-TENANT-001 (User Invitation)](../functional-requirements/tenant-admin.md#FR-TENANT-001)
* [FR-LOG-003 (Control Plane Auditing)](../functional-requirements/audit.md#FR-LOG-003)

<a id="UC-TENANT-INVITE-RESEND"></a>

## UC-TENANT-INVITE-RESEND Invitation Resend

**Actor**: [ACT-USER (Tenant User)](../actors/list.md#ACT-USER) (Role: Owner or Administrator)

**Description**:
The [ACT-USER (Tenant User)](../actors/list.md#ACT-USER) resends an invitation to a user whose previous invitation expired or was not received.

**Trigger**:
The [ACT-USER (Tenant User)](../actors/list.md#ACT-USER) selects "Resend Invitation" for a pending invitation.

**Preconditions**:

1. The [ACT-USER (Tenant User)](../actors/list.md#ACT-USER) is logged in with Owner or Administrator role.
2. A pending or expired invitation exists for the target user.

**Postconditions**:

1. The previous invitation is invalidated.
2. A new invitation with fresh expiration is created.
3. A new invitation email is sent to the user.

**Scenario**:

1. The [ACT-USER (Tenant User)](../actors/list.md#ACT-USER) views the list of pending invitations.
2. The [ACT-USER (Tenant User)](../actors/list.md#ACT-USER) selects "Resend" for the target user.
3. The [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP) invalidates the old invitation.
4. The [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP) creates a new invitation and sends the email.

**Related Requirements**:

* [FR-TENANT-007 (Invitation Resend)](../functional-requirements/tenant-admin.md#FR-TENANT-007)
* [FR-LOG-003 (Control Plane Auditing)](../functional-requirements/audit.md#FR-LOG-003)

<a id="UC-TENANT-SSO"></a>

## UC-TENANT-SSO SSO Configuration

**Actor**: [ACT-USER (Tenant User)](../actors/list.md#ACT-USER) (Role: Owner)

**Description**:
The [ACT-USER (Tenant User)](../actors/list.md#ACT-USER) (Role: Owner) configures an external Identity Provider (OIDC) to enable Single Sign-On for their users.

**Trigger**:
The [ACT-USER (Tenant User)](../actors/list.md#ACT-USER) initiates "SSO Setup" in the **Tenant Administration Console**.

**Preconditions**:

1. The [ACT-USER (Tenant User)](../actors/list.md#ACT-USER) is logged in with Owner role.
2. The [ACT-USER (Tenant User)](../actors/list.md#ACT-USER) has the necessary metadata (Client ID, Issuer URL) from their IdP.

**Postconditions**:

1. The tenant is configured to use the specified IdP.
2. Subsequent logins from this tenant's domain can use SSO.

**Scenario**:

1. The [ACT-USER (Tenant User)](../actors/list.md#ACT-USER) enters IdP details (Issuer URL, Client ID, Client Secret).
2. The [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP) verifies the IdP configuration (discovery).
3. The [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP) saves the configuration.

**Related Requirements**:

* [FR-AUTH-003 (Tenant SSO Configuration)](../functional-requirements/auth.md#FR-AUTH-003)
* [FR-LOG-003 (Control Plane Auditing)](../functional-requirements/audit.md#FR-LOG-003)

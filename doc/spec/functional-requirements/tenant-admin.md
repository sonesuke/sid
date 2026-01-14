# Tenant Administration

<a id="FR-TENANT-001"></a>

## FR-TENANT-001 User Invitation

The [TERM-SYS-CP](../terminology/definitions.md#TERM-SYS-CP) SHALL allow Tenant Owners and Administrators to invite new [Users](../data-model/schema.md#DAT-USER) to their [Tenant](../data-model/schema.md#DAT-TENANT).
This process SHALL create a [User Invitation](../data-model/schema.md#DAT-INVITE) record.

* Invitations SHALL have a configurable expiration period (default: 7 days).
* Expired invitations SHALL be marked as invalid and cannot be used for registration.

**Realized by**:

* [Tenant Administration Console](../interface-requirements/ui.md#IF-TENANT-CONSOLE)

**Quality Attributes**:

* [Encryption in Transit](../non-functional-requirements/security.md#NFR-SEC-001)
* [Least Privilege](../non-functional-requirements/security.md#NFR-SEC-005)
* [User Scalability](../non-functional-requirements/capacity.md#NFR-CAP-002)
* [Availability SLO](../non-functional-requirements/availability.md#NFR-OPS-001)

**Error Conditions**:

* [Access Denied](../error-handling/auth.md#ERR-AUTH-403)
* [Conflict](../error-handling/validation.md#ERR-VAL-409)
* [Business Rule Violation](../error-handling/validation.md#ERR-VAL-422)

<a id="FR-TENANT-002"></a>

### FR-TENANT-002 User Deletion

The [TERM-SYS-CP](../terminology/definitions.md#TERM-SYS-CP) SHALL allow Tenant Owners and Administrators to delete [Users](../data-model/schema.md#DAT-USER) from their [Tenant](../data-model/schema.md#DAT-TENANT).
When a user is deleted, the system SHALL invalidate all active [Sessions](../data-model/schema.md#DAT-SESSION) for that user.

**Realized by**:

* [Tenant Administration Console](../interface-requirements/ui.md#IF-TENANT-CONSOLE)

**Quality Attributes**:

* [Encryption in Transit](../non-functional-requirements/security.md#NFR-SEC-001)
* [Encryption at Rest](../non-functional-requirements/security.md#NFR-SEC-002)
* [Least Privilege](../non-functional-requirements/security.md#NFR-SEC-005)
* [Availability SLO](../non-functional-requirements/availability.md#NFR-OPS-001)

**Error Conditions**:

* [Access Denied](../error-handling/auth.md#ERR-AUTH-403)
* [Resource Not Found](../error-handling/resource.md#ERR-RES-404)

<a id="FR-TENANT-003"></a>

#### FR-TENANT-003 Contract Modification

The [TERM-SYS-CP](../terminology/definitions.md#TERM-SYS-CP) SHALL allow only Tenant Owners to modify the tenant's subscription contract (specifically [Tenant.plan](../data-model/schema.md#DAT-TENANT)).

**Realized by**:

* [Tenant Administration Console](../interface-requirements/ui.md#IF-TENANT-CONSOLE)

**Quality Attributes**:

* [Encryption in Transit](../non-functional-requirements/security.md#NFR-SEC-001)
* [Least Privilege](../non-functional-requirements/security.md#NFR-SEC-005)
* [Tenant Scalability](../non-functional-requirements/capacity.md#NFR-CAP-001)
* [Availability SLO](../non-functional-requirements/availability.md#NFR-OPS-001)

**Error Conditions**:

* [Access Denied](../error-handling/auth.md#ERR-AUTH-403)

<a id="FR-TENANT-004"></a>

#### FR-TENANT-004 User Role Management

The [TERM-SYS-CP](../terminology/definitions.md#TERM-SYS-CP) SHALL allow Tenant Owners and Administrators to modify the [Roles](../data-model/schema.md#DAT-ROLE) of existing [Users](../data-model/schema.md#DAT-USER) within their [Tenant](../data-model/schema.md#DAT-TENANT).
When a role is updated, the system SHALL invalidate all active [Sessions](../data-model/schema.md#DAT-SESSION) for the target user.

**Realized by**:

* [Tenant Administration Console](../interface-requirements/ui.md#IF-TENANT-CONSOLE)

**Quality Attributes**:

* [Encryption in Transit](../non-functional-requirements/security.md#NFR-SEC-001)
* [Least Privilege](../non-functional-requirements/security.md#NFR-SEC-005)
* [Availability SLO](../non-functional-requirements/availability.md#NFR-OPS-001)

**Error Conditions**:

* [Access Denied](../error-handling/auth.md#ERR-AUTH-403)
* [Resource Not Found](../error-handling/resource.md#ERR-RES-404)

<a id="FR-TENANT-006"></a>

#### FR-TENANT-006 User Status Management

The [TERM-SYS-CP](../terminology/definitions.md#TERM-SYS-CP) SHALL allow Tenant Owners and Administrators to modify the [Status](../data-model/schema.md#DAT-USER) of existing [Users](../data-model/schema.md#DAT-USER) (e.g., Enable, Disable).
When a user is Disabled, the system SHALL invalidate all active [Sessions](../data-model/schema.md#DAT-SESSION) for that user.

**Realized by**:

* [Tenant Administration Console](../interface-requirements/ui.md#IF-TENANT-CONSOLE)

**Quality Attributes**:

* [Encryption in Transit](../non-functional-requirements/security.md#NFR-SEC-001)
* [Least Privilege](../non-functional-requirements/security.md#NFR-SEC-005)
* [Availability SLO](../non-functional-requirements/availability.md#NFR-OPS-001)

**Error Conditions**:

* [Access Denied](../error-handling/auth.md#ERR-AUTH-403)
* [Resource Not Found](../error-handling/resource.md#ERR-RES-404)

<a id="FR-TENANT-007"></a>

#### FR-TENANT-007 Invitation Resend

The [TERM-SYS-CP](../terminology/definitions.md#TERM-SYS-CP) SHALL allow Tenant Owners and Administrators to resend an invitation to a user whose invitation has expired or was not received.

* Resending SHALL invalidate the previous [User Invitation](../data-model/schema.md#DAT-INVITE) and create a new one.
* The new invitation SHALL have a fresh expiration period.

**Realized by**:

* [Tenant Administration Console](../interface-requirements/ui.md#IF-TENANT-CONSOLE)

**Quality Attributes**:

* [Encryption in Transit](../non-functional-requirements/security.md#NFR-SEC-001)
* [Least Privilege](../non-functional-requirements/security.md#NFR-SEC-005)
* [Availability SLO](../non-functional-requirements/availability.md#NFR-OPS-001)

**Error Conditions**:

* [Access Denied](../error-handling/auth.md#ERR-AUTH-403)
* [Resource Not Found](../error-handling/resource.md#ERR-RES-404)

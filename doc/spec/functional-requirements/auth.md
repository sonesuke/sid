# Authentication & Authorization

<a id="FR-AUTH-001"></a>

#### FR-AUTH-001 Supported Authentication Methods
The [TERM-SYS-CP](../terminology/definitions.md#TERM-SYS-CP) SHALL support the following authentication methods for [Tenant Users ](../data-model/schema.md#DAT-USER):

*   OpenID Connect (OIDC)
*   Password-based authentication

**Realized by**:

*   [Universal Login Page ](../interface-requirements/ui.md#IF-LOGIN-UI)

**Quality Attributes**:

*   [Encryption in Transit ](../non-functional-requirements/security.md#NFR-SEC-001)
*   [MFA ](../non-functional-requirements/security.md#NFR-SEC-003)
*   [Least Privilege ](../non-functional-requirements/security.md#NFR-SEC-005)
*   [Adaptive Authentication ](../non-functional-requirements/security.md#NFR-SEC-006)
*   [Availability SLO ](../non-functional-requirements/availability.md#NFR-OPS-001)

**Error Conditions**:

*   [Invalid Credentials ](../error-handling/auth.md#ERR-AUTH-401)
*   [MFA Required ](../error-handling/auth.md#ERR-AUTH-461)
*   [Rate Limit Exceeded ](../error-handling/rate-limit.md#ERR-RATE-429)

<a id="FR-AUTH-003"></a>

#### FR-AUTH-003 Tenant SSO Configuration
The [TERM-SYS-CP](../terminology/definitions.md#TERM-SYS-CP) SHALL allow a Tenant Owner (role of [ACT-USER](../actors/list.md#ACT-USER), see [DAT-ROLE](../data-model/schema.md#DAT-ROLE)) to register an external Identity Provider (IdP) for Single Sign-On (SSO).
The configuration SHALL be stored in [SSO Configuration ](../data-model/schema.md#DAT-SSO-CONFIG).

**Realized by**:

*   [Tenant Administration Console ](../interface-requirements/ui.md#IF-TENANT-CONSOLE)

**Quality Attributes**:

*   [Encryption in Transit ](../non-functional-requirements/security.md#NFR-SEC-001)
*   [Key Management ](../non-functional-requirements/security.md#NFR-SEC-004)
*   [Least Privilege ](../non-functional-requirements/security.md#NFR-SEC-005)
*   [Availability SLO ](../non-functional-requirements/availability.md#NFR-OPS-001)

**Error Conditions**:

*   [Access Denied ](../error-handling/auth.md#ERR-AUTH-403)
*   [Invalid Input ](../error-handling/validation.md#ERR-VAL-400)
*   [Conflict ](../error-handling/validation.md#ERR-VAL-409)

<a id="FR-AUTH-004"></a>

#### FR-AUTH-004 Password Reset
The [TERM-SYS-CP](../terminology/definitions.md#TERM-SYS-CP) SHALL allow [Tenant Users ](../data-model/schema.md#DAT-USER) (using password authentication) to request a password reset via their registered email address.
The [TERM-SYS-CP](../terminology/definitions.md#TERM-SYS-CP) SHALL allow authenticated [Tenant Users ](../data-model/schema.md#DAT-USER) to change their password.
Upon successful password reset or change, the system SHALL invalidate all active [Sessions ](../data-model/schema.md#DAT-SESSION) for the user.

**Realized by**:

*   [Universal Login Page ](../interface-requirements/ui.md#IF-LOGIN-UI)

**Quality Attributes**:

*   [Encryption in Transit ](../non-functional-requirements/security.md#NFR-SEC-001)
*   [MFA ](../non-functional-requirements/security.md#NFR-SEC-003)
*   [Key Management ](../non-functional-requirements/security.md#NFR-SEC-004)
*   [Availability SLO ](../non-functional-requirements/availability.md#NFR-OPS-001)

**Error Conditions**:

*   [Invalid Credentials ](../error-handling/auth.md#ERR-AUTH-401)
*   [Business Rule Violation ](../error-handling/validation.md#ERR-VAL-422)
*   [Rate Limit Exceeded ](../error-handling/rate-limit.md#ERR-RATE-429)

<a id="FR-AUTH-005"></a>

#### FR-AUTH-005 Session Management
The [TERM-SYS-CP](../terminology/definitions.md#TERM-SYS-CP) SHALL establish a [Session ](../data-model/schema.md#DAT-SESSION) upon successful user authentication.
The [TERM-SYS-CP](../terminology/definitions.md#TERM-SYS-CP) SHALL support session invalidation triggers including explicit logout and administrative revocation.

**Realized by**:

*   [Universal Login Page ](../interface-requirements/ui.md#IF-LOGIN-UI)
*   [Tenant Administration Console ](../interface-requirements/ui.md#IF-TENANT-CONSOLE)

**Quality Attributes**:

*   [Encryption in Transit ](../non-functional-requirements/security.md#NFR-SEC-001)
*   [Encryption at Rest ](../non-functional-requirements/security.md#NFR-SEC-002)
*   [Least Privilege ](../non-functional-requirements/security.md#NFR-SEC-005)
*   [Availability SLO ](../non-functional-requirements/availability.md#NFR-OPS-001)

**Error Conditions**:

*   [Access Denied ](../error-handling/auth.md#ERR-AUTH-403)
*   [Session Expired ](../error-handling/auth.md#ERR-AUTH-440)

<a id="FR-AUTH-006"></a>

#### FR-AUTH-006 Password Policy Configuration
The [TERM-SYS-CP](../terminology/definitions.md#TERM-SYS-CP) SHALL allow each [Tenant ](../data-model/schema.md#DAT-TENANT) to configure password complexity requirements (e.g., minimum length, required character types).

**Constrained by**: [CON-SEC-001](../constraints-and-assumptions/index.md#CON-SEC-001)

**Realized by**:

*   [Tenant Administration Console ](../interface-requirements/ui.md#IF-TENANT-CONSOLE)

**Quality Attributes**:

*   [Encryption in Transit ](../non-functional-requirements/security.md#NFR-SEC-001)
*   [Encryption at Rest ](../non-functional-requirements/security.md#NFR-SEC-002)
*   [Least Privilege ](../non-functional-requirements/security.md#NFR-SEC-005)
*   [Availability SLO ](../non-functional-requirements/availability.md#NFR-OPS-001)

**Error Conditions**:

*   [Access Denied ](../error-handling/auth.md#ERR-AUTH-403)
*   [Invalid Input ](../error-handling/validation.md#ERR-VAL-400)

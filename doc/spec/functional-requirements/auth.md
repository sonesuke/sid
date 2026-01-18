# Authentication & Authorization

<a id="FR-AUTH-001"></a>

## FR-AUTH-001 Supported Authentication Methods

The [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP) SHALL support the following authentication methods for [DAT-USER (Users)](../data-model/schema.md#DAT-USER):

* OpenID Connect (OIDC)
* Password-based authentication

**Realized by**:

* [IF-LOGIN-UI (Universal Login Page)](../interface-requirements/ui.md#IF-LOGIN-UI)

**Quality Attributes**:

* [NFR-SEC-001 (Encryption in Transit)](../non-functional-requirements/security.md#NFR-SEC-001)
* [NFR-SEC-003 (Multi-Factor Authentication)](../non-functional-requirements/security.md#NFR-SEC-003)
* [NFR-SEC-005 (Least Privilege)](../non-functional-requirements/security.md#NFR-SEC-005)
* [NFR-SEC-006 (Adaptive Authentication)](../non-functional-requirements/security.md#NFR-SEC-006)
* [NFR-OPS-001 (Service Level Objective)](../non-functional-requirements/availability.md#NFR-OPS-001)

**Error Conditions**:

* [ERR-AUTH-401 (Invalid Credentials)](../error-handling/auth.md#ERR-AUTH-401)
* [ERR-AUTH-461 (MFA Required)](../error-handling/auth.md#ERR-AUTH-461)
* [ERR-RATE-429 (Rate Limit Exceeded)](../error-handling/rate-limit.md#ERR-RATE-429)

<a id="FR-AUTH-003"></a>

### FR-AUTH-003 Tenant SSO Configuration

The [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP) SHALL allow a Tenant Owner (role of [ACT-USER (Tenant User)](../actors/tenant-user.md#ACT-USER), see [DAT-ROLE (Roles)](../data-model/schema.md#DAT-ROLE)) to register an external Identity Provider (IdP) for Single Sign-On (SSO).
The configuration SHALL be stored in [DAT-SSO-CONFIG (SSO Configuration)](../data-model/schema.md#DAT-SSO-CONFIG).

**Realized by**:

* [IF-TENANT-CONSOLE (Tenant Administration Console)](../interface-requirements/ui.md#IF-TENANT-CONSOLE)

**Quality Attributes**:

* [NFR-SEC-001 (Encryption in Transit)](../non-functional-requirements/security.md#NFR-SEC-001)
* [NFR-SEC-004 (Key Management)](../non-functional-requirements/security.md#NFR-SEC-004)
* [NFR-SEC-005 (Least Privilege)](../non-functional-requirements/security.md#NFR-SEC-005)
* [NFR-OPS-001 (Service Level Objective)](../non-functional-requirements/availability.md#NFR-OPS-001)

**Error Conditions**:

* [ERR-AUTH-403 (Access Denied)](../error-handling/auth.md#ERR-AUTH-403)
* [ERR-VAL-400 (Invalid Input)](../error-handling/validation.md#ERR-VAL-400)
* [ERR-VAL-409 (Conflict)](../error-handling/validation.md#ERR-VAL-409)

<a id="FR-AUTH-004"></a>

#### FR-AUTH-004 Password Reset

The [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP) SHALL allow [DAT-USER (Users)](../data-model/schema.md#DAT-USER) (using password authentication) to request a password reset via their registered email address.
The [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP) SHALL allow authenticated [DAT-USER (Users)](../data-model/schema.md#DAT-USER) to change their password.
Upon successful password reset or change, the system SHALL invalidate all active [DAT-SESSION (User Sessions)](../data-model/schema.md#DAT-SESSION) for the user.

**Realized by**:

* [IF-LOGIN-UI (Universal Login Page)](../interface-requirements/ui.md#IF-LOGIN-UI)

**Quality Attributes**:

* [NFR-SEC-001 (Encryption in Transit)](../non-functional-requirements/security.md#NFR-SEC-001)
* [NFR-SEC-003 (Multi-Factor Authentication)](../non-functional-requirements/security.md#NFR-SEC-003)
* [NFR-SEC-004 (Key Management)](../non-functional-requirements/security.md#NFR-SEC-004)
* [NFR-OPS-001 (Service Level Objective)](../non-functional-requirements/availability.md#NFR-OPS-001)

**Error Conditions**:

* [ERR-AUTH-401 (Invalid Credentials)](../error-handling/auth.md#ERR-AUTH-401)
* [ERR-VAL-422 (Business Rule Violation)](../error-handling/validation.md#ERR-VAL-422)
* [ERR-RATE-429 (Rate Limit Exceeded)](../error-handling/rate-limit.md#ERR-RATE-429)

<a id="FR-AUTH-005"></a>

#### FR-AUTH-005 Session Management

The [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP) SHALL establish a [DAT-SESSION (User Sessions)](../data-model/schema.md#DAT-SESSION) upon successful user authentication.
The [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP) SHALL support session invalidation triggers including explicit logout and administrative revocation.

**Realized by**:

* [IF-LOGIN-UI (Universal Login Page)](../interface-requirements/ui.md#IF-LOGIN-UI)
* [IF-TENANT-CONSOLE (Tenant Administration Console)](../interface-requirements/ui.md#IF-TENANT-CONSOLE)

**Quality Attributes**:

* [NFR-SEC-001 (Encryption in Transit)](../non-functional-requirements/security.md#NFR-SEC-001)
* [NFR-SEC-002 (Encryption at Rest)](../non-functional-requirements/security.md#NFR-SEC-002)
* [NFR-SEC-005 (Least Privilege)](../non-functional-requirements/security.md#NFR-SEC-005)
* [NFR-OPS-001 (Service Level Objective)](../non-functional-requirements/availability.md#NFR-OPS-001)

**Error Conditions**:

* [ERR-AUTH-403 (Access Denied)](../error-handling/auth.md#ERR-AUTH-403)
* [ERR-AUTH-440 (Session Expired)](../error-handling/auth.md#ERR-AUTH-440)

<a id="FR-AUTH-006"></a>

#### FR-AUTH-006 Password Policy Configuration

The [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP) SHALL allow each [DAT-TENANT (Tenants)](../data-model/schema.md#DAT-TENANT) to configure password complexity requirements (e.g., minimum length, required character types).

**Constrained by**: [CON-SEC-001 (Configurable Password Policy)](../constraints-and-assumptions/index.md#CON-SEC-001)

**Realized by**:

* [IF-TENANT-CONSOLE (Tenant Administration Console)](../interface-requirements/ui.md#IF-TENANT-CONSOLE)

**Quality Attributes**:

* [NFR-SEC-001 (Encryption in Transit)](../non-functional-requirements/security.md#NFR-SEC-001)
* [NFR-SEC-002 (Encryption at Rest)](../non-functional-requirements/security.md#NFR-SEC-002)
* [NFR-SEC-005 (Least Privilege)](../non-functional-requirements/security.md#NFR-SEC-005)
* [NFR-OPS-001 (Service Level Objective)](../non-functional-requirements/availability.md#NFR-OPS-001)

**Error Conditions**:

* [ERR-AUTH-403 (Access Denied)](../error-handling/auth.md#ERR-AUTH-403)
* [ERR-VAL-400 (Invalid Input)](../error-handling/validation.md#ERR-VAL-400)

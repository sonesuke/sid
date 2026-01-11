Authentication & Authorization
==============================

.. _FR-AUTH-001:

FR-AUTH-001 Supported Authentication Methods
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The :ref:`TERM-SYS-CP` SHALL support the following authentication methods for :ref:`Tenant Users <DAT-USER>`:

*   OpenID Connect (OIDC)
*   Password-based authentication

**Realized by**: :ref:`Universal Login Page <IF-LOGIN-UI>`

.. _FR-AUTH-003:

FR-AUTH-003 Tenant SSO Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The :ref:`TERM-SYS-CP` SHALL allow a Tenant Owner (role of :ref:`ACT-USER`, see :ref:`DAT-ROLE`) to register an external Identity Provider (IdP) for Single Sign-On (SSO).
The configuration SHALL be stored in :ref:`SSO Configuration <DAT-SSO-CONFIG>`.
**Realized by**: :ref:`Tenant Administration Console <IF-TENANT-CONSOLE>`

.. _FR-AUTH-004:

FR-AUTH-004 Password Reset
^^^^^^^^^^^^^^^^^^^^^^^^^^
The :ref:`TERM-SYS-CP` SHALL allow :ref:`Tenant Users <DAT-USER>` (using password authentication) to request a password reset via their registered email address.
The :ref:`TERM-SYS-CP` SHALL allow authenticated :ref:`Tenant Users <DAT-USER>` to change their password.
Upon successful password reset or change, the system SHALL invalidate all active :ref:`Sessions <DAT-SESSION>` for the user.

**Realized by**: :ref:`Universal Login Page <IF-LOGIN-UI>`

.. _FR-AUTH-005:

FR-AUTH-005 Session Management
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The :ref:`TERM-SYS-CP` SHALL establish a :ref:`Session <DAT-SESSION>` upon successful user authentication.
The :ref:`TERM-SYS-CP` SHALL support session invalidation triggers including explicit logout and administrative revocation.

**Realized by**: :ref:`Universal Login Page <IF-LOGIN-UI>`, :ref:`Tenant Administration Console <IF-TENANT-CONSOLE>`

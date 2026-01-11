Security
========

.. _NFR-SEC-001:

NFR-SEC-001 Encryption in Transit
---------------------------------
All network communications SHALL use TLS 1.2 or higher.

**Constrained by**: :ref:`CON-SEC-003`

.. _NFR-SEC-002:

NFR-SEC-002 Encryption at Rest
------------------------------
All persistent data SHALL be encrypted using AES-256 or equivalent algorithm.

**Constrained by**: :ref:`CON-SEC-004`

.. _NFR-SEC-003:

NFR-SEC-003 Multi-Factor Authentication
---------------------------------------
The system SHALL support Multi-Factor Authentication (MFA) for user login.
MFA options SHALL include TOTP (Time-based One-Time Password) and WebAuthn.

**Rationale**: NIST CSF 2.0 - Strong authentication.

.. _NFR-SEC-004:

NFR-SEC-004 Key Management
--------------------------
The system SHALL implement secure key management practices including:

*   Automated key generation using cryptographically secure methods.
*   Periodic key rotation (at least annually).
*   Secure key destruction upon expiration or revocation.

**Rationale**: NIST CSF 2.0 - Data protection.

.. _NFR-SEC-005:

NFR-SEC-005 Least Privilege
---------------------------
The system SHALL enforce the principle of least privilege:

*   Users and services SHALL be granted only the minimum permissions required.
*   Separation of duties SHALL be implemented for sensitive operations.

**Rationale**: NIST CSF 2.0 - Access control.

.. _NFR-SEC-006:

NFR-SEC-006 Adaptive Authentication
-----------------------------------
The system SHOULD implement adaptive (risk-based) authentication that considers:

*   User location and device.
*   Time of access.
*   Behavioral patterns.

When elevated risk is detected, additional authentication factors SHALL be required.

**Rationale**: NIST CSF 2.0 - Context-aware security.

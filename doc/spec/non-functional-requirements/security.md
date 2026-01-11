# Security

<a id="NFR-SEC-001"></a>

## NFR-SEC-001 Encryption in Transit
All network communications SHALL use TLS 1.2 or higher.

**Constrained by**: [CON-SEC-003](../constraints-and-assumptions/index.md#CON-SEC-003)

<a id="NFR-SEC-002"></a>

## NFR-SEC-002 Encryption at Rest
All persistent data SHALL be encrypted using AES-256 or equivalent algorithm.

**Constrained by**: [CON-SEC-004](../constraints-and-assumptions/index.md#CON-SEC-004)

<a id="NFR-SEC-003"></a>

## NFR-SEC-003 Multi-Factor Authentication
The system SHALL support Multi-Factor Authentication (MFA) for user login.
MFA options SHALL include TOTP (Time-based One-Time Password) and WebAuthn.

**Constrained by**: [CON-SEC-005](../constraints-and-assumptions/index.md#CON-SEC-005)

<a id="NFR-SEC-004"></a>

## NFR-SEC-004 Key Management
The system SHALL implement secure key management practices including:

*   Automated key generation using cryptographically secure methods.
*   Periodic key rotation (at least annually).
*   Secure key destruction upon expiration or revocation.

**Constrained by**: [CON-SEC-006](../constraints-and-assumptions/index.md#CON-SEC-006)

<a id="NFR-SEC-005"></a>

## NFR-SEC-005 Least Privilege
The system SHALL enforce the principle of least privilege:

*   Users and services SHALL be granted only the minimum permissions required.
*   Separation of duties SHALL be implemented for sensitive operations.

**Constrained by**: [CON-SEC-007](../constraints-and-assumptions/index.md#CON-SEC-007)

<a id="NFR-SEC-006"></a>

## NFR-SEC-006 Adaptive Authentication
The system SHOULD implement adaptive (risk-based) authentication that considers:

*   User location and device.
*   Time of access.
*   Behavioral patterns.

When elevated risk is detected, additional authentication factors SHALL be required.

**Constrained by**: [CON-SEC-008](../constraints-and-assumptions/index.md#CON-SEC-008)

# [ADR-AUTH-001] Authentication Method Implementation

## Context and Problem Statement

We need to define *how* authentication is implemented. Specifically, the mechanism for transmitting identity and validating it across the Control Plane and Managed Apps.

### Decision Drivers
* Security standards compliance (OAuth2 / OIDC)
* Statelessness
* Compatibility with SPA / Mobile clients
* Ease of revocation

## Considered Options
* JWT (JSON Web Tokens) - Access/Refresh Token pattern
* Server-side Code Sessions (Cookie-based)
* API Keys (for M2M only)

## Decision Outcome

### Positive Consequences
* Stateless verification by services
* Standardized (OIDC compatible)

### Negative Consequences
* Token revocation complexity
* Token size

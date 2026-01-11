Cross-cutting Concepts
======================

This section describes the **Design Constitution**: the permanent rules and principles that apply across all architectural building blocks.

Authentication and Authorization
--------------------------------
*Delegate identity management to specialized providers.*

*   **Rule**: Authentication SHALL be delegated to an External Identity Provider (OIDC compliant).
    *   **Decision**: :doc:`../../adr/0007-authentication-provider` (Azure Entra ID).
*   **Rule**: Services SHALL be Stateless. Trust Identity/Access Tokens (JWT) verified via public keys.
*   **Rule**: Authorization SHALL use a Role + Scope model.
    *   **Role**: Coarse-grained access (e.g., `TenantAdmin`, `User`).
    *   **Scope**: Fine-grained permissions (e.g., `billing:read`).

Error Handling
--------------
*Consistent error reporting for machine and human consumption.*

*   **Rule**: Internal exceptions SHALL be mapped to standard HTTP error codes.
*   **Rule**: Business Errors (e.g., "Insufficient Funds") SHALL be distinguished from System Errors (e.g., "DB Connection Failed").
*   **Rule**: Internal stack traces SHALL NOT be exposed in API responses (Security).
*   **Rule**: All errors SHALL follow standard JSON Problem Details format (RFC 7807).

Logging and Auditing
--------------------
*Traceability across the distributed system.*

*   **Rule**: A **Correlation ID** is MANDATORY for all internal and external requests. It MUST be propagated across service boundaries.
    *   Satisfies :ref:`Continuous Monitoring <NFR-MON-001>` (Distributed Tracing).
*   **Rule**: Personally Identifiable Information (PII) SHALL NOT be logged.
*   **Rule**: Security events (login, permission changes) SHALL be emitted to the Audit Log.

Security
--------
*Identity as the new perimeter.*

*   **Rule**: Zero Trust Model. Do not rely on network perimeter (VPC) for security.
    *   **Decision**: :doc:`../../adr/0008-network-strategy` (No VPC).
*   **Rule**: TLS 1.2+ is MANDATORY for all data in transit, including internal service-to-service communication.
    *   Satisfies :ref:`Encryption in Transit <NFR-SEC-001>`.
*   **Rule**: Secrets SHALL be injected at runtime (e.g., via environment variables) and NEVER checked into source code.

Data and Transaction
--------------------
*Resilience over strict consistency.*

*   **Rule**: Write operations SHALL be **Idempotent** to allow safe retries.
*   **Rule**: **Eventual Consistency** is accepted. Distributed Transactions (2PC) are PROHIBITED.
    *   Use Event Sourcing / Saga patterns where cross-domain consistency is required.

API Design
----------
*Standardized interfaces.*

*   **Rule**: APIs SHALL follow REST principles and use JSON as the data format.
*   **Rule**: API versioning strategy SHALL avoid breaking changes (prefer backwards-compatible additions).

Observability
-------------
*Measure what matters.*

*   **Rule**: Monitoring SHALL be driven by Service Level Indicators (SLIs) and Service Level Objectives (SLOs).
    *   Satisfies :ref:`Service Level Objective <NFR-OPS-001>`.
*   **Rule**: Metrics SHALL follow the RED method (Rate, Errors, Duration).

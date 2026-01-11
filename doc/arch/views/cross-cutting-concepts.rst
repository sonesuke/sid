Cross-cutting Concepts
======================

This section describes the **Design Constitution**: the permanent rules and principles that apply across all architectural building blocks.

Authentication and Authorization
--------------------------------
*Delegate identity management to specialized providers.*

.. _CC-DEV-001:

Development Methodology
-----------------------
*AI Agents as primary developers.*

*   **Rule [CC-DEV-001]**: Technology selection SHALL prioritize **AI Proficiency** (accuracy of LLM code generation) and **Ecosystem Maturity** over human learning curves.
    *   **Decision**: :doc:`../../adr/decisions/language-runtime` (Python), :doc:`../../adr/decisions/iac-tool-selection` (Terraform).

Authentication and Authorization
--------------------------------

.. _CC-AUTH-001:

*   **Rule [CC-AUTH-001]**: Authentication SHALL be delegated to an External Identity Provider (OIDC compliant).
    *   **Decision**: :doc:`../../adr/decisions/authentication-provider` (Azure Entra ID).
    *   **Root**:

        *   :ref:`FR-AUTH-001` (Auth Methods)

.. _CC-AUTH-002:

*   **Rule [CC-AUTH-002]**: Services SHALL be Stateless. Trust Identity/Access Tokens (JWT) verified via public keys.
    *   **Root**:

        *   :ref:`NFR-CAP-002` (User Scalability)
        *   :ref:`NFR-PERF-001` (Auth Latency)

.. _CC-AUTH-003:

*   **Rule [CC-AUTH-003]**: Authorization SHALL use a Role + Scope model.
    *   **Role**: Coarse-grained access (e.g., `TenantAdmin`, `User`).
    *   **Scope**: Fine-grained permissions (e.g., `billing:read`).
    *   **Root**:

        *   :ref:`FR-AUTH-003` (SSO Config)
        *   :ref:`NFR-SEC-005` (Least Privilege)

Error Handling
--------------
*Consistent error reporting for machine and human consumption.*

.. _CC-ERR-001:

*   **Rule [CC-ERR-001]**: Internal exceptions SHALL be mapped to standard HTTP error codes.
    *   **Root**:

        *   :ref:`NFR-OPS-001` (Availability SLO)

.. _CC-ERR-002:

*   **Rule [CC-ERR-002]**: Business Errors (e.g., "Insufficient Funds") SHALL be distinguished from System Errors (e.g., "DB Connection Failed").

.. _CC-ERR-003:

*   **Rule [CC-ERR-003]**: Internal stack traces SHALL NOT be exposed in API responses (Security).
    *   **Root**:

        *   :ref:`NFR-SEC-001` (Information Leakage Prevention)

.. _CC-ERR-004:

*   **Rule [CC-ERR-004]**: All errors SHALL follow standard JSON Problem Details format (RFC 7807).

Logging and Auditing
--------------------
*Traceability across the distributed system.*

.. _CC-LOG-001:

*   **Rule [CC-LOG-001]**: A **Correlation ID** is MANDATORY for all internal and external requests. It MUST be propagated across service boundaries.
    *   **Decision**: :doc:`../../adr/decisions/communication-pattern`.
    *   **Root**:

        *   :ref:`NFR-MON-001` (Continuous Monitoring)

.. _CC-LOG-002:

*   **Rule [CC-LOG-002]**: Personally Identifiable Information (PII) SHALL NOT be logged.
    *   **Root**:

        *   :ref:`NFR-DATA-001` (Data Privacy)

.. _CC-LOG-003:

*   **Rule [CC-LOG-003]**: Security events (login, permission changes) SHALL be emitted to the Audit Log.
    *   **Root**:

        *   :ref:`FR-LOG-003` (Control Plane Auditing)

Security
--------
*Identity as the new perimeter.*

.. _CC-SEC-001:

*   **Rule [CC-SEC-001]**: Zero Trust Model. Do not rely on network perimeter (VPC) for security.
    *   **Decision**: :doc:`../../adr/network-strategy` (No VPC).
    *   **Root**:

        *   :ref:`NFR-SEC-005` (Least Privilege)

.. _CC-SEC-002:

*   **Rule [CC-SEC-002]**: TLS 1.2+ is MANDATORY for all data in transit, including internal service-to-service communication.
    *   **Decision**: :doc:`../../adr/network-strategy`.
    *   **Root**:

        *   :ref:`NFR-SEC-001` (Encryption in Transit)

.. _CC-SEC-003:

*   **Rule [CC-SEC-003]**: Secrets SHALL be injected at runtime (e.g., via environment variables) and NEVER checked into source code.
    *   **Root**:

        *   :ref:`NFR-SEC-004` (Key Management)

Data and Transaction
--------------------
*Resilience over strict consistency.*

.. _CC-DAT-001:

*   **Rule [CC-DAT-001]**: Write operations SHALL be **Idempotent** to allow safe retries.
    *   **Root**:

        *   :ref:`NFR-OPS-003` (Failover)

.. _CC-DAT-002:

*   **Rule [CC-DAT-002]**: **Eventual Consistency** is accepted. Distributed Transactions (2PC) are PROHIBITED.
    *   **Root**:

        *   :ref:`NFR-CAP-001` (Tenant Scalability)

API Design
----------
*Standardized interfaces.*

.. _CC-API-001:

*   **Rule [CC-API-001]**: APIs SHALL follow REST principles and use JSON as the data format.

.. _CC-API-002:

*   **Rule [CC-API-002]**: API versioning strategy SHALL avoid breaking changes (prefer backwards-compatible additions).

Observability
-------------
*Measure what matters.*

.. _CC-OBS-001:

*   **Rule [CC-OBS-001]**: Monitoring SHALL be driven by Service Level Indicators (SLIs) and Service Level Objectives (SLOs).
    *   **Root**:

        *   :ref:`NFR-OPS-001` (SLO)

.. _CC-OBS-002:

*   **Rule [CC-OBS-002]**: Metrics SHALL follow the RED method (Rate, Errors, Duration).
    *   **Root**:

        *   :ref:`NFR-MON-001` (Continuous Monitoring)

Deployment and Operations
-------------------------
*Minimize risk through reversibility and consistency.*

.. _CC-OPS-001:

*   **Rule [CC-OPS-001]**: Releases SHALL be **Reversible**.
    *   New deployments MUST NOT destructively alter the previous version's resources until the successful switchover is confirmed.
    *   **Decision**: :doc:`../../adr/decisions/deployment-strategy` (Blue-Green).
    *   **Root**:
        *   :ref:`NFR-OPS-002` (MTTR)

.. _CC-OPS-002:

*   **Rule [CC-OPS-002]**: Deployment Artifacts SHALL be **Immutable** (Build Once, Deploy Many).
    *   The same built artifact (container image, lambda zip) MUST be promoted from Staging to Production. Configuration is injected via environment variables.
    *   **Root**:
        *   :ref:`NFR-SEC-002` (Supply Chain Security)

    *   **Root**:
        *   :ref:`NFR-OPS-001` (Availability)

.. _CC-OPS-004:

*   **Rule [CC-OPS-004]**: CI/CD Pipelines SHALL be defined as Code (**Pipeline as Code**).
    *   Workflows MUST be versioned alongside the application code to ensure the build process evolves with the software.
    *   **Decision**: :doc:`../../adr/decisions/cicd-platform` (GitHub Actions).
    *   **Root**:
        *   :ref:`NFR-OPS-002` (MTTR - Revert of pipeline logic)


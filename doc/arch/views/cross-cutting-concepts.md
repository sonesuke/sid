# Cross-cutting Concepts

This section describes the **Design Constitution**: the permanent rules and principles that apply across all architectural building blocks.

## Authentication and Authorization
*Delegate identity management to specialized providers.*

<a id="CC-DEV-001"></a>

## Development Methodology
*AI Agents as primary developers.*

*   **Rule [CC-DEV-001]**: Technology selection SHALL prioritize **AI Proficiency** (accuracy of LLM code generation) and **Ecosystem Maturity** over human learning curves.
    *   **Decision**: [../../adr/decisions/language-runtime](../../adr/decisions/language-runtime.md) (Python), [../../adr/decisions/iac-tool-selection](../../adr/decisions/iac-tool-selection.md) (Terraform).

## Authentication and Authorization

<a id="CC-AUTH-001"></a>

*   **Rule [CC-AUTH-001]**: Authentication SHALL be delegated to an External Identity Provider (OIDC compliant).
    *   **Decision**: [../../adr/decisions/authentication-provider](../../adr/decisions/authentication-provider.md) (Azure Entra ID).
    *   **Root**:

        *   [FR-AUTH-001](../../spec/functional-requirements/auth.md#FR-AUTH-001) (Auth Methods)

<a id="CC-AUTH-002"></a>

*   **Rule [CC-AUTH-002]**: Services SHALL be Stateless. Trust Identity/Access Tokens (JWT) verified via public keys.
    *   **Root**:

        *   [NFR-CAP-002](../../spec/non-functional-requirements/capacity.md#NFR-CAP-002) (User Scalability)
        *   [NFR-PERF-001](../../spec/non-functional-requirements/performance.md#NFR-PERF-001) (Auth Latency)

<a id="CC-AUTH-003"></a>

*   **Rule [CC-AUTH-003]**: Authorization SHALL use a Role + Scope model.
    *   **Role**: Coarse-grained access (e.g., `TenantAdmin`, `User`).
    *   **Scope**: Fine-grained permissions (e.g., `billing:read`).
    *   **Root**:

        *   [FR-AUTH-003](../../spec/functional-requirements/auth.md#FR-AUTH-003) (SSO Config)
        *   [NFR-SEC-005](../../spec/non-functional-requirements/security.md#NFR-SEC-005) (Least Privilege)

## Error Handling
*Consistent error reporting for machine and human consumption.*

<a id="CC-ERR-001"></a>

*   **Rule [CC-ERR-001]**: Internal exceptions SHALL be mapped to standard HTTP error codes.
    *   **Root**:

        *   [NFR-OPS-001](../../spec/non-functional-requirements/availability.md#NFR-OPS-001) (Availability SLO)

<a id="CC-ERR-002"></a>

*   **Rule [CC-ERR-002]**: Business Errors (e.g., "Insufficient Funds") SHALL be distinguished from System Errors (e.g., "DB Connection Failed").

<a id="CC-ERR-003"></a>

*   **Rule [CC-ERR-003]**: Internal stack traces SHALL NOT be exposed in API responses (Security).
    *   **Root**:

        *   [NFR-SEC-001](../../spec/non-functional-requirements/security.md#NFR-SEC-001) (Information Leakage Prevention)

<a id="CC-ERR-004"></a>

*   **Rule [CC-ERR-004]**: All errors SHALL follow standard JSON Problem Details format (RFC 7807).

## Logging and Auditing
*Traceability across the distributed system.*

<a id="CC-LOG-001"></a>

*   **Rule [CC-LOG-001]**: A **Correlation ID** is MANDATORY for all internal and external requests. It MUST be propagated across service boundaries.
    *   **Decision**: [../../adr/decisions/communication-pattern](../../adr/decisions/communication-pattern.md).
    *   **Root**:

        *   [NFR-MON-001](../../spec/non-functional-requirements/monitoring.md#NFR-MON-001) (Continuous Monitoring)

<a id="CC-LOG-002"></a>

*   **Rule [CC-LOG-002]**: Personally Identifiable Information (PII) SHALL NOT be logged.
    *   **Root**:

        *   [NFR-DATA-001](../../spec/non-functional-requirements/data.md#NFR-DATA-001) (Data Privacy)

<a id="CC-LOG-003"></a>

*   **Rule [CC-LOG-003]**: Security events (login, permission changes) SHALL be emitted to the Audit Log.
    *   **Root**:

        *   [FR-LOG-003](../../spec/functional-requirements/audit.md#FR-LOG-003) (Control Plane Auditing)

## Security
*Identity as the new perimeter.*

<a id="CC-SEC-001"></a>

*   **Rule [CC-SEC-001]**: Zero Trust Model. Do not rely on network perimeter (VPC) for security.
    *   **Decision**: [../../adr/network-strategy](../../adr/network-strategy.md) (No VPC).
    *   **Root**:

        *   [NFR-SEC-005](../../spec/non-functional-requirements/security.md#NFR-SEC-005) (Least Privilege)

<a id="CC-SEC-002"></a>

*   **Rule [CC-SEC-002]**: TLS 1.2+ is MANDATORY for all data in transit, including internal service-to-service communication.
    *   **Decision**: [../../adr/network-strategy](../../adr/network-strategy.md).
    *   **Root**:

        *   [NFR-SEC-001](../../spec/non-functional-requirements/security.md#NFR-SEC-001) (Encryption in Transit)

<a id="CC-SEC-003"></a>

*   **Rule [CC-SEC-003]**: Secrets SHALL be injected at runtime (e.g., via environment variables) and NEVER checked into source code.
    *   **Root**:

        *   [NFR-SEC-004](../../spec/non-functional-requirements/security.md#NFR-SEC-004) (Key Management)

## Data and Transaction
*Resilience over strict consistency.*

<a id="CC-DAT-001"></a>

*   **Rule [CC-DAT-001]**: Write operations SHALL be **Idempotent** to allow safe retries.
    *   **Root**:

        *   [NFR-OPS-003](../../spec/non-functional-requirements/availability.md#NFR-OPS-003) (Failover)

<a id="CC-DAT-002"></a>

*   **Rule [CC-DAT-002]**: **Eventual Consistency** is accepted. Distributed Transactions (2PC) are PROHIBITED.
    *   **Root**:

        *   [NFR-CAP-001](../../spec/non-functional-requirements/capacity.md#NFR-CAP-001) (Tenant Scalability)

## API Design
*Standardized interfaces.*

<a id="CC-API-001"></a>

*   **Rule [CC-API-001]**: APIs SHALL follow REST principles and use JSON as the data format.

<a id="CC-API-002"></a>

*   **Rule [CC-API-002]**: API versioning strategy SHALL avoid breaking changes (prefer backwards-compatible additions).

## Observability
*Measure what matters.*

<a id="CC-OBS-001"></a>

*   **Rule [CC-OBS-001]**: Monitoring SHALL be driven by Service Level Indicators (SLIs) and Service Level Objectives (SLOs).
    *   **Root**:

        *   [NFR-OPS-001](../../spec/non-functional-requirements/availability.md#NFR-OPS-001) (SLO)

<a id="CC-OBS-002"></a>

*   **Rule [CC-OBS-002]**: Metrics SHALL follow the RED method (Rate, Errors, Duration).
    *   **Root**:

        *   [NFR-MON-001](../../spec/non-functional-requirements/monitoring.md#NFR-MON-001) (Continuous Monitoring)

## Deployment and Operations
*Minimize risk through reversibility and consistency.*

<a id="CC-OPS-001"></a>

*   **Rule [CC-OPS-001]**: Releases SHALL be **Reversible**.
    *   New deployments MUST NOT destructively alter the previous version's resources until the successful switchover is confirmed.
    *   **Decision**: [../../adr/decisions/deployment-strategy](../../adr/decisions/deployment-strategy.md) (Blue-Green).
    *   **Root**:
        *   [NFR-OPS-002](../../spec/non-functional-requirements/availability.md#NFR-OPS-002) (MTTR)

<a id="CC-OPS-002"></a>

*   **Rule [CC-OPS-002]**: Deployment Artifacts SHALL be **Immutable** (Build Once, Deploy Many).
    *   The same built artifact (container image, lambda zip) MUST be promoted from Staging to Production. Configuration is injected via environment variables.
    *   **Root**:
        *   [NFR-SEC-002](../../spec/non-functional-requirements/security.md#NFR-SEC-002) (Supply Chain Security)

    *   **Root**:
        *   [NFR-OPS-001](../../spec/non-functional-requirements/availability.md#NFR-OPS-001) (Availability)

<a id="CC-OPS-004"></a>

*   **Rule [CC-OPS-004]**: CI/CD Pipelines SHALL be defined as Code (**Pipeline as Code**).
    *   Workflows MUST be versioned alongside the application code to ensure the build process evolves with the software.
    *   **Decision**: [../../adr/decisions/cicd-platform](../../adr/decisions/cicd-platform.md) (GitHub Actions).
    *   **Root**:
        *   [NFR-OPS-002](../../spec/non-functional-requirements/availability.md#NFR-OPS-002) (MTTR - Revert of pipeline logic)


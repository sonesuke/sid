# Runtime View

This section describes concrete behavior and interactions between building blocks in the form of **scenarios**.
Each scenario shows the "time-axis story" of how components collaborate to fulfill a requirement, governed by Cross-Cutting rules.

<a id="RT-001"></a>

## RT-001 User Login (OIDC)

### Scenario

A user authenticates via the external Identity Provider (Azure Entra ID) and gains access to the Web Console.

### Actors
* [User](../../spec/actors/list.md#ACT-USER)
* [Web Console (SPA)](building-block-view.md#BB-UI-001)
* [Auth Service (External IdP)](building-block-view.md#BB-AUTH-001)
* [API Gateway](building-block-view.md#BB-API-001)

### Flow

```mermaid

sequenceDiagram
participant User
participant SPA as Web Console (SPA)
participant IdP as Azure Entra ID
participant APIGW as API Gateway
participant Lambda as Backend Lambda

User->>SPA: Access protected page
SPA->>IdP: Redirect to /authorize (OIDC)
IdP->>User: Prompt for credentials (MFA if enabled)
User->>IdP: Submit credentials
IdP->>SPA: Return ID Token (JWT) + Auth Code
SPA->>IdP: Exchange Auth Code for Access Token
IdP->>SPA: Return Access Token
SPA->>APIGW: Call API with Bearer Token
APIGW->>APIGW: Validate JWT (Signature, Expiry, Audience)
APIGW->>Lambda: Forward authorized request
Lambda->>APIGW: Return response
APIGW->>SPA: Return response
SPA->>User: Display protected content

```

### Cross-cutting
* [CC-AUTH-001](cross-cutting-concepts.md#CC-AUTH-001) (Delegate Auth to External IdP)
* [CC-AUTH-002](cross-cutting-concepts.md#CC-AUTH-002) (Stateless JWT validation)
* [CC-LOG-001](cross-cutting-concepts.md#CC-LOG-001) (Correlation ID propagated)

### Requirements
* [FR-AUTH-001](../../spec/functional-requirements/auth.md#FR-AUTH-001) (Supported Authentication Methods)
* [NFR-PERF-001](../../spec/non-functional-requirements/performance.md#NFR-PERF-001) (Authentication Latency)

----

<a id="RT-002"></a>

## RT-002 Authenticated API Request

### Scenario

An authenticated user makes a REST API call to retrieve tenant information.

### Actors
* [User](../../spec/actors/list.md#ACT-USER)
* [API Gateway](building-block-view.md#BB-API-001)
* [Tenant Service](building-block-view.md#BB-TNT-001)

### Flow

```mermaid

sequenceDiagram
participant User
participant APIGW as API Gateway
participant Lambda as Tenant Service (Lambda)
participant DynamoDB as DynamoDB

User->>APIGW: GET /tenants/{id} (Bearer Token)
APIGW->>APIGW: Validate JWT
Note right of APIGW: CC-AUTH-002: Stateless validation
APIGW->>Lambda: Forward request + Claims
Lambda->>Lambda: Check Authorization (Role + Scope)
Note right of Lambda: CC-AUTH-003: Role + Scope
Lambda->>DynamoDB: Query Tenant Data
DynamoDB->>Lambda: Return Data
Lambda->>Lambda: Construct Response
Lambda->>APIGW: Return 200 OK + JSON
APIGW->>User: Return Response

```

### Cross-cutting
* [CC-AUTH-002](cross-cutting-concepts.md#CC-AUTH-002) (Stateless JWT)
* [CC-AUTH-003](cross-cutting-concepts.md#CC-AUTH-003) (Role + Scope Authorization)
* [CC-LOG-001](cross-cutting-concepts.md#CC-LOG-001) (Correlation ID)
* [CC-API-001](cross-cutting-concepts.md#CC-API-001) (REST + JSON)

### Requirements
* [FR-TENANT-001](../../spec/functional-requirements/tenant-admin.md#FR-TENANT-001) (User Invitation / Tenant context)
* [NFR-PERF-002](../../spec/non-functional-requirements/performance.md#NFR-PERF-002) (API Latency)

----

<a id="RT-003"></a>

## RT-003 Async Event Processing

### Scenario

A domain event (e.g., `TenantCreated`) is published and consumed by multiple services asynchronously.

### Actors
* [Tenant Service](building-block-view.md#BB-TNT-001)
* [Event Bus](building-block-view.md#BB-EVT-001)
* [Billing Service](building-block-view.md#BB-BIL-001)
* [Audit Service](building-block-view.md#BB-AUD-001)

### Flow

```mermaid

sequenceDiagram
participant TenantSvc as Tenant Service
participant EventBus as EventBridge
participant BillingSvc as Billing Service
participant AuditSvc as Audit Service

TenantSvc->>EventBus: Publish TenantCreated event
Note right of EventBus: event.correlation_id = req.correlation_id

par Parallel Fan-out
EventBus->>BillingSvc: Deliver event (Rule: source = tenant.*)
EventBus->>AuditSvc: Deliver event (Rule: *)
end

BillingSvc->>BillingSvc: Initialize billing profile
Note right of BillingSvc: CC-DAT-001: Idempotent write

AuditSvc->>AuditSvc: Persist audit log

```

### Cross-cutting
* [CC-LOG-001](cross-cutting-concepts.md#CC-LOG-001) (Correlation ID propagation)
* [CC-DAT-001](cross-cutting-concepts.md#CC-DAT-001) (Idempotent writes)
* [CC-DAT-002](cross-cutting-concepts.md#CC-DAT-002) (Eventual Consistency)

### Requirements
* [FR-BILL-002](../../spec/functional-requirements/billing.md#FR-BILL-002) (Billing Event Ingestion)
* [FR-LOG-001](../../spec/functional-requirements/audit.md#FR-LOG-001) (Audit Log Collection)
* [NFR-OPS-003](../../spec/non-functional-requirements/availability.md#NFR-OPS-003) (Failover / Event Delivery)

----

<a id="RT-004"></a>

## RT-004 Blue-Green Switchover

### Scenario

A new version is deployed to Production using Blue-Green deployment. Traffic is switched from Blue (old) to Green (new).

### Actors
* [CI/CD Service](building-block-view.md#BB-CICD-001)
* [API Gateway](building-block-view.md#BB-API-001)
* [Observability Platform](building-block-view.md#BB-OBS-001)

### Flow

```mermaid

sequenceDiagram
participant CICD as CI/CD (GitHub Actions)
participant APIGW as API Gateway (Alias)
participant LambdaBlue as Lambda (Blue - v1)
participant LambdaGreen as Lambda (Green - v2)
participant Obs as Observability

CICD->>LambdaGreen: Deploy new version (v2)
CICD->>LambdaGreen: Invoke warm-up / smoke test
LambdaGreen->>CICD: Health OK

CICD->>APIGW: Update Alias weight (Blue=0%, Green=100%)
Note right of APIGW: CC-OPS-001: Reversible release

loop Monitor (5 min)
Obs->>LambdaGreen: Collect metrics (Error Rate, P99 Latency)
Obs->>CICD: Report health status
end

alt Health OK
CICD->>LambdaBlue: Decommission (optional)
else Health Degraded
CICD->>APIGW: Rollback Alias (Blue=100%, Green=0%)
APIGW->>LambdaBlue: Route traffic
end

```

### Cross-cutting
* [CC-OPS-001](cross-cutting-concepts.md#CC-OPS-001) (Reversible release)
* [CC-OPS-002](cross-cutting-concepts.md#CC-OPS-002) (Immutable artifact)
* [CC-OBS-001](cross-cutting-concepts.md#CC-OBS-001) (SLI/SLO driven)

### Requirements
* [NFR-OPS-001](../../spec/non-functional-requirements/availability.md#NFR-OPS-001) (Availability SLO)
* [NFR-OPS-002](../../spec/non-functional-requirements/availability.md#NFR-OPS-002) (MTTR)

----

<a id="RT-005"></a>

## RT-005 Error Handling Flow

### Scenario

An API request fails due to a downstream service error. The system logs the error, returns a structured response, and retries if applicable.

### Actors
* [User](../../spec/actors/list.md#ACT-USER)
* [API Gateway](building-block-view.md#BB-API-001)
* [Tenant Service](building-block-view.md#BB-TNT-001)
* [Observability Platform](building-block-view.md#BB-OBS-001)

### Flow

```mermaid

sequenceDiagram
participant User
participant APIGW as API Gateway
participant Lambda as Tenant Service
participant DynamoDB
participant Obs as Observability

User->>APIGW: POST /tenants (Bearer Token)
APIGW->>Lambda: Forward request
Lambda->>DynamoDB: PutItem (with retry logic)
DynamoDB-->>Lambda: Error (500 - Service Unavailable)

Lambda->>Lambda: Retry (exponential backoff, max 3)
DynamoDB-->>Lambda: Error again

Lambda->>Obs: Log error (correlation_id, stack trace)
Note right of Lambda: CC-ERR-003: No stack trace in response
Lambda->>APIGW: Return 503 (RFC 7807 Problem Details)
Note right of APIGW: CC-ERR-004: JSON Problem Details
APIGW->>User: Return 503 + Retry-After header

Obs->>Obs: Trigger Alert (NFR-MON-002)

```

### Cross-cutting
* [CC-ERR-001](cross-cutting-concepts.md#CC-ERR-001) (Map to HTTP codes)
* [CC-ERR-002](cross-cutting-concepts.md#CC-ERR-002) (Business vs System errors)
* [CC-ERR-003](cross-cutting-concepts.md#CC-ERR-003) (No stack trace exposure)
* [CC-ERR-004](cross-cutting-concepts.md#CC-ERR-004) (RFC 7807)
* [CC-LOG-001](cross-cutting-concepts.md#CC-LOG-001) (Correlation ID)

### Requirements
* [NFR-OPS-001](../../spec/non-functional-requirements/availability.md#NFR-OPS-001) (Availability SLO)
* [NFR-MON-002](../../spec/non-functional-requirements/monitoring.md#NFR-MON-002) (System Health Alerting)

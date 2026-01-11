Runtime View
============

This section describes concrete behavior and interactions between building blocks in the form of **scenarios**.
Each scenario shows the "time-axis story" of how components collaborate to fulfill a requirement, governed by Cross-Cutting rules.

.. _RT-001:

RT-001 User Login (OIDC)
------------------------

Scenario
~~~~~~~~
A user authenticates via the external Identity Provider (Azure Entra ID) and gains access to the Web Console.

Actors
~~~~~~
*   :ref:`User <ACT-USER>`
*   :ref:`Web Console (SPA) <BB-UI-001>`
*   :ref:`Auth Service (External IdP) <BB-AUTH-001>`
*   :ref:`API Gateway <BB-API-001>`

Flow
~~~~
.. mermaid::

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

Cross-cutting
~~~~~~~~~~~~~
*   :ref:`CC-AUTH-001` (Delegate Auth to External IdP)
*   :ref:`CC-AUTH-002` (Stateless JWT validation)
*   :ref:`CC-LOG-001` (Correlation ID propagated)

Requirements
~~~~~~~~~~~~
*   :ref:`FR-AUTH-001` (Supported Authentication Methods)
*   :ref:`NFR-PERF-001` (Authentication Latency)

----

.. _RT-002:

RT-002 Authenticated API Request
--------------------------------

Scenario
~~~~~~~~
An authenticated user makes a REST API call to retrieve tenant information.

Actors
~~~~~~
*   :ref:`User <ACT-USER>`
*   :ref:`API Gateway <BB-API-001>`
*   :ref:`Tenant Service <BB-TNT-001>`

Flow
~~~~
.. mermaid::

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

Cross-cutting
~~~~~~~~~~~~~
*   :ref:`CC-AUTH-002` (Stateless JWT)
*   :ref:`CC-AUTH-003` (Role + Scope Authorization)
*   :ref:`CC-LOG-001` (Correlation ID)
*   :ref:`CC-API-001` (REST + JSON)

Requirements
~~~~~~~~~~~~
*   :ref:`FR-TENANT-001` (User Invitation / Tenant context)
*   :ref:`NFR-PERF-002` (API Latency)

----

.. _RT-003:

RT-003 Async Event Processing
-----------------------------

Scenario
~~~~~~~~
A domain event (e.g., `TenantCreated`) is published and consumed by multiple services asynchronously.

Actors
~~~~~~
*   :ref:`Tenant Service <BB-TNT-001>`
*   :ref:`Event Bus <BB-EVT-001>`
*   :ref:`Billing Service <BB-BIL-001>`
*   :ref:`Audit Service <BB-AUD-001>`

Flow
~~~~
.. mermaid::

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

Cross-cutting
~~~~~~~~~~~~~
*   :ref:`CC-LOG-001` (Correlation ID propagation)
*   :ref:`CC-DAT-001` (Idempotent writes)
*   :ref:`CC-DAT-002` (Eventual Consistency)

Requirements
~~~~~~~~~~~~
*   :ref:`FR-BILL-002` (Billing Event Ingestion)
*   :ref:`FR-LOG-001` (Audit Log Collection)
*   :ref:`NFR-OPS-003` (Failover / Event Delivery)

----

.. _RT-004:

RT-004 Blue-Green Switchover
----------------------------

Scenario
~~~~~~~~
A new version is deployed to Production using Blue-Green deployment. Traffic is switched from Blue (old) to Green (new).

Actors
~~~~~~
*   :ref:`CI/CD Service <BB-CICD-001>`
*   :ref:`API Gateway <BB-API-001>`
*   :ref:`Observability Platform <BB-OBS-001>`

Flow
~~~~
.. mermaid::

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

Cross-cutting
~~~~~~~~~~~~~
*   :ref:`CC-OPS-001` (Reversible release)
*   :ref:`CC-OPS-002` (Immutable artifact)
*   :ref:`CC-OBS-001` (SLI/SLO driven)

Requirements
~~~~~~~~~~~~
*   :ref:`NFR-OPS-001` (Availability SLO)
*   :ref:`NFR-OPS-002` (MTTR)

----

.. _RT-005:

RT-005 Error Handling Flow
--------------------------

Scenario
~~~~~~~~
An API request fails due to a downstream service error. The system logs the error, returns a structured response, and retries if applicable.

Actors
~~~~~~
*   :ref:`User <ACT-USER>`
*   :ref:`API Gateway <BB-API-001>`
*   :ref:`Tenant Service <BB-TNT-001>`
*   :ref:`Observability Platform <BB-OBS-001>`

Flow
~~~~
.. mermaid::

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

Cross-cutting
~~~~~~~~~~~~~
*   :ref:`CC-ERR-001` (Map to HTTP codes)
*   :ref:`CC-ERR-002` (Business vs System errors)
*   :ref:`CC-ERR-003` (No stack trace exposure)
*   :ref:`CC-ERR-004` (RFC 7807)
*   :ref:`CC-LOG-001` (Correlation ID)

Requirements
~~~~~~~~~~~~
*   :ref:`NFR-OPS-001` (Availability SLO)
*   :ref:`NFR-MON-002` (System Health Alerting)

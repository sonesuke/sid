Deployment View
===============

This section describes the technical infrastructure where the system executes.
The system is deployed on **AWS (Amazon Web Services)** using a completely **Serverless** model to minimize operational overhead (:doc:`ADR-ARCH-001 <../../adr/decisions/architecture-style>`).
Network strategy follows a **No-VPC / Identity-Based Security** model relying on IAM and TLS (:doc:`ADR-INF-001 <../../adr/decisions/network-strategy>`).

Infrastructure Level 1
----------------------
.. mermaid::
   
   C4Deployment
      title Deployment Diagram for SaaS Foundation Platform (AWS)

      Deployment_Node(aws, "AWS Cloud", "ap-northeast-1") {
         
         Deployment_Node(ui, "Frontend", "CloudFront + S3 + Lambda@Edge") {
             Container(spa, "Web Console", "React App", "Static Assets")
         }

         Deployment_Node(auth, "Authentication", "Azure Cloud") {
            Container(idp, "Auth Service", "Azure Entra ID", "Manages User Identities")
         }
         
         Deployment_Node(api, "API Layer", "API Gateway") {
            Container(gw, "API Gateway", "HTTP API", "Entry point")
         }

         Deployment_Node(compute, "Compute Layer", "Lambda (No VPC)") {
            Container(lambda_tenant, "Tenant Function", "Python 3.12")
            Container(lambda_billing, "Billing Function", "Python 3.12")
         }
         
         Deployment_Node(data, "Data Persistence", "DynamoDB") {
            Container(db_tenant, "Tenant Table", "On-Demand")
         }
         
         Deployment_Node(msg, "Messaging", "EventBridge") {
            Container(bus, "Event Bus", "Serverless Bus")
         }
         
         Deployment_Node(mgmt, "Management", "AWS Management") {
            Container(logs, "Logs", "CloudWatch Logs", "Operational Logs")
            Container(archive, "Audit Archive", "S3 Glacier", "Long-term Retention")
            Container(backup, "Backup", "AWS Backup", "DynamoDB PITR")
         }

         Deployment_Node(sec, "Security", "Infrastructure Security") {
            Container(waf, "WAF", "AWS WAF", "Threat Protection")
         }
      }

      Rel(user, spa, "HTTPS / Downloads Assets")
      Rel(spa, gw, "HTTPS / AJAX")
      Rel(gw, auth, "Authorizes via JWT")
      Rel(lambda_tenant, db_tenant, "Reads/Writes")
      Rel(lambda_tenant, bus, "Publishes Events")
      Rel(lambda_tenant, logs, "Streams Logs")
      Rel(db_tenant, backup, "Backs up")
      Rel(bus, archive, "Archives Events")
      
      Rel(user, waf, "Filtered by")

Mapping to Infrastructure
~~~~~~~~~~~~~~~~~~~~~~~~~
This table maps the conceptual building blocks to concrete AWS Managed Services.

.. _DEP-AWS-001:

*   **[DEP-AWS-001] API Gateway**:
    *   **AWS Service**: Amazon API Gateway
    *   **Mapping**: :ref:`BB-API-001`
    *   **Configuration Details**:
        *   HTTP APIs (v2) for lower latency and cost.

.. _DEP-AWS-006:

*   **[DEP-AWS-006] Web Console (SPA)**:
    *   **AWS Service**: CloudFront + S3 + Lambda@Edge
    *   **Mapping**: :ref:`BB-UI-001`
    *   **Configuration Details**:
        *   Hosting for static assets (React/TS). Lambda@Edge for security headers/routing.

.. _DEP-AZU-001:

*   **[DEP-AZU-001] Auth Service**:
    *   **AWS Service**: Azure Entra ID (External)
    *   **Mapping**: :ref:`BB-AUTH-001`
    *   **Configuration Details**:
        *   External Identities (CIAM). OIDC integration.

.. _DEP-AWS-002:

*   **[DEP-AWS-002] Compute (Lambda)**:
    *   **AWS Service**: AWS Lambda
    *   **Mapping**: :ref:`BB-TNT-001`, :ref:`BB-BIL-001`, :ref:`BB-AUD-001`
    *   **Configuration Details**:
        *   Python 3.x runtime. Deployed via Terraform.
    *   **Decision**: :doc:`../../adr/decisions/language-runtime`, :doc:`../../adr/decisions/iac-tool-selection`

.. _DEP-AWS-003:

*   **[DEP-AWS-003] Data Store**:
    *   **AWS Service**: Amazon DynamoDB
    *   **Mapping**: :ref:`BB-TNT-001`, :ref:`BB-BIL-001` (Persistence)
    *   **Configuration Details**:
        *   On-Demand Capacity mode.
    *   **Decision**: :doc:`../../adr/decisions/data-persistence`

.. _DEP-AWS-004:

*   **[DEP-AWS-004] Event Bus**:
    *   **AWS Service**: Amazon EventBridge
    *   **Mapping**: :ref:`BB-EVT-001`
    *   **Configuration Details**:
        *   Custom Registry for domain events.

.. _DEP-AWS-005:

*   **[DEP-AWS-005] Feature Flags**:
    *   **AWS Service**: AWS AppConfig
    *   **Mapping**: :ref:`BB-FLG-001`
    *   **Configuration Details**:
        *   Freeform configuration profile.

.. _DEP-AWS-007:

*   **[DEP-AWS-007] Observability & Archive**:
    *   **AWS Service**: CloudWatch Logs / S3
    *   **Mapping**: :ref:`BB-AUD-001`
    *   **Configuration Details**:
        *   CloudWatch for real-time logs (Retention: 30 days). S3 Glacier for long-term audit archive (Retention: 7 years).

.. _DEP-AWS-008:

*   **[DEP-AWS-008] Backup**:
    *   **AWS Service**: AWS Backup
    *   **Mapping**: :ref:`BB-TNT-001`, :ref:`BB-BIL-001`
    *   **Configuration Details**:
        *   Centralized backup policy. DynamoDB PITR (Point-in-Time Recovery) enabled (35 days).

.. _DEP-AWS-009:

*   **[DEP-AWS-009] Web Application Firewall**:
    *   **AWS Service**: AWS WAF
    *   **Mapping**: :ref:`BB-UI-001` (CloudFront), :ref:`BB-API-001` (API Gateway)
    *   **Configuration Details**:
        *   Protects against common web exploits (OWASP Top 10) and bots. Managed Rules enabled.

Environment Strategy
--------------------
To ensure stability, we utilize a multi-account strategy with strict promotion rules (:ref:`CC-OPS-002`).

.. list-table::
   :header-rows: 1
   :widths: 20 60 20

   * - Environment
     - Purpose & Configuration
     - References
   * - **[DEP-ENV-001] Development**
     - **Purpose**: Integration testing for developers.
     - *   :ref:`CC-DEV-001`
   * - **[DEP-ENV-002] Staging**
     - **Purpose**: Pre-production verification (E2E, Load Tests).
     - *   :ref:`CC-OPS-002`
   * - **[DEP-ENV-003] Production**
     - **Purpose**: Live traffic. High Availability.
     - *   :ref:`NFR-OPS-001`

Deployment Strategy
-------------------
We adopt **Blue-Green Deployment** to achieve Zero Downtime and Immediate Rollback capabilities.

.. _DEP-OPS-001:

*   **[DEP-OPS-001] Blue-Green Switchover**:
    *   **Mechanism**: Traffic shifting via API Gateway Stages / Lambda Aliases.
    *   **Procedure**:
        1.  Deploy new version (Green) alongside active version (Blue).
        2.  Run Smoke Tests against Green endpoint.
        3.  Update Routing Weight to 100% Green.
        4.  Monitor Error Rates (Red Metrics).
        5.  *If success*: Deprovision Blue after stabilization period.
        6.  *If failure*: Atomically revert Routing to 100% Blue.
    *   **Decision**: :doc:`../../adr/decisions/deployment-strategy`
    *   **Principles**: :ref:`CC-OPS-001` (Reversibility), :ref:`CC-OPS-003` (DB Compatibility).

NFR Satisfaction
----------------
This deployment structure supports:

- **Availability**: Relies on AWS Multi-AZ availability for Lambda, DynamoDB, and API Gateway (implicitly HA).
- **Scalability**: All selected services (Lambda, DynamoDB On-Demand) scale to zero and burst automatically.
- **Operational Efficiency**: No servers to patch or manage (NoOps).


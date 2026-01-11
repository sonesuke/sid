Deployment View
===============

This section describes the technical infrastructure where the system executes.
The system is deployed on **AWS (Amazon Web Services)** using a completely **Serverless** model to minimize operational overhead (:doc:`ADR-0006 <../../adr/0006-architecture-style>`).
Network strategy follows a **No-VPC / Identity-Based Security** model relying on IAM and TLS (:doc:`ADR-0008 <../../adr/0008-network-strategy>`).

Infrastructure Level 1
----------------------
.. mermaid::
   
   C4Deployment
      title Deployment Diagram for SaaS Foundation Platform (AWS)

      Deployment_Node(aws, "AWS Cloud", "ap-northeast-1") {
         
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
      }

      Rel(gw, lambda_tenant, "Invokes")
      Rel(gw, auth, "Authorizes via JWT")
      Rel(lambda_tenant, db_tenant, "Reads/Writes")
      Rel(lambda_tenant, bus, "Publishes Events")

Mapping to Infrastructure
~~~~~~~~~~~~~~~~~~~~~~~~~
This table maps the conceptual building blocks to concrete AWS Managed Services.

.. list-table::
   :header-rows: 1
   :widths: 20 30 50

   * - Building Block
     - AWS Service
     - Configuration Details
   * - **API Gateway**
     - Amazon API Gateway
     - HTTP APIs (v2) for lower latency and cost. Throttling enabled.
   * - **Auth Service**
     - Azure Entra ID
     - External Identities (CIAM). OIDC integration.
   * - **Tenant / Billing Service**
     - AWS Lambda
     - Python 3.x runtime. Deployed via SAM/CDK.
   * - **Data Store**
     - Amazon DynamoDB
     - On-Demand Capacity mode (pay-per-request) to handle spiky traffic without provisioning.
   * - **Event Bus**
     - Amazon EventBridge
     - Custom Registry for domain events. Archive enabled for Audit.
   * - **Feature Flags**
     - AWS AppConfig
     - Freeform configuration profile or Feature Flag profile.

Environment Strategy
--------------------
To ensure stability, we utilize a multi-account or multi-environment strategy.

- **Development**: Features deployed immediately for integration testing. Resources may have shorter retention.
- **Staging**: Mirror of production configuration for final verification.
- **Production**: Strictly controlled environment. High availability settings enforced.

NFR Satisfaction
----------------
This deployment structure supports:

- **Availability**: Relies on AWS Multi-AZ availability for Lambda, DynamoDB, and API Gateway (implicitly HA).
- **Scalability**: All selected services (Lambda, DynamoDB On-Demand) scale to zero and burst automatically.
- **Operational Efficiency**: No servers to patch or manage (NoOps).


# Deployment View

This section describes the technical infrastructure where the system executes.
The system is deployed on **AWS (Amazon Web Services)** using a completely **Serverless** model to minimize operational overhead ([ADR-ARCH-001](../../adr/decisions/architecture-style.md)).
Network strategy follows a **No-VPC / Identity-Based Security** model relying on IAM and TLS ([ADR-INF-001](../../adr/decisions/network-strategy.md)).

## Infrastructure Level 1

```mermaid

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

```

### Mapping to Infrastructure

This table maps the conceptual building blocks to concrete AWS Managed Services.

<a id="DEP-AWS-001"></a>

#### API Gateway

* **AWS Service**: Amazon API Gateway
* **Mapping**: [BB-API-001](building-block-view.md#BB-API-001)
* **Configuration Details**:
  * HTTP APIs (v2) for lower latency and cost.

<a id="DEP-AWS-006"></a>

#### Web Console (SPA)

* **AWS Service**: CloudFront + S3 + Lambda@Edge + **Amazon API Gateway + AWS Lambda**
* **Mapping**: [BB-UI-001](building-block-view.md#BB-UI-001)
* **Configuration Details**:
  * Hosting for static assets (React/TS). Lambda@Edge for security headers.
  * **BFF (Backend for Frontend)**: Specific API endpoints (e.g., config, session) served via APIGW + Lambda.

<a id="DEP-AZU-001"></a>

#### Auth Service

* **AWS Service**: Azure Entra ID (External)
* **Mapping**: [BB-AUTH-001](building-block-view.md#BB-AUTH-001)
* **Configuration Details**:
  * External Identities (CIAM). OIDC integration.

<a id="DEP-AWS-002"></a>

#### Compute (Lambda)

* **AWS Service**: AWS Lambda
* **Mapping**: [BB-TNT-001](building-block-view.md#BB-TNT-001), [BB-BIL-001](building-block-view.md#BB-BIL-001), [BB-AUD-001](building-block-view.md#BB-AUD-001)
* **Configuration Details**:
  * Python 3.x runtime. Deployed via Terraform.
* **Decision**: [../../adr/decisions/language-runtime](../../adr/decisions/language-runtime.md), [../../adr/decisions/iac-tool-selection](../../adr/decisions/iac-tool-selection.md)

<a id="DEP-AWS-003"></a>

#### Data Store

* **AWS Service**: Amazon DynamoDB
* **Mapping**: [BB-TNT-001](building-block-view.md#BB-TNT-001), [BB-BIL-001](building-block-view.md#BB-BIL-001) (Persistence)
* **Configuration Details**:
  * On-Demand Capacity mode.
* **Decision**: [../../adr/decisions/data-persistence](../../adr/decisions/data-persistence.md)

<a id="DEP-AWS-004"></a>

#### Event Bus

* **AWS Service**: Amazon EventBridge
* **Mapping**: [BB-EVT-001](building-block-view.md#BB-EVT-001)
* **Configuration Details**:
  * Custom Registry for domain events.

<a id="DEP-AWS-005"></a>

#### Feature Flag Services

* **AWS Service**: AWS AppConfig
* **Mapping**: [BB-FLG-001](building-block-view.md#BB-FLG-001)
* **Configuration Details**:
  * Freeform configuration profile.

<a id="DEP-AWS-007"></a>

#### Observability & Archive

* **AWS Service**: CloudWatch Logs / S3
* **Mapping**: [BB-AUD-001](building-block-view.md#BB-AUD-001), [BB-OBS-001](building-block-view.md#BB-OBS-001)
* **Configuration Details**:
  * CloudWatch for real-time logs (Retention: 30 days). S3 Glacier for long-term audit archive (Retention: 7 years).

<a id="DEP-AWS-008"></a>

#### Backup

* **AWS Service**: AWS Backup
* **Mapping**: [BB-TNT-001](building-block-view.md#BB-TNT-001), [BB-BIL-001](building-block-view.md#BB-BIL-001)
* **Configuration Details**:
  * Centralized backup policy. DynamoDB PITR (Point-in-Time Recovery) enabled (35 days).

<a id="DEP-AWS-009"></a>

#### Web Application Firewall

* **AWS Service**: AWS WAF
* **Mapping**: [BB-UI-001](building-block-view.md#BB-UI-001) (CloudFront), [BB-API-001](building-block-view.md#BB-API-001) (API Gateway)
* **Configuration Details**:
  * Protects against common web exploits (OWASP Top 10) and bots. Managed Rules enabled.

## Environment Strategy

To ensure stability, we utilize a multi-account strategy with strict promotion rules ([CC-OPS-002](cross-cutting-concepts.md#CC-OPS-002)).

| Environment | Purpose & Configuration | References |
|-------------|-------------------------|------------|
| **[DEP-ENV-001] Development** | Integration testing for developers. | [CC-DEV-001](cross-cutting-concepts.md#CC-DEV-001) |
| **[DEP-ENV-002] Staging** | Pre-production verification (E2E, Load Tests). | [CC-OPS-002](cross-cutting-concepts.md#CC-OPS-002) |
| **[DEP-ENV-003] Production** | Live traffic. High Availability. | [NFR-OPS-001](../../spec/non-functional-requirements/availability.md#NFR-OPS-001) |

## Deployment Strategy

We adopt **Blue-Green Deployment** to achieve Zero Downtime and Immediate Rollback capabilities.

<a id="DEP-OPS-001"></a>

### Blue-Green Switchover

* **Mechanism**: Traffic shifting via API Gateway Stages / Lambda Aliases.
* **Procedure**:

  1. Deploy new version (Green) alongside active version (Blue).
  2. Run Smoke Tests against Green endpoint.
  3. Update Routing Weight to 100% Green.
  4. Monitor Error Rates (Red Metrics).
  5. *If success*: Deprovision Blue after stabilization period.
  6. *If failure*: Atomically revert Routing to 100% Blue.

* **Decision**: [../../adr/decisions/deployment-strategy](../../adr/decisions/deployment-strategy.md)
* **Decision**: [../../adr/decisions/deployment-strategy](../../adr/decisions/deployment-strategy.md)
* **Principles**: [CC-OPS-001](cross-cutting-concepts.md#CC-OPS-001) (Reversibility), [CC-OPS-003](cross-cutting-concepts.md#CC-OPS-003) (DB Compatibility).

<a id="DEP-OPS-002"></a>

### CI/CD Pipeline

* **Automated Flow**:

  1. **Pull Request**: Run Linting (Ruff), Unit Tests (Pytest), and Security Scans (Trivy).
  2. **Merge to Main**: Trigger Build Artifact (Lambda Zip).
  3. **Deploy Dev**: Deploy to Development environment. Run Integration Tests.
  4. **Promote Staging**: Deploy same artifact to Staging ([CC-OPS-002](cross-cutting-concepts.md#CC-OPS-002)). Run E2E / Load Tests.
  5. **Manual Approval**: Operator approves promotion to Production.
  6. **Promote Production**: Trigger Blue-Green Deployment ([DEP-OPS-001](#DEP-OPS-001)).

* **Mechanism**: GitHub Actions Workflows.
* **Decision**: [../../adr/decisions/cicd-platform](../../adr/decisions/cicd-platform.md)
* **Principles**: [CC-OPS-002](cross-cutting-concepts.md#CC-OPS-002) (Immutable), [CC-OPS-004](cross-cutting-concepts.md#CC-OPS-004) (Pipeline as Code).

## NFR Satisfaction

This deployment structure supports:

* **Availability**: Relies on AWS Multi-AZ availability for Lambda, DynamoDB, and API Gateway (implicitly HA).
* **Scalability**: All selected services (Lambda, DynamoDB On-Demand) scale to zero and burst automatically.
* **Operational Efficiency**: No servers to patch or manage (NoOps).

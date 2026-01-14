# Building Block View

This section decomposes the system into its building blocks (modules, components).
The architecture follows a **Microservices** approach utilizing **Managed Services** (see [../../adr/decisions/architecture-style](../../adr/decisions/architecture-style.md)).

## Level 1: System Whitebox (Container View)

```mermaid

C4Container
title Container Diagram for SaaS Foundation Platform (Microservices)

Person(user, "User", "Accesses via Browser/API")

System_Boundary(c1, "SaaS Foundation Platform") {
Container(web_ui, "Web Console (SPA)", "React/TypeScript", "Operator & Tenant Administration Portal")
Container(api_gw, "API Gateway", "API Gateway", "Unified Entry Point, Routing, Throttling")

Container(auth_svc, "Auth Service", "Identity Provider / FaaS", "IdP, Token Vending, User Mgmt")
Container(tenant_svc, "Tenant Service", "FaaS + NoSQL", "Tenant Registration, Config, Lifecycle")
Container(flag_svc, "Feature Flag Service", "Configuration Service", "Feature Toggles & Rollouts")
Container(obs_platform, "Observability Platform", "CloudWatch / X-Ray", "Metrics, Logs, Tracing, Alerting")
Container(cicd_svc, "CI/CD Service", "GitHub Actions", "Build, Test, Deploy Pipeline")

Container(event_bus, "Event Bus", "Message Broker", "Asynchronous Event Backbone")
}

System_Ext(app, "Managed Application", "Consumes Auth & Flags")

Rel(user, web_ui, "HTTPS / Browser")
Rel(web_ui, api_gw, "HTTPS / REST (JSON)")
Rel(user, api_gw, "HTTPS / REST")

Rel(api_gw, auth_svc, "Routes Auth Req")
Rel(api_gw, tenant_svc, "Routes Tenant Req")
Rel(api_gw, flag_svc, "Routes Flag Req")

Rel(auth_svc, event_bus, "Publishes User Events")
Rel(tenant_svc, event_bus, "Publishes Tenant Events")
Rel(billing_svc, event_bus, "Subscribes to Billable Events")
Rel(audit_svc, event_bus, "Subscribes to All Events")

Rel(api_gw, obs_platform, "Sends Metrics/Logs")
Rel(tenant_svc, obs_platform, "Sends Metrics/Logs")
Rel(auth_svc, obs_platform, "Sends Metrics/Logs")

Rel(app, api_gw, "Validates Tokens / Fetches Flags")

```

## Component Description

<a id="BB-UI-001"></a>

* **[BB-UI-001] Web Console (SPA)**:
  * **Responsibility**: Single Page Application providing Administrative interfaces for Operators and Tenants.
  * **Related FRs**:
    * [Operator Console](../../spec/interface-requirements/ui.md#IF-OPS-CONSOLE)
    * [Tenant Administration Console](../../spec/interface-requirements/ui.md#IF-TENANT-CONSOLE)
    * [Auditor Console](../../spec/interface-requirements/ui.md#IF-AUDIT-CONSOLE)
    * [Universal Login Page](../../spec/interface-requirements/ui.md#IF-LOGIN-UI)
  * **Related NFRs**:
    * [UI Responsiveness](../../spec/non-functional-requirements/performance.md#NFR-PERF-003)

<a id="BB-API-001"></a>

* **[BB-API-001] API Gateway**:
  * **Responsibility**: Entry point for all external requests. Handles routing, rate limiting, and authentication offloading.
  * **Related FRs**:

    *   [API Key Management](../../spec/functional-requirements/system-ops.md#FR-SYS-002)
  * **Related NFRs**:

    *   [Load Balancing and Failover](../../spec/non-functional-requirements/availability.md#NFR-OPS-003)
    *   [Authentication Latency](../../spec/non-functional-requirements/performance.md#NFR-PERF-001)

<a id="BB-AUTH-001"></a>

* **[BB-AUTH-001] Auth Service**:
  * **Responsibility**: Manages user identities and credentials via External IdP.
  * **Related FRs**:

    *   [Supported Authentication Methods](../../spec/functional-requirements/auth.md#FR-AUTH-001)
    *   [Tenant SSO Configuration](../../spec/functional-requirements/auth.md#FR-AUTH-003)
    *   [Password Reset](../../spec/functional-requirements/auth.md#FR-AUTH-004)
    *   [Session Management](../../spec/functional-requirements/auth.md#FR-AUTH-005)
    *   [Password Policy Configuration](../../spec/functional-requirements/auth.md#FR-AUTH-006)
  * **Related NFRs**:

    *   [Multi-Factor Authentication](../../spec/non-functional-requirements/security.md#NFR-SEC-003)
    *   [Adaptive Authentication](../../spec/non-functional-requirements/security.md#NFR-SEC-006)
    *   [User Scalability](../../spec/non-functional-requirements/capacity.md#NFR-CAP-002)

<a id="BB-TNT-001"></a>

* **[BB-TNT-001] Tenant Service**:
  * **Responsibility**: Manages Tenant lifecycle (onboarding, configuration, suspension).
  * **Related FRs**:

    *   [User Invitation](../../spec/functional-requirements/tenant-admin.md#FR-TENANT-001)
    *   [User Deletion](../../spec/functional-requirements/tenant-admin.md#FR-TENANT-002)
    *   [Contract Modification](../../spec/functional-requirements/tenant-admin.md#FR-TENANT-003)
    *   [User Role Management](../../spec/functional-requirements/tenant-admin.md#FR-TENANT-004)
    *   [User Status Management](../../spec/functional-requirements/tenant-admin.md#FR-TENANT-006)
    *   [Invitation Resend](../../spec/functional-requirements/tenant-admin.md#FR-TENANT-007)
    *   [Tenant Status Management](../../spec/functional-requirements/platform-ops.md#FR-OPS-001)
    *   [Tenant Deletion](../../spec/functional-requirements/platform-ops.md#FR-OPS-002)
    *   [Operator JIT Provisioning](../../spec/functional-requirements/system-ops.md#FR-SYS-004)
  * **Related NFRs**:

    *   [Tenant Scalability](../../spec/non-functional-requirements/capacity.md#NFR-CAP-001)
    *   [Data Residency](../../spec/non-functional-requirements/data.md#NFR-DATA-001)

<a id="BB-FLG-001"></a>

* **[BB-FLG-001] Feature Flag Service**:
  * **Responsibility**: Delivers dynamic configuration and feature toggles to the Application.
  * **Related FRs**:

    *   [Flag Configuration](../../spec/functional-requirements/feature-flags.md#FR-FLAG-001)
    *   [Flag Delivery](../../spec/functional-requirements/feature-flags.md#FR-FLAG-002)
  * **Related NFRs**:

    *   [API Latency](../../spec/non-functional-requirements/performance.md#NFR-PERF-002)

<a id="BB-BIL-001"></a>

* **[BB-BIL-001] Billing Service**:
  * **Responsibility**: Aggregates usage metrics and interfaces with external Billing System.
  * **Related FRs**:

    *   [Billing Event Persistence](../../spec/functional-requirements/billing.md#FR-BILL-001)
    *   [Billing Event Ingestion](../../spec/functional-requirements/billing.md#FR-BILL-002)
    *   [Billing Data Export](../../spec/functional-requirements/billing.md#FR-BILL-003)
  * **Related NFRs**:

    *   [Backup and Redundancy](../../spec/non-functional-requirements/availability.md#NFR-OPS-004)

<a id="BB-AUD-001"></a>

* **[BB-AUD-001] Audit Service**:
  * **Responsibility**: Ingests and archives security and operational logs.
  * **Related FRs**:

    *   [Audit Log Collection](../../spec/functional-requirements/audit.md#FR-LOG-001)
    *   [Audit Log Export](../../spec/functional-requirements/audit.md#FR-LOG-002)
    *   [Control Plane Auditing](../../spec/functional-requirements/audit.md#FR-LOG-003)
  * **Related NFRs**:

    *   [Continuous Monitoring](../../spec/non-functional-requirements/monitoring.md#NFR-MON-001)

<a id="BB-OBS-001"></a>

* **[BB-OBS-001] Observability Platform**:
  * **Responsibility**: Centralized collection and visualization of Metrics, Logs, and Traces. Handles Alerting and Synthetics.
  * **Related FRs**:
    * [System Health Monitoring](../../spec/functional-requirements/system-ops.md#FR-SYS-005)
  * **Related NFRs**:
    * [System Health Alerting](../../spec/non-functional-requirements/monitoring.md#NFR-MON-002)
    * [Synthetic Monitoring](../../spec/non-functional-requirements/monitoring.md#NFR-MON-003)
    * [Continuous Monitoring](../../spec/non-functional-requirements/monitoring.md#NFR-MON-001)

<a id="BB-CICD-001"></a>

* **[BB-CICD-001] CI/CD Service**:
  * **Responsibility**: Automation of Build, Test, Security Scanning, and Deployment processes.
  * **Related NFRs**:
    * [Availability SLO](../../spec/non-functional-requirements/availability.md#NFR-OPS-001) (Deployment Safety)
  * **Decision**: [../../adr/decisions/cicd-platform](../../adr/decisions/cicd-platform.md)

<a id="BB-EVT-001"></a>

* **[BB-EVT-001] Event Bus**:
  * **Responsibility**: Asynchronous message broker for decoupling services (Publish/Subscribe pattern).
  * **Related FRs**:

    *   Infrastructure component supporting all Event-Driven FRs.
  * **Related NFRs**:

    *   [Load Balancing and Failover](../../spec/non-functional-requirements/availability.md#NFR-OPS-003)

## Internal Structure

The internal structure of each microservice follows a standard **Layered / Hexagonal Architecture** to ensure testability and consistency.
For the detailed component pattern, see [../../adr/decisions/architecture-style](../../adr/decisions/architecture-style.md).

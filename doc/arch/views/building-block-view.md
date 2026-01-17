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
Container(billing_svc, "Billing Service", "FaaS + NoSQL", "Usage Metering & Billing Events")
Container(audit_svc, "Audit Service", "FaaS + S3", "Audit Log Collection & Archive")
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

### Web Console (SPA)

* **Responsibility**: Single Page Application providing Administrative interfaces for Operators and Tenants.
* **Related FRs**:
  * [IF-OPS-CONSOLE (Operator Console)](../../spec/interface-requirements/ui.md#IF-OPS-CONSOLE)
  * [IF-TENANT-CONSOLE (Tenant Administration Console)](../../spec/interface-requirements/ui.md#IF-TENANT-CONSOLE)
  * [IF-AUDIT-CONSOLE (Auditor Console)](../../spec/interface-requirements/ui.md#IF-AUDIT-CONSOLE)
  * [IF-LOGIN-UI (Universal Login Page)](../../spec/interface-requirements/ui.md#IF-LOGIN-UI)
* **Related NFRs**:
  * [NFR-PERF-003 (UI Responsiveness)](../../spec/non-functional-requirements/performance.md#NFR-PERF-003)

<a id="BB-API-001"></a>

### API Gateway

* **Responsibility**: Entry point for all external requests. Handles routing, rate limiting, and authentication offloading.
* **Related FRs**:
  * [FR-SYS-002 (API Key Management)](../../spec/functional-requirements/system-ops.md#FR-SYS-002)
* **Related NFRs**:
  * [NFR-OPS-003 (Load Balancing and Failover)](../../spec/non-functional-requirements/availability.md#NFR-OPS-003)
  * [NFR-PERF-001 (Authentication Latency)](../../spec/non-functional-requirements/performance.md#NFR-PERF-001)

<a id="BB-AUTH-001"></a>

### Auth Service

* **Responsibility**: Manages user identities and credentials via External IdP.
* **Related FRs**:
  * [FR-AUTH-001 (Supported Authentication Methods)](../../spec/functional-requirements/auth.md#FR-AUTH-001)
  * [FR-AUTH-003 (Tenant SSO Configuration)](../../spec/functional-requirements/auth.md#FR-AUTH-003)
  * [FR-AUTH-004 (Password Reset)](../../spec/functional-requirements/auth.md#FR-AUTH-004)
  * [FR-AUTH-005 (Session Management)](../../spec/functional-requirements/auth.md#FR-AUTH-005)
  * [FR-AUTH-006 (Password Policy Configuration)](../../spec/functional-requirements/auth.md#FR-AUTH-006)
* **Related NFRs**:
  * [NFR-SEC-003 (Multi-Factor Authentication)](../../spec/non-functional-requirements/security.md#NFR-SEC-003)
  * [NFR-SEC-006 (Adaptive Authentication)](../../spec/non-functional-requirements/security.md#NFR-SEC-006)
  * [NFR-CAP-002 (User Scalability)](../../spec/non-functional-requirements/capacity.md#NFR-CAP-002)

<a id="BB-TNT-001"></a>

### Tenant Service

* **Responsibility**: Manages Tenant lifecycle (onboarding, configuration, suspension).
* **Related FRs**:
  * [FR-TENANT-001 (User Invitation)](../../spec/functional-requirements/tenant-admin.md#FR-TENANT-001)
  * [FR-TENANT-002 (User Deletion)](../../spec/functional-requirements/tenant-admin.md#FR-TENANT-002)
  * [FR-TENANT-003 (Contract Modification)](../../spec/functional-requirements/tenant-admin.md#FR-TENANT-003)
  * [FR-TENANT-004 (User Role Management)](../../spec/functional-requirements/tenant-admin.md#FR-TENANT-004)
  * [FR-TENANT-006 (User Status Management)](../../spec/functional-requirements/tenant-admin.md#FR-TENANT-006)
  * [FR-TENANT-007 (Invitation Resend)](../../spec/functional-requirements/tenant-admin.md#FR-TENANT-007)
  * [FR-OPS-001 (Tenant Status Management)](../../spec/functional-requirements/platform-ops.md#FR-OPS-001)
  * [FR-OPS-002 (Tenant Deletion)](../../spec/functional-requirements/platform-ops.md#FR-OPS-002)
  * [FR-SYS-004 (Operator JIT Provisioning)](../../spec/functional-requirements/system-ops.md#FR-SYS-004)
* **Related NFRs**:
  * [NFR-CAP-001 (Tenant Scalability)](../../spec/non-functional-requirements/capacity.md#NFR-CAP-001)
  * [NFR-DATA-001 (Data Residency)](../../spec/non-functional-requirements/data.md#NFR-DATA-001)

<a id="BB-FLG-001"></a>

### Feature Flag Service

* **Responsibility**: Delivers dynamic configuration and feature toggles to the Application.
* **Related FRs**:
  * [FR-FLAG-001 (Flag Configuration)](../../spec/functional-requirements/feature-flags.md#FR-FLAG-001)
  * [FR-FLAG-002 (Flag Delivery)](../../spec/functional-requirements/feature-flags.md#FR-FLAG-002)
* **Related NFRs**:
  * [NFR-PERF-002 (API Latency)](../../spec/non-functional-requirements/performance.md#NFR-PERF-002)

<a id="BB-BIL-001"></a>

### Billing Service

* **Responsibility**: Aggregates usage metrics and interfaces with external Billing System.
* **Related FRs**:
  * [FR-BILL-001 (Billing Event Persistence)](../../spec/functional-requirements/billing.md#FR-BILL-001)
  * [FR-BILL-002 (Billing Event Ingestion)](../../spec/functional-requirements/billing.md#FR-BILL-002)
  * [FR-BILL-003 (Billing Data Export)](../../spec/functional-requirements/billing.md#FR-BILL-003)
* **Related NFRs**:
  * [NFR-OPS-004 (Backup and Redundancy)](../../spec/non-functional-requirements/availability.md#NFR-OPS-004)

<a id="BB-AUD-001"></a>

### Audit Service

* **Responsibility**: Ingests and archives security and operational logs.
* **Related FRs**:
  * [FR-LOG-001 (Audit Log Collection)](../../spec/functional-requirements/audit.md#FR-LOG-001)
  * [FR-LOG-002 (Audit Log Export)](../../spec/functional-requirements/audit.md#FR-LOG-002)
  * [FR-LOG-003 (Control Plane Auditing)](../../spec/functional-requirements/audit.md#FR-LOG-003)
  * **Related NFRs**:

    * [NFR-MON-001 (Continuous Monitoring)](../../spec/non-functional-requirements/monitoring.md#NFR-MON-001)

<a id="BB-OBS-001"></a>

### Observability Platform

* **Responsibility**: Centralized collection and visualization of Metrics, Logs, and Traces. Handles Alerting and Synthetics.
* **Related FRs**:
  * [FR-SYS-005 (System Health Monitoring)](../../spec/functional-requirements/system-ops.md#FR-SYS-005)
* **Related NFRs**:
  * [NFR-MON-002 (System Health Alerting)](../../spec/non-functional-requirements/monitoring.md#NFR-MON-002)
  * [NFR-MON-003 (Synthetic Monitoring)](../../spec/non-functional-requirements/monitoring.md#NFR-MON-003)
  * [NFR-MON-001 (Continuous Monitoring)](../../spec/non-functional-requirements/monitoring.md#NFR-MON-001)

<a id="BB-CICD-001"></a>

### CI/CD Service

* **Responsibility**: Automation of Build, Test, Security Scanning, and Deployment processes.
* **Related NFRs**:
  * [NFR-OPS-001 (Service Level Objective)](../../spec/non-functional-requirements/availability.md#NFR-OPS-001) (Deployment Safety)
* **Decision**: [../../adr/decisions/cicd-platform](../../adr/decisions/cicd-platform.md)

<a id="BB-EVT-001"></a>

### Event Bus

* **Responsibility**: Asynchronous message broker for decoupling services (Publish/Subscribe pattern).
* **Related FRs**:
  * Infrastructure component supporting all Event-Driven FRs.
* **Related NFRs**:
  * [NFR-OPS-003 (Load Balancing and Failover)](../../spec/non-functional-requirements/availability.md#NFR-OPS-003)

## Internal Structure

The internal structure of each microservice follows a standard **Layered / Hexagonal Architecture** to ensure testability and consistency.
For the detailed component pattern, see [../../adr/decisions/architecture-style](../../adr/decisions/architecture-style.md).

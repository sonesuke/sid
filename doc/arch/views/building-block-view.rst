Building Block View
===================

This section decomposes the system into its building blocks (modules, components).
The architecture follows a **Microservices** approach utilizing **Managed Services** (see :doc:`../../adr/decisions/architecture-style`).

Level 1: System Whitebox (Container View)
-----------------------------------------
.. mermaid::
   
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

Component Description
---------------------

.. _BB-UI-001:

*   **[BB-UI-001] Web Console (SPA)**:
    *   **Responsibility**: Single Page Application providing Administrative interfaces for Operators and Tenants.
    *   **Related FRs**:
        *   :ref:`Operator Console <IF-OPS-CONSOLE>`
        *   :ref:`Tenant Administration Console <IF-TENANT-CONSOLE>`
        *   :ref:`Auditor Console <IF-AUDIT-CONSOLE>`
        *   :ref:`Universal Login Page <IF-LOGIN-UI>`
    *   **Related NFRs**:
        *   :ref:`UI Responsiveness <NFR-PERF-003>`

.. _BB-API-001:

*   **[BB-API-001] API Gateway**:
    *   **Responsibility**: Entry point for all external requests. Handles routing, rate limiting, and authentication offloading.
    *   **Related FRs**:

        *   :ref:`API Key Management <FR-SYS-002>`
    *   **Related NFRs**:

        *   :ref:`Load Balancing and Failover <NFR-OPS-003>`
        *   :ref:`Authentication Latency <NFR-PERF-001>`

.. _BB-AUTH-001:

*   **[BB-AUTH-001] Auth Service**:
    *   **Responsibility**: Manages user identities and credentials via External IdP.
    *   **Related FRs**:

        *   :ref:`Supported Authentication Methods <FR-AUTH-001>`
        *   :ref:`Tenant SSO Configuration <FR-AUTH-003>`
        *   :ref:`Password Reset <FR-AUTH-004>`
        *   :ref:`Session Management <FR-AUTH-005>`
        *   :ref:`Password Policy Configuration <FR-AUTH-006>`
    *   **Related NFRs**:

        *   :ref:`Multi-Factor Authentication <NFR-SEC-003>`
        *   :ref:`Adaptive Authentication <NFR-SEC-006>`
        *   :ref:`User Scalability <NFR-CAP-002>`

.. _BB-TNT-001:

*   **[BB-TNT-001] Tenant Service**:
    *   **Responsibility**: Manages Tenant lifecycle (onboarding, configuration, suspension).
    *   **Related FRs**:

        *   :ref:`User Invitation <FR-TENANT-001>`
        *   :ref:`User Deletion <FR-TENANT-002>`
        *   :ref:`Contract Modification <FR-TENANT-003>`
        *   :ref:`User Role Management <FR-TENANT-004>`
        *   :ref:`User Status Management <FR-TENANT-006>`
        *   :ref:`Invitation Resend <FR-TENANT-007>`
        *   :ref:`Tenant Status Management <FR-OPS-001>`
        *   :ref:`Tenant Deletion <FR-OPS-002>`
        *   :ref:`Operator JIT Provisioning <FR-SYS-004>`
    *   **Related NFRs**:

        *   :ref:`Tenant Scalability <NFR-CAP-001>`
        *   :ref:`Data Residency <NFR-DATA-001>`

.. _BB-FLG-001:

*   **[BB-FLG-001] Feature Flag Service**:
    *   **Responsibility**: Delivers dynamic configuration and feature toggles to the Application.
    *   **Related FRs**:

        *   :ref:`Flag Configuration <FR-FLAG-001>`
        *   :ref:`Flag Delivery <FR-FLAG-002>`
    *   **Related NFRs**:

        *   :ref:`API Latency <NFR-PERF-002>`

.. _BB-BIL-001:

*   **[BB-BIL-001] Billing Service**:
    *   **Responsibility**: Aggregates usage metrics and interfaces with external Billing System.
    *   **Related FRs**:

        *   :ref:`Billing Event Persistence <FR-BILL-001>`
        *   :ref:`Billing Event Ingestion <FR-BILL-002>`
        *   :ref:`Billing Data Export <FR-BILL-003>`
    *   **Related NFRs**:

        *   :ref:`Backup and Redundancy <NFR-OPS-004>`

.. _BB-AUD-001:

*   **[BB-AUD-001] Audit Service**:
    *   **Responsibility**: Ingests and archives security and operational logs.
    *   **Related FRs**:

        *   :ref:`Audit Log Collection <FR-LOG-001>`
        *   :ref:`Audit Log Export <FR-LOG-002>`
        *   :ref:`Control Plane Auditing <FR-LOG-003>`
    *   **Related NFRs**:

        *   :ref:`Continuous Monitoring <NFR-MON-001>`

.. _BB-OBS-001:

*   **[BB-OBS-001] Observability Platform**:
    *   **Responsibility**: Centralized collection and visualization of Metrics, Logs, and Traces. Handles Alerting and Synthetics.
    *   **Related FRs**:
        *   :ref:`System Health Monitoring <FR-SYS-005>`
    *   **Related NFRs**:
        *   :ref:`System Health Alerting <NFR-MON-002>`
        *   :ref:`Synthetic Monitoring <NFR-MON-003>`
        *   :ref:`Continuous Monitoring <NFR-MON-001>`

.. _BB-CICD-001:

*   **[BB-CICD-001] CI/CD Service**:
    *   **Responsibility**: Automation of Build, Test, Security Scanning, and Deployment processes.
    *   **Related NFRs**:
        *   :ref:`Availability SLO <NFR-OPS-001>` (Deployment Safety)
    *   **Decision**: :doc:`../../adr/decisions/cicd-platform`

.. _BB-EVT-001:

*   **[BB-EVT-001] Event Bus**:
    *   **Responsibility**: Asynchronous message broker for decoupling services (Publish/Subscribe pattern).
    *   **Related FRs**:

        *   Infrastructure component supporting all Event-Driven FRs.
    *   **Related NFRs**:

        *   :ref:`Load Balancing and Failover <NFR-OPS-003>`

Internal Structure
------------------
The internal structure of each microservice follows a standard **Layered / Hexagonal Architecture** to ensure testability and consistency.
For the detailed component pattern, see :doc:`../../adr/decisions/architecture-style`.

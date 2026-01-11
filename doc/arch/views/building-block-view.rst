Building Block View
===================

This section decomposes the system into its building blocks (modules, components).
The architecture follows a **Microservices** approach utilizing **Managed Services** (see :doc:`../../adr/0006-architecture-style`).

Level 1: System Whitebox (Container View)
-----------------------------------------
.. mermaid::
   
   C4Container
      title Container Diagram for SaaS Foundation Platform (Microservices)

      Person(user, "User", "Accesses via Browser/API")
      
      System_Boundary(c1, "SaaS Foundation Platform") {
         Container(api_gw, "API Gateway", "API Gateway", "Unified Entry Point, Routing, Throttling")
         
         Container(auth_svc, "Auth Service", "Identity Provider / FaaS", "IdP, Token Vending, User Mgmt")
         Container(tenant_svc, "Tenant Service", "FaaS + NoSQL", "Tenant Registration, Config, Lifecycle")
         Container(flag_svc, "Feature Flag Service", "Configuration Service", "Feature Toggles & Rollouts")
         Container(billing_svc, "Billing Service", "FaaS + Event Logic", "Usage Metering, Payment Integration")
         Container(audit_svc, "Audit Service", "Log Aggregator", "Centralized Audit Logging")
         
         Container(event_bus, "Event Bus", "Message Broker", "Asynchronous Event Backbone")
      }

      System_Ext(app, "Managed Application", "Consumes Auth & Flags")

      Rel(user, api_gw, "HTTPS / REST")
      
      Rel(api_gw, auth_svc, "Routes Auth Req")
      Rel(api_gw, tenant_svc, "Routes Tenant Req")
      Rel(api_gw, flag_svc, "Routes Flag Req")
      
      Rel(auth_svc, event_bus, "Publishes User Events")
      Rel(tenant_svc, event_bus, "Publishes Tenant Events")
      Rel(billing_svc, event_bus, "Subscribes to Billable Events")
      Rel(audit_svc, event_bus, "Subscribes to All Events")
      
      Rel(app, api_gw, "Validates Tokens / Fetches Flags")

**Container Responsibilities**:

1. **API Gateway**
   - **Responsibilities**: Entry point for all external traffic. Routes requests to appropriate microservices. Handles rate limiting and initial request validation.
   - **Tech**: API Gateway.

2. **Auth Service**
   - **Responsibilities**: User authentication, credential management, token generation (JWT).
   - **Satisfies**: :ref:`FR-AUTH <FR-AUTH>`.
   - **Tech**: Identity Provider (IdP) / Serverless Function.

3. **Tenant Service**
   - **Responsibilities**: Tenant onboarding, configuration management, subscription tracking.
   - **Satisfies**: :ref:`FR-TENANT <FR-TENANT>`.
   - **Tech**: Serverless Function, NoSQL Store.

4. **Feature Flag Service**
   - **Responsibilities**: Serves feature flag states to applications.
   - **Satisfies**: :ref:`FR-FLAG <FR-FLAG>`.
   - **Tech**: Configuration Management Service.

5. **Billing Service**
   - **Responsibilities**: Aggregates usage data, integrates with external billing providers.
   - **Satisfies**: :ref:`FR-BILL <FR-BILL>`.
   - **Tech**: Event Processing Logic.

6. **Audit Service**
   - **Responsibilities**: Persists audit logs for compliance.
   - **Satisfies**: :ref:`FR-LOG <FR-LOG>`.
   - **Tech**: Log Aggregation & Storage.

7. **Event Bus**
   - **Responsibilities**: Decoupling services. Distributes domain events (e.g., `TenantCreated`, `UserLoggedIn`).
   - **Tech**: Message Broker / Event Bus.

Level 2: Service Component Pattern
----------------------------------
Most microservices in this platform follow a **Event-Driven Service Pattern**.

.. mermaid::
   
   C4Component
      title Generic Microservice Component Diagram

      Container_Boundary(svc, "Microservice Boundary") {
         Component(handler, "API Handler", "Function", "Validates input, calls domain logic")
         Component(logic, "Domain Logic", "Module", "Business rules, State transitions")
         Component(dal, "Data Access Layer", "Module", "Abstracts DB interactions")
         Component(db, "Service Data Store", "NoSQL / SQL", "Private state for this service")
         Component(publisher, "Event Publisher", "Client", "Publishes to Event Bus")
      }

      Rel(handler, logic, "Invokes")
      Rel(logic, dal, "Reads/Writes")
      Rel(dal, db, "Persists State")
      Rel(logic, publisher, "Emits Domain Events")

**Structure**:
- **API Handler**: Entry point (triggered by API Gateway).
- **Domain Logic**: Core business logic, agnostic of infrastructure where possible.
- **Data Access Layer**: Repository pattern to access data stores.
- **Data Store**: Dedicated storage ensuring loose coupling.



Building Block View
===================

This section decomposes the system into its building blocks (modules, components).

Level 1: System Whitebox
------------------------
.. mermaid::
   
   C4Container
      title Container Diagram for SaaS Foundation Platform

      Person(user, "User", "Accesses via Browser/API")
      
      System_Boundary(c1, "SaaS Foundation Platform") {
         Container(api, "Control Plane API", "REST/gRPC", "Handles Tenant & User Management, Auth")
         Container(db, "Core Database", "Relational DB", "Stores Tenant, User, and Config data")
         Container(event_bus, "Event Bus", "Message Queue", "Async events for Audit & Billing")
      }

      System_Ext(app, "Managed Application", "Consumes Auth & Flags")

      Rel(user, api, "Uses", "HTTPS")
      Rel(api, db, "Reads/Writes")
      Rel(api, event_bus, "Publishes Events")
      Rel(app, api, "Validates Tokens")

**Container Responsibilities**:

1. **Control Plane API**
   - **Responsibilities**: Authentication, Tenant Management, Feature Flag distribution.
   - **Satisfies**: :ref:`FR-AUTH <FR-AUTH>`, :ref:`FR-FLAG <FR-FLAG>`.

2. **Core Database**
   - **Responsibilities**: Persistence of normative data models.
   - **Satisfies**: :ref:`Data Persistence NFRs <NFR-DATA>`.

3. **Event Bus**
   - **Responsibilities**: Decoupling critical path from auditing and billing integration.
   - **Satisfies**: :ref:`FR-LOG <FR-LOG>`, :ref:`NFR-PERF <NFR-PERF>`.

Level 2: Component Whitebox
---------------------------
(Deferred to Level 3 design)


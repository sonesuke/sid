Context View
============

This section describes the system's boundaries and interactions with external actors and systems.

System Context Diagram (level 1)
--------------------------------
.. mermaid::
   
   C4Context
      title System Context Diagram for SaaS Foundation Platform

      Person(user, "Tenant User", "Accesses applications via SSO/Auth")
      Person(ops, "Platform Operator", "Manages tenants and system config")
      Person(audit, "Auditor", "Reviews system logs")
      Person(dev, "Developer", "Integrates applications")

      System_Boundary(c1, "SaaS Foundation Platform") {
         System(system, "Control Plane & Auth", "Provides Auth, Feature Flags, and Billing events")
      }

      System_Ext(app, "Managed Application", "B2B SaaS App protected by the platform")
      System_Ext(idp, "External IdP", "Customer's Identity Provider")
      System_Ext(billing, "Billing System", "Processes invoices")

      Rel(user, system, "Authenticates via")
      Rel(user, app, "Uses")
      Rel(ops, system, "Configures")
      Rel(audit, system, "Audits")
      Rel(dev, system, "Registers App")
      Rel(system, billing, "Sends Billable Events")
      Rel(system, idp, "Federates Identity")

External Elements
-----------------
The following actors and systems interact with the SaaS Foundation Platform.

Actors
~~~~~~
.. _CTX-ACT-001:

*   **[CTX-ACT-001] Tenant User**: :ref:`ACT-USER <ACT-USER>`

.. _CTX-ACT-002:

*   **[CTX-ACT-002] Platform Operator**: :ref:`ACT-OPS <ACT-OPS>`

.. _CTX-ACT-003:

*   **[CTX-ACT-003] Auditor**: :ref:`ACT-AUDIT <ACT-AUDIT>`

.. _CTX-ACT-004:

*   **[CTX-ACT-004] Developer**: :ref:`ACT-DEV <ACT-DEV>`

External Systems
~~~~~~~~~~~~~~~~
.. _CTX-EXT-001:

*   **[CTX-EXT-001] Managed Application**: :ref:`TERM-APP-TARGET <TERM-APP-TARGET>`

.. _CTX-EXT-002:

*   **[CTX-EXT-002] External Billing System**: :ref:`ACT-BILLING <ACT-BILLING>`

.. _CTX-EXT-003:

*   **[CTX-EXT-003] External Identity Provider**: OIDC-compliant IdP (e.g., Azure Entra ID).
    *   See :doc:`../../adr/decisions/authentication-provider`.

Scope Boundaries
----------------
- **In-Scope**: Authentication, Feature Flags, Logging (See :doc:`Scope <../../spec/scope/boundaries>`).
- **Out-of-Scope**: Payment Processing, Operator IdP Management.


# Context View

This section describes the system's boundaries and interactions with external actors and systems.

## System Context Diagram (level 1)

```mermaid

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

```

## External Elements

The following actors and systems interact with the SaaS Foundation Platform.

### Actors

<a id="CTX-ACT-001"></a>

#### Tenant User

[ACT-USER (Tenant User)](../../spec/actors/list.md#ACT-USER)

<a id="CTX-ACT-002"></a>

#### Platform Operator

[ACT-OPS (Platform Operator)](../../spec/actors/list.md#ACT-OPS)

<a id="CTX-ACT-003"></a>

#### Auditor

[ACT-AUDIT (Auditor)](../../spec/actors/list.md#ACT-AUDIT)

<a id="CTX-ACT-004"></a>

#### Developer

[ACT-DEV (Developer)](../../spec/actors/list.md#ACT-DEV)

### External Systems

<a id="CTX-EXT-001"></a>

#### Managed Application

[TERM-APP-TARGET (Managed Application)](../../spec/terminology/definitions.md#TERM-APP-TARGET)

<a id="CTX-EXT-002"></a>

#### External Billing System

[ACT-BILLING (External Billing System)](../../spec/actors/list.md#ACT-BILLING)

<a id="CTX-EXT-003"></a>

#### External Identity Provider

OIDC-compliant IdP (e.g., Azure Entra ID).

* See [../../adr/decisions/authentication-provider](../../adr/decisions/authentication-provider.md).

## Scope Boundaries

* **In-Scope**: Authentication, Feature Flags, Logging (See [Scope](../../spec/scope/boundaries.md)).
* **Out-of-Scope**: Payment Processing, Operator IdP Management.

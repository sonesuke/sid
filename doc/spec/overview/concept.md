# Concept

This document outlines the core concept, actors, and scope of the Control Plane System, derived from the initial concept interview.

## Actors

* **Tenant User (TERM-ACTOR-USER)**: A user of the customer (tenant) who accesses the SaaS applications. Uses this system for authentication.
* **Platform Operator (TERM-ACTOR-OPS)**: A service provider user who manages subscriptions, configures tenants, and controls feature flags for the SaaS applications.
* **Auditor (TERM-ACTOR-AUDIT)**: A user responsible for reviewing audit logs provided by the system.

## Scope

## In-Scope

* Issuance of authentication tokens for SaaS applications.
* Delivery of Feature Flags to control application functionality.
* Collection and provision of monitoring and audit logs.
* Recording of billable events/operations.

## Out-of-Scope

* Actual billing and payment processing (e.g., invoice generation, credit card processing via Stripe). These will be handled by an external system based on the recorded events.

## Primary Use Case

## Tenant Provisioning by Platform Operator

The single most critical scenario is where a **Platform Operator** configures a new tenant and immediately makes the subscribed features available for use. This use case validates the core value of the control plane: rapid and centralized onboarding.

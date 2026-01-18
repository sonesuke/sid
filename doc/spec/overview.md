# Project Overview

## Motivation

There is a growing need to manage multiple B2B SaaS applications efficiently. Currently, common control plane elements such as User Management (CIAM), Feature Flag management, and monitoring are fragmented or duplicated across applications.

The goal is to centralize these controls to reduce development and operational costs while ensuring consistency across all managed SaaS products.

## Concept

This document outlines the core concept, actors, and role of the Control Plane System, derived from the initial concept interview.

The system serves as a centralized management foundation for multiple B2B SaaS applications, providing unified authentication, feature control, and auditing capabilities.

### Primary Actors

* **Platform Operator**: Service provider managing subscriptions and tenants.
* **Tenant User**: End-user of the SaaS applications.
* **Auditor**: Reviewer of system operation logs.

## Scope

This section defines the functionalities that are In-Scope and explicitly Out-of-Scope for the project.

### In-Scope

* Issuance of authentication tokens for SaaS applications.
* Delivery of Feature Flags to control application functionality.
* Collection and provision of monitoring and audit logs.
* Recording of billable events/operations.

### Related Regulations

* Japanese Act on the Protection of Personal Information (APPI)
* NIST SP 800-53
* ISO 27001

### Out-of-Scope

* Actual billing and payment processing (e.g., invoice generation, credit card processing via Stripe). These will be handled by an external system based on the recorded events.
* Management of Platform Operator accounts (registration, deletion, identity management). This is delegated to an external Identity Provider (IdP).

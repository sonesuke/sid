# Capacity

<a id="NFR-CAP-001"></a>

## NFR-CAP-001 Tenant Scalability

The system SHALL scale to support a minimum of 1,000 concurrent active [DAT-TENANT (Tenants)](../data-model/schema.md#DAT-TENANT).

**Constrained by**: [CON-CAP-001 (Tenant Capacity)](../constraints-and-assumptions/index.md#CON-CAP-001)

<a id="NFR-CAP-002"></a>

## NFR-CAP-002 User Scalability

The system SHALL scale to support a minimum of 10,000 [DAT-USER (Users)](../data-model/schema.md#DAT-USER) per [DAT-TENANT (Tenants)](../data-model/schema.md#DAT-TENANT).

**Constrained by**: [CON-CAP-002 (User Capacity per Tenant)](../constraints-and-assumptions/index.md#CON-CAP-002)

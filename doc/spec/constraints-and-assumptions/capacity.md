# Capacity Constraints

<a id="CON-CAP-001"></a>

## CON-CAP-001 Tenant Capacity

The system SHALL support a minimum of 1,000 active [DAT-TENANT (Tenants)](../data-model/schema.md#DAT-TENANT).

**Rationale**:

* Business scalability requirement.

**Related NFRs**:

* [NFR-CAP-001 (Tenant Scalability)](../non-functional-requirements/capacity.md#NFR-CAP-001)

<a id="CON-CAP-002"></a>

## CON-CAP-002 User Capacity per Tenant

The system SHALL support a minimum of 10,000 [DAT-USER (Users)](../data-model/schema.md#DAT-USER) per [DAT-TENANT (Tenants)](../data-model/schema.md#DAT-TENANT).

**Rationale**:

* Business scalability requirement.

**Related NFRs**:

* [NFR-CAP-002 (User Scalability)](../non-functional-requirements/capacity.md#NFR-CAP-002)

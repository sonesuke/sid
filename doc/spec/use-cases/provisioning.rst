Primary Use Cases
=================

.. _UC-PROV-001:

UC-PROV-001 Tenant Provisioning
-------------------------------
**Actor**: :ref:`ACT-OPS`

**Description**:
The Platform Operator creates a new tenant configuration and enables subscribed features, allowing the tenant to immediately access the SaaS applications.

**Trigger**:
A new customer subscription is confirmed.

**Preconditions**:
1. The Platform Operator is logged in.

**Postconditions**:
1. A new tenant entity is created in the system.
2. Initial admin user for the tenant is provisioned.
3. Feature flags corresponding to the subscription plan are active.

**Scenario**:
1. Operator navigates to the :ref:`IF-OPS-CONSOLE`.
2. Operator enters tenant details (Name, Domain, Plan).
3. Operator selects the "Provision" action.
4. System creates the tenant and confirms success.

**Related Requirements**:
*   :ref:`FR-FLAG-001`
*   :ref:`FR-TENANT-001`
*   :ref:`FR-TENANT-003`

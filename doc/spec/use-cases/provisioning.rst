Primary Use Cases
=================

.. _UC-PROV-001:

UC-PROV-001 Tenant Provisioning
-------------------------------
**Actor**: :ref:`ACT-OPS`

**Description**:
The :ref:`Platform Operator <ACT-OPS>` creates a new tenant configuration and enables subscribed features, allowing the tenant to immediately access the SaaS applications.

**Trigger**:
A new customer subscription is confirmed.

**Preconditions**:
1. The :ref:`Platform Operator <ACT-OPS>` is logged in.

**Postconditions**:
1. A new tenant entity is created in the :ref:`Control Plane <TERM-SYS-CP>`.
2. Initial admin user for the tenant is provisioned.
3. Feature flags corresponding to the subscription plan are active.

**Scenario**:
1. The :ref:`Platform Operator <ACT-OPS>` navigates to the :ref:`IF-OPS-CONSOLE`.
2. The :ref:`Platform Operator <ACT-OPS>` enters tenant details (Name, Domain, Plan).
3. The :ref:`Platform Operator <ACT-OPS>` selects the "Provision" action.
4. The :ref:`Control Plane <TERM-SYS-CP>` creates the tenant and confirms success.

**Related Requirements**:
*   :ref:`FR-FLAG-001`
*   :ref:`FR-TENANT-001`
*   :ref:`FR-TENANT-003`

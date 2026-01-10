Primary Use Cases
=================

.. _UC-PROV-001:

UC-PROV-001 Tenant Provisioning
-------------------------------
**Actor**: :ref:`ACT-OPS`

**Description**:
The :ref:`Platform Operator <ACT-OPS>` creates a new tenant configuration and enables subscribed features, allowing the tenant to immediately access the :ref:`Managed Application <TERM-APP-TARGET>`.

**Trigger**:
A new customer subscription is confirmed.

**Preconditions**:
1. The :ref:`Platform Operator <ACT-OPS>` is logged in.

**Postconditions**:
1. A new :ref:`Tenant <DAT-TENANT>` entity is created in the :ref:`Control Plane <TERM-SYS-CP>`.
2. Initial :ref:`Tenant User <ACT-USER>` (Role: Owner) is provisioned in the :ref:`Users <DAT-USER>` table.
3. :ref:`Feature Flags <DAT-FLAG>` corresponding to the subscription plan are active.

**Scenario**:
1. The :ref:`Platform Operator <ACT-OPS>` navigates to the :ref:`IF-OPS-CONSOLE`.
2. The :ref:`Platform Operator <ACT-OPS>` enters tenant details (Name, Domain, Plan) and the email address for the initial Owner.
3. The :ref:`Platform Operator <ACT-OPS>` selects the :ref:`Managed Application <TERM-APP-TARGET>` to enable.
4. The :ref:`Platform Operator <ACT-OPS>` selects the "Provision" action.
5. The :ref:`Control Plane <TERM-SYS-CP>` creates the tenant and the initial :ref:`Tenant User <ACT-USER>` (Role: Owner).
6. The :ref:`Control Plane <TERM-SYS-CP>` enables access to the :ref:`Managed Application <TERM-APP-TARGET>`.

**Related Requirements**:
*   :ref:`FR-FLAG-001`
*   :ref:`FR-TENANT-001`
*   :ref:`FR-TENANT-003`
*   :ref:`FR-LOG-003`

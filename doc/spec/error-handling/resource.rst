Resource Errors
===============

.. _ERR-RES-404:

ERR-RES-404 Resource Not Found
------------------------------
**Description**:
The requested resource does not exist.

**Triggers**:

*   Invalid resource ID
*   Resource has been deleted
*   Resource belongs to a different tenant

**Outcome**:

*   Operation is rejected
*   No state change occurs

**Related Requirements**:

*   :ref:`FR-TENANT-002`
*   :ref:`FR-TENANT-004`
*   :ref:`FR-OPS-001`

**Constraints**:

*   :ref:`CON-SEC-009`

.. _ERR-RES-410:

ERR-RES-410 Resource Gone
-------------------------
**Description**:
The resource previously existed but has been permanently deleted.

**Triggers**:

*   Tenant has been deleted (past grace period)
*   Data retention policy applied

**Outcome**:

*   Operation is rejected
*   Resource cannot be recovered

**Related Requirements**:

*   :ref:`FR-OPS-002`
*   :ref:`FR-OPS-003`

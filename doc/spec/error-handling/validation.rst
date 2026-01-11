Validation Errors
=================

.. _ERR-VAL-400:

ERR-VAL-400 Invalid Input
-------------------------
**Description**:
The request contains invalid or malformed input data.

**Triggers**:

*   Missing required fields
*   Invalid data format
*   Value out of allowed range

**Outcome**:

*   Operation is rejected
*   No state change occurs

**Related Requirements**:

*   All FRs accepting user input

.. _ERR-VAL-409:

ERR-VAL-409 Conflict
--------------------
**Description**:
The operation conflicts with existing state.

**Triggers**:

*   Duplicate email address in invitation
*   Attempting to create a resource that already exists
*   Concurrent modification conflict

**Outcome**:

*   Operation is rejected
*   Existing state is preserved

**Related Requirements**:

*   :ref:`FR-TENANT-001`
*   :ref:`FR-SYS-001`

.. _ERR-VAL-422:

ERR-VAL-422 Business Rule Violation
-----------------------------------
**Description**:
The operation violates a business rule or policy.

**Triggers**:

*   Password does not meet complexity requirements
*   Invitation has expired
*   Tenant capacity exceeded

**Outcome**:

*   Operation is rejected
*   No state change occurs

**Related Requirements**:

*   :ref:`FR-AUTH-006`
*   :ref:`FR-TENANT-001`
*   :ref:`FR-TENANT-007`

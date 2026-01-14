# Validation Errors

<a id="ERR-VAL-400"></a>

## ERR-VAL-400 Invalid Input

**Description**:
The request contains invalid or malformed input data.

**Triggers**:

* Missing required fields
* Invalid data format
* Value out of allowed range

**Outcome**:

* Operation is rejected
* No state change occurs

<a id="ERR-VAL-409"></a>

## ERR-VAL-409 Conflict

**Description**:
The operation conflicts with existing state.

**Triggers**:

* Duplicate email address in invitation
* Attempting to create a resource that already exists
* Concurrent modification conflict

**Outcome**:

* Operation is rejected
* Existing state is preserved

<a id="ERR-VAL-422"></a>

## ERR-VAL-422 Business Rule Violation

**Description**:
The operation violates a business rule or policy.

**Triggers**:

* Password does not meet complexity requirements
* Invitation has expired
* Tenant capacity exceeded

**Outcome**:

* Operation is rejected
* No state change occurs

# Resource Errors

<a id="ERR-RES-404"></a>

## ERR-RES-404 Resource Not Found

**Description**:
The requested resource does not exist.

**Triggers**:

* Invalid resource ID
* Resource has been deleted
* Resource belongs to a different tenant

**Outcome**:

* Operation is rejected
* No state change occurs

<a id="ERR-RES-410"></a>

## ERR-RES-410 Resource Gone

**Description**:
The resource previously existed but has been permanently deleted.

**Triggers**:

* Tenant has been deleted (past grace period)
* Data retention policy applied

**Outcome**:

* Operation is rejected
* Resource cannot be recovered

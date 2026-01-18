# System Errors

<a id="ERR-SYS-500"></a>

## ERR-SYS-500 Internal Error

**Description**:
An unexpected internal error occurred.

**Triggers**:

* Unhandled exception
* Database connection failure
* Dependency service unavailable

**Outcome**:

* Operation fails
* State may be inconsistent (should be recoverable)

<a id="ERR-SYS-503"></a>

## ERR-SYS-503 Service Unavailable

**Description**:
The service is temporarily unavailable.

**Triggers**:

* Scheduled maintenance
* System overload
* Failover in progress

**Outcome**:

* Operation is rejected
* Client should retry later

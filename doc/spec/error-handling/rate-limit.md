# Rate Limit Errors

<a id="ERR-RATE-429"></a>

## ERR-RATE-429 Rate Limit Exceeded

**Description**:
The client has exceeded the allowed request rate.

**Triggers**:

* Too many requests in a short period
* Authentication attempt rate limiting
* API call quota exceeded

**Outcome**:

* Current request is rejected
* Client should wait and retry

**Constraints**:

* [CON-PERF-001 (Response Time and Throughput)](../constraints-and-assumptions/index.md#CON-PERF-001)

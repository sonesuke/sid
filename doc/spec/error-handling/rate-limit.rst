Rate Limit Errors
=================

.. _ERR-RATE-429:

ERR-RATE-429 Rate Limit Exceeded
--------------------------------
**Description**:
The client has exceeded the allowed request rate.

**Triggers**:

*   Too many requests in a short period
*   Authentication attempt rate limiting
*   API call quota exceeded

**Outcome**:

*   Current request is rejected
*   Client should wait and retry

**Constraints**:

*   :ref:`Response Time and Throughput <CON-PERF-001>`

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

**Related Requirements**:

*   :ref:`FR-AUTH-001`
*   :ref:`FR-BILL-002`
*   :ref:`FR-FLAG-002`

**Constraints**:

*   :ref:`CON-PERF-001`

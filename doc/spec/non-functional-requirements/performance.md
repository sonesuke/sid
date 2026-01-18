# Performance

<a id="NFR-PERF-001"></a>

## NFR-PERF-001 Authentication Latency

Authentication requests SHALL complete within the following latency targets:

* P95 (95th percentile): < 1000ms
* P99 (99th percentile): < 2000ms

This includes password verification, OIDC/SSO flows, and MFA validation.

<a id="NFR-PERF-002"></a>

## NFR-PERF-002 API Latency

General API requests SHALL complete within the following latency targets:

* P95 (95th percentile): < 500ms
* P99 (99th percentile): < 1000ms

<a id="NFR-PERF-003"></a>

## NFR-PERF-003 UI Responsiveness

User interface interactions SHALL provide feedback within the following targets:

* Page transitions: < 2 seconds
* Interactive elements: < 400ms perceived response

<a id="NFR-PERF-004"></a>

## NFR-PERF-004 Authentication Throughput

The authentication system SHALL support a minimum throughput of:

* 5,000 authentication requests per second (RPS)

This ensures capacity for peak login periods across all tenants.

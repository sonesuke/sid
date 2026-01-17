# [ADR-ARCH-002] Service Communication Pattern (Sync vs Async)

## Context and Problem Statement

The system consists of a Control Plane and potentially distributed managed applications or agents.
We need to decide how these components communicate, specifically balancing coupling, latency, and reliability.

### Decision Drivers

* Loose coupling between services
* Latency requirements for user-facing actions
* System resilience and handling of downtime
* Complexity of operations

## Considered Options

* Synchronous REST/gRPC only
* Asynchronous Messaging (Event-driven) primarily
* Hybrid (Sync for queries, Async for mutations)

## Decision Outcome

### Positive Consequences

* ...

### Negative Consequences

* ...

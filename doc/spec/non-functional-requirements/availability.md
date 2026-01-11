# Availability

<a id="NFR-OPS-001"></a>

## NFR-OPS-001 Service Level Objective
The system SHALL maintain 99.9% availability, excluding scheduled maintenance windows.

**Constrained by**: [CON-OPS-001](../constraints-and-assumptions/index.md#CON-OPS-001)

<a id="NFR-OPS-002"></a>

## NFR-OPS-002 Maintenance Scheduling
Scheduled maintenance windows SHALL be defined and communicated to stakeholders in advance. (Details TBD)

**Constrained by**: [CON-OPS-002](../constraints-and-assumptions/index.md#CON-OPS-002)

<a id="NFR-OPS-003"></a>

## NFR-OPS-003 Load Balancing and Failover
The system SHALL implement:

*   Load balancing to distribute traffic across multiple instances.
*   Automatic failover to prevent single points of failure.
*   Geographic redundancy where feasible.

**Constrained by**: [CON-OPS-003](../constraints-and-assumptions/index.md#CON-OPS-003)

<a id="NFR-OPS-004"></a>

## NFR-OPS-004 Backup and Redundancy
The system SHALL implement backup and recovery capabilities:

*   Automated regular backups (at least daily).
*   3-2-1 backup rule (3 copies, 2 different media, 1 offsite).
*   Backup encryption.
*   Regular restore testing (at least annually).

**Constrained by**: [CON-OPS-004](../constraints-and-assumptions/index.md#CON-OPS-004)

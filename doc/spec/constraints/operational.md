# Operational Constraints

<a id="CON-OPS-SLO"></a>

## CON-OPS-SLO Availability SLO

The system SHALL target a Service Level Objective (SLO) of 99.9% availability, excluding scheduled maintenance windows.

**Rationale**:

* Business continuity requirement.

**Related NFRs**:

* [NFR-OPS-001 (Service Level Objective)](../non-functional-requirements/availability.md#NFR-OPS-001)

<a id="CON-OPS-MAINTENANCE"></a>

## CON-OPS-MAINTENANCE Maintenance Window

Scheduled maintenance windows SHALL be defined and communicated in advance. (Details TBD)

**Rationale**:

* Operational planning.

**Related NFRs**:

* [NFR-OPS-002 (Maintenance Scheduling)](../non-functional-requirements/availability.md#NFR-OPS-002)

<a id="CON-OPS-FAILOVER"></a>

## CON-OPS-FAILOVER Load Balancing and Failover

The system SHALL implement load balancing and automatic failover.

**Rationale**:

* NIST CSF 2.0 - Availability.

**Related NFRs**:

* [NFR-OPS-003 (Load Balancing and Failover)](../non-functional-requirements/availability.md#NFR-OPS-003)

<a id="CON-OPS-BACKUP"></a>

## CON-OPS-BACKUP Backup and Redundancy

The system SHALL implement backup and recovery capabilities following the 3-2-1 rule.

**Rationale**:

* NIST CSF 2.0 - Recovery.

**Related NFRs**:

* [NFR-OPS-004 (Backup and Redundancy)](../non-functional-requirements/availability.md#NFR-OPS-004)

Availability
============

.. _NFR-OPS-001:

NFR-OPS-001 Service Level Objective
-----------------------------------
The system SHALL maintain 99.9% availability, excluding scheduled maintenance windows.

**Constrained by**: :ref:`CON-OPS-001`

.. _NFR-OPS-002:

NFR-OPS-002 Maintenance Scheduling
----------------------------------
Scheduled maintenance windows SHALL be defined and communicated to stakeholders in advance. (Details TBD)

**Constrained by**: :ref:`CON-OPS-002`

.. _NFR-OPS-003:

NFR-OPS-003 Load Balancing and Failover
---------------------------------------
The system SHALL implement:

*   Load balancing to distribute traffic across multiple instances.
*   Automatic failover to prevent single points of failure.
*   Geographic redundancy where feasible.

**Constrained by**: :ref:`CON-OPS-003`

.. _NFR-OPS-004:

NFR-OPS-004 Backup and Redundancy
---------------------------------
The system SHALL implement backup and recovery capabilities:

*   Automated regular backups (at least daily).
*   3-2-1 backup rule (3 copies, 2 different media, 1 offsite).
*   Backup encryption.
*   Regular restore testing (at least annually).

**Constrained by**: :ref:`CON-OPS-004`

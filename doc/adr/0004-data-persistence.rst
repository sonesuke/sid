ADR-0004: Data Persistence Strategy
===================================

* Status: Proposed
* Deciders: Project Team
* Date: 2026-01-11

Context and Problem Statement
-----------------------------
We need to select the primary data storage technology for the Core Database (Tenants, Users, Config).
The data is highly relational and requires strong consistency (ACID) for billing and provisioning critical paths.

Decision Drivers
~~~~~~~~~~~~~~~~
* ACID compliance
* Relational data integrity (Foreign Keys)
* Cloud provider support (Managed Services)
* Scalability requirements

Considered Options
------------------
* PostgreSQL
* MySQL / MariaDB
* NoSQL (MongoDB, DynamoDB)

Decision Outcome
----------------
[Proposed]: PostgreSQL

Positive Consequences
~~~~~~~~~~~~~~~~~~~~~
* Strong strict consistency
* Rich ecosystem (JSONB support, extensions)

Negative Consequences
~~~~~~~~~~~~~~~~~~~~~
* Vertical scaling limits compared to NoSQL

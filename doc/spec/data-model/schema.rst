Schema Definitions
==================

This section defines the core data entities managed by the :ref:`Control Plane <TERM-SYS-CP>`.

.. _DAT-TENANT:

Tenants
-------
Represents a customer organization subscribed to the :ref:`Managed Application <TERM-APP-TARGET>`.

.. list-table::
   :header-rows: 1
   :widths: 20 20 60

   * - Field
     - Type
     - Description
   * - ``id``
     - UUID
     - Unique identifier for the tenant.
   * - ``name``
     - String
     - Display name of the organization.
   * - ``domain``
     - String
     - Unique domain identifier for the tenant (e.g., ``acme``).
   * - ``plan``
     - Enum
     - Subscription plan (e.g., ``Free``, ``Pro``, ``Enterprise``).
   * - ``status``
     - Enum
     - Account status (``Active``, ``Suspended``).
   * - ``created_at``
     - Timestamp
     - Record creation time.

.. _DAT-USER:

Users
-----
Represents an individual user belonging to a :ref:`Tenant <DAT-TENANT>` or the Platform.

.. list-table::
   :header-rows: 1
   :widths: 20 20 60

   * - Field
     - Type
     - Description
   * - ``id``
     - UUID
     - Unique identifier for the user.
   * - ``tenant_id``
     - UUID
     - Foreign Key to :ref:`Tenants <DAT-TENANT>`. Null for Platform Operators.
   * - ``email``
     - String
     - Unique email address used for login.
   * - ``role``
     - Enum
     - Access level (:ref:`DAT-ROLE`).
   * - ``status``
     - Enum
     - User status (``Invited``, ``Active``, ``Disabled``).

.. _DAT-ROLE:

Roles
-----
Enumeration of defined user roles.

*   **Owner**: Full access to tenant configuration, billing, and user management.
*   **Administrator**: Access to user management and tenant configuration (excluding billing).
*   **User**: Access to the :ref:`Managed Application <TERM-APP-TARGET>` features only.
*   **Operator**: (Platform level) Full access to the :ref:`Control Plane <TERM-SYS-CP>`.

.. _DAT-FLAG:

Feature Flags
-------------
Controls the availability of features for specific tenants.

.. list-table::
   :header-rows: 1
   :widths: 20 20 60

   * - Field
     - Type
     - Description
   * - ``id``
     - UUID
     - Unique identifier.
   * - ``tenant_id``
     - UUID
     - Foreign Key to :ref:`Tenants <DAT-TENANT>`.
   * - ``key``
     - String
     - Feature identifier (e.g., ``ai_module_enabled``).
   * - ``value``
     - Boolean
     - State of the feature (True/False).

.. _DAT-LOG:

Audit Logs
----------
Immutable record of system events for security and compliance.

.. list-table::
   :header-rows: 1
   :widths: 20 20 60

   * - Field
     - Type
     - Description
   * - ``id``
     - UUID
     - Unique identifier.
   * - ``timestamp``
     - Timestamp
     - Time when the event occurred.
   * - ``actor_id``
     - String
     - ID of the user or system component initiating the action.
   * - ``actor_type``
     - Enum
     - Type of actor (``User``, ``Operator``, ``System``).
   * - ``action``
     - String
     - Description of the operation (e.g., ``tenant.create``).
   * - ``resource``
     - String
     - Identifier of the target resource.
   * - ``outcome``
     - Enum
     - Result of the operation (``Success``, ``Failure``).
   * - ``metadata``
     - JSON
     - Additional context (e.g., previous values, IP address).

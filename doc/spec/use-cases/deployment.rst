System Deployment
=================

.. _UC-DEV-REGISTER:

UC-DEV-REGISTER Application Registration
----------------------------------------
**Actor**: :ref:`Developer <ACT-DEV>`

**Description**:
The :ref:`Developer <ACT-DEV>` registers the :ref:`Managed Application <TERM-APP-TARGET>` with the Control Plane to obtain credentials for API access. This is typically done as part of the initial system deployment.

**Trigger**:
The :ref:`Developer <ACT-DEV>` initiates the "Register System" workflow (via CLI or script).

**Preconditions**:

1. The :ref:`Developer <ACT-DEV>` has administrative access to the Control Plane infrastructure.

**Postconditions**:

1. A :ref:`Managed Application <DAT-APP>` record is created.
2. An :ref:`API Access Key <DAT-KEY>` is issued and returned to the :ref:`Developer <ACT-DEV>`.
3. The :ref:`Managed Application <TERM-APP-TARGET>` is configured with the key.

**Scenario**:

1. The :ref:`Developer <ACT-DEV>` submits the application metadata (Name, Environment).
2. The :ref:`Control Plane <TERM-SYS-CP>` creates the application record.
3. The :ref:`Control Plane <TERM-SYS-CP>` generates a client ID and secret.
4. The :ref:`Control Plane <TERM-SYS-CP>` stores the hashed secret.
5. The :ref:`Control Plane <TERM-SYS-CP>` returns the ID and Secret to the :ref:`Developer <ACT-DEV>`.

**Related Requirements**:

*   :ref:`Application Registration <FR-SYS-001>`
*   :ref:`API Key Management <FR-SYS-002>`

.. _UC-DEV-UPDATE:

UC-DEV-UPDATE Application Update
--------------------------------
**Actor**: :ref:`Developer <ACT-DEV>`

**Description**:
The :ref:`Developer <ACT-DEV>` updates the configuration or status of a :ref:`Managed Application <DAT-APP>`. This includes disabling the application to prevent access.

**Trigger**:
The :ref:`Developer <ACT-DEV>` initiates a deployment or CLI command to update the application.

**Preconditions**:

1. The :ref:`Developer <ACT-DEV>` has valid administrative credentials.
2. The target :ref:`Managed Application <DAT-APP>` exists.

**Postconditions**:

1. The :ref:`Managed Application <DAT-APP>` record is updated.
2. If status is set to Disabled, all API access is blocked.

**Scenario**:

1. The :ref:`Developer <ACT-DEV>` submits the update request (e.g., set status to Disabled).
2. The :ref:`Control Plane <TERM-SYS-CP>` validates the request.
3. The :ref:`Control Plane <TERM-SYS-CP>` updates the application record.
4. The :ref:`Control Plane <TERM-SYS-CP>` applies the new state (e.g., blocking incoming API calls).

**Related Requirements**:

*   :ref:`Application Lifecycle Management <FR-SYS-003>`

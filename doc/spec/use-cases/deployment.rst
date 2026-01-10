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

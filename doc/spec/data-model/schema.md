# Schema Definitions

This section defines the core data entities managed by the [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP).

<a id="DAT-TENANT"></a>

## Tenants

Represents a customer organization subscribed to the [TERM-APP-TARGET (Managed Application)](../terminology/definitions.md#TERM-APP-TARGET).

| Field | Type | Description |
|-------|------|-------------|
| id | UUID | Unique identifier for the tenant. |
| name | String | Display name of the organization. |
| domain | String | Unique domain identifier for the tenant (e.g., `acme`). |
| plan | Enum | Subscription plan (e.g., `Free`, `Pro`, `Enterprise`). |
| status | Enum | Account status (`Active`, `Suspended`). |
| created_at | Timestamp | Record creation time. |

<a id="DAT-USER"></a>

## Users

Represents an individual user belonging to a [DAT-TENANT (Tenants)](#DAT-TENANT) or the Platform.

| Field | Type | Description |
|-------|------|-------------|
| id | UUID | Unique identifier for the user. |
| tenant_id | UUID | Foreign Key to [DAT-TENANT (Tenants)](#DAT-TENANT). Null for Platform Operators. |
| email | String | Unique email address used for login. |
| role | Enum | Access level ([DAT-ROLE (Roles)](#DAT-ROLE)). |
| status | Enum | User status (`Invited`, `Active`, `Disabled`). |

<a id="DAT-ROLE"></a>

## Roles

Enumeration of defined user roles.

* **Owner**: Full access to tenant configuration, billing, and user management.
* **Administrator**: Access to user management and tenant configuration (excluding billing).
* **User**: Access to the [TERM-APP-TARGET (Managed Application)](../terminology/definitions.md#TERM-APP-TARGET) features only.
* **Operator**: (Platform level) Full access to the [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP).

<a id="DAT-FLAG"></a>

## Feature Flags

Controls the availability of features for specific tenants.

| Field | Type | Description |
|-------|------|-------------|
| id | UUID | Unique identifier. |
| tenant_id | UUID | Foreign Key to [DAT-TENANT (Tenants)](#DAT-TENANT). |
| key | String | Feature identifier (e.g., `ai_module_enabled`). |
| value | Boolean | State of the feature (True/False). |

<a id="DAT-LOG"></a>

## Audit Logs

Immutable record of system events for security and compliance.

| Field | Type | Description |
|-------|------|-------------|
| id | UUID | Unique identifier. |
| timestamp | Timestamp | Time when the event occurred. |
| actor_id | String | ID of the user or system component initiating the action. |
| actor_type | Enum | Type of actor (`User`, `Operator`, `System`). |
| action | String | Description of the operation (e.g., `tenant.create`). |
| resource | String | Identifier of the target resource. |
| outcome | Enum | Result of the operation (`Success`, `Failure`). |
| metadata | JSON | Additional context (e.g., previous values, IP address). |

<a id="DAT-APP"></a>

## Managed Applications

Represents a registered [TERM-APP-TARGET (Managed Application)](../terminology/definitions.md#TERM-APP-TARGET) instance that interacts with the Platform APIs.

| Field | Type | Description |
|-------|------|-------------|
| id | UUID | Unique identifier. |
| name | String | Name of the application. |
| owner_id | String | Identifier of the [ACT-DEV (Developer)](../actors/list.md#ACT-DEV) or owner. |
| status | Enum | Registration status (`Active`, `Disabled`). |

<a id="DAT-KEY"></a>

## API Access Keys

Credentials used by [DAT-APP (Managed Applications)](#DAT-APP) to authenticate against [TERM-SYS-CP (Control Plane)](../terminology/definitions.md#TERM-SYS-CP) APIs.

| Field | Type | Description |
|-------|------|-------------|
| id | UUID | Unique key identifier (KID). |
| app_id | UUID | Foreign Key to [DAT-APP (Managed Applications)](#DAT-APP). |
| key_hash | String | Secure hash of the API Secret. |
| scopes | String[] | List of allowed API scopes (e.g., `bill:write`, `log:write`). |
| created_at | Timestamp | Issuance time. |
| expires_at | Timestamp | Expiration time (optional). |

<a id="DAT-SSO-CONFIG"></a>

## SSO Configuration

Stores the Identity Provider details for a [DAT-TENANT (Tenants)](#DAT-TENANT).

| Field | Type | Description |
|-------|------|-------------|
| id | UUID | Unique identifier. |
| tenant_id | UUID | Foreign Key to [DAT-TENANT (Tenants)](#DAT-TENANT). |
| issuer_url | String | OIDC Issuer URL. |
| client_id | String | Client Identifier at IdP. |
| secret | String | Encrypted Client Secret. |
| created_at | Timestamp | Configuration time. |

<a id="DAT-INVITE"></a>

## User Invitations

Tracks pending invitations for new users.

| Field | Type | Description |
|-------|------|-------------|
| id | UUID | Unique identifier. |
| tenant_id | UUID | Foreign Key to [DAT-TENANT (Tenants)](#DAT-TENANT). |
| email | String | Target email address. |
| role | Enum | Proposed role ([DAT-ROLE (Roles)](#DAT-ROLE)). |
| token | String | Unique token sent via email. |
| expires_at | Timestamp | Token expiration time. |
| status | Enum | Invitation status (`Pending`, `Accepted`, `Expired`). |

<a id="DAT-BILL-EVENT"></a>

## Billing Events

Raw records of billable activities reported by applications.

| Field | Type | Description |
|-------|------|-------------|
| id | UUID | Unique identifier. |
| tenant_id | UUID | Foreign Key to [DAT-TENANT (Tenants)](#DAT-TENANT). |
| app_id | UUID | Foreign Key to [DAT-APP (Managed Applications)](#DAT-APP). |
| event_type | String | Type of billable action (e.g., `api_call`, `storage_gb`). |
| quantity | Integer | Amount consumed. |
| timestamp | Timestamp | Event occurrence time. |

<a id="DAT-SESSION"></a>

## User Sessions

Represents an active login session for a [DAT-USER (Users)](#DAT-USER).

| Field | Type | Description |
|-------|------|-------------|
| id | UUID | Unique identifier for the session. |
| user_id | UUID | Foreign Key to [DAT-USER (Users)](#DAT-USER). |
| token | String | Secure session token or JWT reference. |
| created_at | Timestamp | Session creation time. |
| expires_at | Timestamp | Session expiration time. |
| status | Enum | Session status (`Active`, `Revoked`). |

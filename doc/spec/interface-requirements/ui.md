# User Interfaces

This section defines the primary User Interfaces (UI) provided by the Control Plane.

<a id="IF-OPS-CONSOLE"></a>

## IF-OPS-CONSOLE Operator Console

**User**: [ACT-OPS (Platform Operator)](../actors/list.md#ACT-OPS)
**Description**:
The administrative web portal for Platform Operators.
Provides capabilities for tenant provisioning, feature flag management, and system monitoring.

<a id="IF-TENANT-CONSOLE"></a>

## IF-TENANT-CONSOLE Tenant Administration Console

**User**: [ACT-USER (Tenant User)](../actors/list.md#ACT-USER) (Owner, Admin)
**Description**:
The self-service web portal for Tenant Administrators.
Provides capabilities to list users, manage roles and status (e.g., Disable), revoke sessions, send invitations, configure SSO, and view subscription details.

<a id="IF-AUDIT-CONSOLE"></a>

## IF-AUDIT-CONSOLE Auditor Console

**User**: [ACT-AUDIT (Auditor)](../actors/list.md#ACT-AUDIT)
**Description**:
The compliance and observation portal for Auditors.
Provides read-only access to system audit logs and reporting capabilities.

<a id="IF-LOGIN-UI"></a>

## IF-LOGIN-UI Universal Login Page

**User**: [ACT-USER (Tenant User)](../actors/list.md#ACT-USER), [ACT-OPS (Platform Operator)](../actors/list.md#ACT-OPS), [ACT-AUDIT (Auditor)](../actors/list.md#ACT-AUDIT)
**Description**:
The centralized login page presented to all users.
Supports input for Email/Password, redirects for SSO/OIDC authentication, and provides access to password reset workflows.

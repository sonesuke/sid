# [ADR-OPS-002] CI/CD Platform Selection

## Context and Problem Statement

We need a Continuous Integration and Continuous Deployment (CI/CD) platform to automate the build, test, and release processes of our Serverless application.
The platform must enable our "Build Once, Deploy Many" principle and integrate seamlessly with our source control.

### Decision Drivers

* **Integration**: Tight integration with Source Code Management (Pull Requests, Code Review).
* **Maintenance**: Minimal operational overhead (SaaS preferred).
* **Security**: Secure handling of Cloud Provider credentials (OIDC).
* **Parallelism**: efficient execution of concurrent test suites.

## Considered Options

* **GitHub Actions** (SaaS)
* **GitLab CI** (SaaS/Self-hosted)
* **Jenkins** (Self-hosted)
* **AWS CodePipeline/CodeBuild** (AWS Native)

## Decision Outcome

**Chosen Option**: **GitHub Actions**

**Justification**:
GitHub Actions is the natural choice as our code resides in GitHub.

1. **Unified Experience**: CI/CD workflows are defined in the same repository (`.github/workflows`) and results are visible directly in Pull Requests.
2. **Security**: Native support for **OIDC (OpenID Connect)** allows us to authenticate with AWS/Azure without storing long-lived access keys (Keyless Authentication).
3. **NoOps**: Fully managed SaaS runners eliminate the need to maintain build servers (unlike Jenkins).
4. **Ecosystem**: Extensive marketplace of Actions simplifies tasks like "Setup Python", "Login to AWS", "Terraform Apply".

### Positive Consequences

* **Developer Velocity**: Fast feedback loops on PRs.
* **Security**: Reduced attack surface via OIDC.
* **Simplicity**: Single pane of glass for Code and Pipeline.

### Negative Consequences

* **Vendor Lock-in**: Workflow syntax is specific to GitHub.
* **Limits**: SaaS concurrency limits may require upgrading plans (handled via scaling to self-hosted runners if needed).

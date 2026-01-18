# Data Constraints

<a id="CON-DATA-RESIDENCY"></a>

## CON-DATA-RESIDENCY Data Residency

All customer data SHALL be stored exclusively in data centers located in Japan or the European Union.

**Rationale**:

* GDPR / APPI - Cross-border data transfer restrictions.

**Related NFRs**:

* [NFR-DATA-001 (Data Residency)](../non-functional-requirements/data.md#NFR-DATA-001)

<a id="CON-DATA-AUDIT-RETENTION"></a>

## CON-DATA-AUDIT-RETENTION Audit Log Retention

[DAT-LOG (Audit Logs)](../data-model/schema.md#DAT-LOG) SHALL be retained for a minimum of 7 years to comply with Japanese accounting laws and APPI requirements.

**Rationale**:

* Legal compliance (Japan Accounting Law, APPI).

**Related FRs**:

* [FR-OPS-003 (Data Retention Enforcement)](../functional-requirements/platform-ops.md#FR-OPS-003)

<a id="CON-DATA-BILLING-RETENTION"></a>

## CON-DATA-BILLING-RETENTION Billing Data Retention

[DAT-BILL-EVENT (Billing Events)](../data-model/schema.md#DAT-BILL-EVENT) SHALL be retained for a minimum of 5 years to comply with tax regulations.

**Rationale**:

* Legal compliance (Tax regulations).

**Related FRs**:

* [FR-OPS-003 (Data Retention Enforcement)](../functional-requirements/platform-ops.md#FR-OPS-003)

# Lab 8: Understand policy types and tuning controls

**Environment:** FORTINETAPACDEMO. **Access:** Read/write.

## Objectives

Find every category in Policy Manager. Identify which controls apply to each category.
Prepare a tuning decision before making a change.

## Prerequisites

Complete Labs 2 and 7. Use your participant ID for any new object.
Screenshots use the demo tenant. Perform configuration work only in the sandpit.

## Lab steps

### Step 1: Map the catalog

1. Confirm **FORTINETAPACDEMO**.
2. Open **Policy Manager > Policies**.
3. Open the **Risk** selector.
4. Inspect **Compliance**, **Vuln Build time**, and **Vuln Run time**.
5. Inspect **Data** if that category is available in your tenant.
6. Open the **Threats** selector.
7. Inspect **Anomalies**, **Threat Observations**, and **Composite Alerts**.

![Policy Catalog categories](images/policy-catalog.png)

**Checkpoint:** Locate the available categories. Record any category unavailable to your role or tenant.
The demo tenant includes Data policies. The sandpit may expose a different set.

![Data policy catalog](images/data-policies.png)

Enabling a Data policy can initiate a rescan for configured DSPM integrations.
Keep Data policies unchanged during this review.

### Step 2: Build a tuning record

Open one policy in each category. Record the controls that the current interface exposes.

| Category | Review focus |
|---|---|
| Compliance | Query, severity, assessed resource condition, and remediation |
| Vuln Build time | Image assessment criteria and build context |
| Vuln Run time | Workload vulnerability criteria and runtime context |
| Data | Data security condition, affected data assets, and available controls |
| Anomalies | Detected deviation, domain, and available tuning controls |
| Threat Observations | Observation definition, entities, and available tuning controls |
| Composite Alerts | Correlated activity, investigation context, and available tuning controls |

**Checkpoint:** For each category, distinguish editable fields from descriptive information.

For **Vuln Build time**, inspect **Critical, fixable CVEs**.
Its Details page shows **Action on failure** and container registry scope.
Its Query page shows CVE count, severity, and fixability criteria.

![Build-time vulnerability policy criteria](images/build-policy-query.png)

For **Vuln Run time**, inspect **New Security Vulnerability**.
Compare its Details and Query tabs with the build-time policy.
Record the visible **Frequency**, severity, and query conditions.

![Runtime vulnerability policy criteria](images/runtime-policy-query.png)

Prepare one build-time change to CVE criteria and one runtime change to frequency or criteria.
Use **Clone** for a sandpit trial when that control is available.
Keep the original managed policy unchanged. Review the clone's state and scope before saving.

For **Composite Alerts**, open **Potentially Compromised Host**.
Read its description and contributing-observation model.
The Details page shows severity and status. Its Edit and Clone controls are disabled.
Do not treat a composite policy as an editable LQL query.

![Composite policy details](images/composite-policy.png)

For **Anomalies**, inspect **New External Server IP Address Connection From Vulnerable Application**.
Its Details page shows frequency, severity, domain, and type.
Its Query tab states **No filter defined** for this managed policy.
Check whether **Clone** is available.

![Anomaly policy query view](images/anomaly-query.png)

For **Threat Observations**, open **Anomalous AssumeRole request.** if that example is available.
Read the description, false positive notes, triage, and remediation sections.
The definition has disabled Edit and Clone controls.
Use this guidance during an investigation.

![Threat observation definition](images/threat-observation.png)

### Step 3: Compare tuning actions

| Action | Question to answer first |
|---|---|
| Change severity | Does business impact justify a different priority? |
| Change query criteria | Which resources should match, and which should not? |
| Add an exception | What exact scope and expiry are justified? |
| Change alert routing | Which team needs this alert? |
| Disable a policy | What detection or assessment coverage would be lost? |

Write one proposed change for each category. Include the scope and verification method.
Keep existing policies unchanged during this review.

**Checkpoint:** Your proposal explains the expected result and the risk of hiding useful evidence.

### Step 4: Inspect custom policy choices

1. Return to **Risk: Compliance**.
2. Click **Add policy**.
3. Compare **Advanced (LQL)** with **Guided Builder (QBL)**.
4. Inspect **Policy type**.
5. Close the form without saving.

![Custom policy form with query language choices](images/policy-builder.png)

The form offers Compliance and Violation for the LQL path.
The QBL path fixes the policy type to Compliance.
A new QBL policy creates a corresponding Risk Insight within about six hours.
Continue the lab while it is processed.

**Checkpoint:** Explain why choosing a query language does not select every policy category in the catalog.

---
Next: [Lab 9: Build and test a custom query and policy](../lab-09/README.md).

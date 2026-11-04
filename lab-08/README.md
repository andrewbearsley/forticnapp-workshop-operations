# Lab 8: Choose the right policy control

**Environment:** FORTINETAPACDEMO. **Access:** Read-only review.

## Concepts

Tuning starts with the problem you want to solve: too many matches, the wrong priority, or the wrong recipients.
Policy categories evaluate different evidence and expose different controls.
A compliance query tests resource configuration. A composite policy combines observations for investigation.
Choose a control that addresses the problem without hiding useful evidence.

## Objectives

- Compare the available controls across all seven policy categories.
- Propose one tuning change and explain its expected result.

## Prerequisites

Complete Labs 2 and 7.
Screenshots use the demo tenant. Review sandpit policies without changing them.

## Lab steps

### Step 1: Map the catalog

1. Confirm **FORTINETAPACDEMO**.
2. Open **Policy Manager > Policies**.
3. Open the **Risk** selector.
4. Locate **Compliance**, **Vuln Build time**, **Vuln Run time**, and **Data** if available.
5. Open the **Threats** selector.
6. Locate **Anomalies**, **Threat Observations**, and **Composite Alerts**.

![Policy Catalog categories](images/policy-catalog.png)

Use the policy table in [your worksheet](../evidence-worksheet.md) if it helps you compare the controls.
At the end, you will choose one policy and propose a useful change.

**Checkpoint:** A team wants to review vulnerability criteria. Which category would you open?
Where would you look for the definition behind your composite alert?

### Step 2: Review a compliance policy

1. Open **Risk: Compliance**.
2. Select a policy that you examined in Lab 7.
3. Read its assessed condition, severity, and remediation.
4. Inspect the available editing controls without saving.

**Checkpoint:** Would raising this policy's severity fix the resource configuration?
Point to the condition that would still need remediation.

### Step 3: Compare vulnerability policies

1. Open **Vuln Build time**.
2. Select **Critical, fixable CVEs**.
3. Read **Action on failure** and the container registry scope in **Details**.
4. Open **Query**.
5. Identify which CVE count, severity, and fixability criteria would make an image fail.

![Build-time vulnerability policy criteria](images/build-policy-query.png)

6. Open **Vuln Run time**.
7. Select **New Security Vulnerability**.
8. Compare its **Details** and **Query** tabs with the build-time policy.
9. Check how **Frequency** and query conditions differ from the build-time policy.

![Runtime vulnerability policy criteria](images/runtime-policy-query.png)

**Checkpoint:** A build fails because of vulnerable images. Which criteria would you review?
Which policy would you examine for workloads already running? Check whether **Clone** is available before proposing a trial.

### Step 4: Review a Data policy

1. Open **Data** if available.
2. Select one policy.
3. Identify its data security condition and affected assets.
4. Inspect the available controls without changing them.

![Data policy catalog](images/data-policies.png)

Enabling a Data policy can initiate a rescan for configured DSPM integrations.
Keep it unchanged during this review.

**Checkpoint:** Which data asset or condition does this policy help you review?
What could enabling it trigger? If the category is unavailable, continue to the next step.

### Step 5: Read a composite policy

1. Open the **Threats** selector.
2. Select **Composite Alerts**.
3. Open **Potentially Compromised Host**.
4. Read its description and contributing-observation model.
5. Inspect **Edit** and **Clone**.

![Composite policy details](images/composite-policy.png)

The managed example has disabled Edit and Clone controls.

**Checkpoint:** Your team wants to change this composite's behaviour. Are the controls here available for that change?
Use the definition and the state of **Edit** and **Clone** to explain your answer.

### Step 6: Review an anomaly policy

1. Open **Anomalies**.
2. Select **New External Server IP Address Connection From Vulnerable Application**.
3. Read its frequency, severity, domain, and type in **Details**.
4. Open **Query**.
5. Check whether **Clone** is available.

![Anomaly policy query view](images/anomaly-query.png)

**Checkpoint:** Which changes does this policy actually let you make?
Use **No filter defined** and the available controls to distinguish the definition from an editable query.

### Step 7: Read a threat observation definition

1. Open **Threat Observations**.
2. Select **Anomalous AssumeRole request.** if available. Otherwise, select another definition.
3. Read its description, false positive notes, and triage guidance.
4. Inspect **Edit** and **Clone** without changing the definition.

![Threat observation definition](images/threat-observation.png)

**Checkpoint:** Could legitimate role activity explain this observation?
Choose one triage check to perform before escalating it.

### Step 8: Inspect custom policy choices

1. Return to **Risk: Compliance**.
2. Click **Add policy**.
3. Compare **Advanced (LQL)** with **Guided Builder (QBL)**.
4. Inspect **Policy type**.
5. Close the form without saving.

![Custom policy form with query language choices](images/policy-builder.png)

LQL is the query language used in the advanced editor. QBL uses the guided query builder.
The LQL path offers Compliance and Violation. The QBL path fixes the policy type to Compliance.
A new QBL policy creates a corresponding Risk Insight within about six hours.

**Checkpoint:** Your team needs a new configuration check. Which authoring path would you choose?
Use its available policy types and editor to explain your choice.

### Step 9: Choose a tuning action

Choose one policy you examined. Propose a change that solves a specific problem. Use the questions below.

| Action | Question to answer first |
|---|---|
| Change severity | Does business impact justify a different priority? |
| Change query criteria | Which resources should match, and which should not? |
| Add an exception | What exact scope and expiry are justified? |
| Change alert routing | Which team needs this alert? |
| Disable a policy | What detection or assessment coverage would be lost? |

> **What matters:** Choose a control that addresses the problem. Changing severity changes priority; it does not change which resources match.

**Checkpoint:** Would your change solve the problem or just make useful evidence disappear?
Explain the expected improvement and one check you would make before applying it.
Keep existing policies unchanged. You will create your own policy in Lab 9.

---
Next: [Lab 9: Turn a security question into a policy](../lab-09/README.md).

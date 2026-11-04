# Lab 7: What do your CIS results tell you?

**Environment:** FORTIDEMO-2026-04. Use the sandpit for an unavailable Azure example. **Access:** Read-only.

## Concepts

A compliance result is useful only when you know what was assessed.
CIS benchmarks group security controls by cloud provider and version.
FortiCNAPP assesses supported controls against collected resource data.
Review failures and assessment gaps together to decide what needs remediation and what needs more evidence.

## Objectives

- Identify the provider, benchmark version, scope, and time behind an assessment.
- Trace a failed control to a resource and distinguish it from an assessment gap.

## Prerequisites

Complete Lab 1.

## Lab steps

### Step 1: What does this assessment cover?

Use the AWS and Azure scopes assigned for this lab.
Keep the framework, version, scope, and time in your worksheet. They will guide your report settings in Lab 11.

1. Open **Risk Center > Findings > Compliance > Cloud**.
2. Select **Frameworks**.
3. Find an AWS CIS framework.
4. Record its complete title and version.
5. Inspect its assessed resources and policy breakdown.
6. Repeat for an Azure CIS framework that is available.

![Cloud Compliance framework results](images/compliance-frameworks.png)

**Checkpoint:** A teammate asks for "the CIS score". Can you explain which environment and benchmark your answer covers?
Check the provider, version, resource scope, and assessment time before quoting a result.
If the demo tenant has no Azure result in the selected scope, use the sandpit for that comparison.

### Step 2: Find the resource behind a failed check

1. Select **Policies**.
2. Search for `permission to everyone`.
3. Open **Ensure the attached S3 bucket policy does not grant 'Allow' permission to everyone**.
4. Identify a non-compliant resource.
5. Compare **Non-compliant**, **Compliant**, **Excepted**, and **Not assessed**.

![A compliance policy with its resource assessment](images/compliance-policy.png)

**Checkpoint:** What would you ask the bucket owner to review?
Use the policy condition and affected resource to make the request specific.

### Step 3: Find what the score cannot tell you

1. Return to **Frameworks**.
2. Review fully assessed, partially assessed, manual, or unknown policy results that are present.
3. Choose a control that needs more evidence.
4. Decide what a reviewer would need to assess it.

**Checkpoint:** Would a higher score settle this assessment gap?
Explain what evidence is still needed before you can give a complete answer.

> **What matters:** A passing automated assessment does not establish complete CIS certification.
> Check manual controls, exclusions, coverage, and the exact framework version.

Use the existing assessments for this exercise.

---
Next: [Lab 8: Choose the right policy control](../lab-08/README.md).

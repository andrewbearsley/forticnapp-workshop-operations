# Lab 6: Decide what to fix first

**Environment:** FORTIDEMO-2026-04. **Access:** Read-only.

## Concepts

A long list of vulnerabilities does not tell you where to start.
Exposure, identity permissions, and available fixes help you choose work that reduces risk.
A reachable host with valuable permissions can need a different response from an isolated host with the same vulnerable package.

## Objectives

- Justify a remediation priority using exposure, permissions, and available fixes.
- Identify where a source-code check could find a problem before deployment.

## Prerequisites

Complete Lab 5. Keep one attack path resource in your worksheet.

## Lab steps

### Step 1: Examine an identity

1. Open **Risk Center > Findings > Identities**.
2. Open **Top Identity Risks**.
3. Select an identity from your attack path if available. Otherwise, use another listed identity.
4. Read its risks and available usage information.
5. Compare its permissions with the work it needs to perform.

**Checkpoint:** Record one permission risk and its usage evidence.
State what you would ask the identity owner before changing access.

> **What matters:** An old or unused identity still needs an owner check.
> Usage history alone does not prove that removing access is safe.

### Step 2: Examine a vulnerability

1. Open **Risk Center > Findings > Vulnerabilities**.
2. Open **Top items**.
3. Compare **Top vulnerabilities by impacted hosts** with **Top fixable packages**.
4. Open one finding.
5. Identify the affected package and available fix information.
6. Check the host or image context.

![Vulnerability overview with exposure and coverage context](images/vulnerabilities.png)

The screenshot shows the Overview tab. Use Top items for the package comparison in this exercise.

**Checkpoint:** Record the package, affected resource, and available fix.
Use the exposure details to justify its place in your work list.

### Step 3: Find the earlier control point

1. Open **Findings > Code Security > Infrastructure (IaC)**.
2. Examine an available assessment.
3. Open **Applications**.
4. Compare a dependency finding with a runtime vulnerability finding.

**Checkpoint:** Identify which evidence concerns source code and which evidence concerns a running workload.

For code scanning exercises, use the [AWS integration workshop](https://github.com/andrewbearsley/forticnapp-workshop-aws-automated).

---
Next: [Lab 7: What do your CIS results tell you?](../lab-07/README.md).

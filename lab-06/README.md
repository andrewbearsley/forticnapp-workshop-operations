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

### Step 1: Check what an identity can do

1. Open **Risk Center > Findings > Identities**.
2. Open **Top Identity Risks**.
3. Select an identity from your attack path if available. Otherwise, use another listed identity.
4. Read its risks and available usage information.
5. Compare its permissions with the work it needs to perform.

**Checkpoint:** Which permission would you ask the owner to review first?
Use the risk and usage information to explain the request.

> **What matters:** An old or unused identity still needs an owner check.
> Usage history alone does not prove that removing access is safe.

### Step 2: Choose a package to fix first

1. Open **Risk Center > Findings > Vulnerabilities**.
2. Open **Top items**.
3. Compare **Top vulnerabilities by impacted hosts** with **Top fixable packages**.
4. Open one finding.
5. Identify the affected package and available fix information.
6. Check the host or image context.

![Vulnerability overview with exposure and coverage context](images/vulnerabilities.png)

The screenshot shows the Overview tab. Use Top items for the package comparison in this exercise.

**Checkpoint:** Would you start with the most widespread vulnerability or a fixable package on an exposed host?
Use the findings you opened to explain your priority.

### Step 3: Could you have caught this before deployment?

1. Open **Findings > Code Security > Infrastructure (IaC)**.
2. Examine an available assessment.
3. Open **Applications**.
4. Compare a dependency finding with a runtime vulnerability finding.

**Checkpoint:** Which finding could a developer act on before deployment?
Which needs a check of the running workload?

For code scanning exercises, use the [AWS integration workshop](https://github.com/andrewbearsley/forticnapp-workshop-aws-automated).

---
Next: [Lab 7: What do your CIS results tell you?](../lab-07/README.md).

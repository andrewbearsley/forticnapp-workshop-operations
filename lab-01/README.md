# Lab 1: What can FortiCNAPP tell you?

**Environment:** FORTIDEMO-2026-04. **Access:** Read-only.

## Concepts

Before you act on a finding, you need to know what it tells you.
An alert describes detected activity or a policy event. Compliance results assess configuration.
Exposure views help you understand what an attacker could reach.
These views answer different questions about the same environment.

## Objectives

- Match the main console views to the security questions they answer.
- Distinguish activity, compliance, and exposure using dashboard examples.

## Prerequisites

Use the console account supplied for the workshop.

## Lab steps

### Step 1: Confirm the tenant

Sign in to [the console](https://partner-demo.lacework.net/) with your workshop account.

1. Read the tenant name at the bottom of the navigation.
2. Open the tenant selector if another tenant is active.
3. Select **FORTIDEMO-2026-04**.
4. Open **Dashboard**.

**Checkpoint:** The tenant selector reads `FORTIDEMO-2026-04`.

### Step 2: Read the overview

Keep your answers in a private copy of [the evidence worksheet](../evidence-worksheet.md).

1. Find **Threat alert overview**.
2. Find **Non-compliant resources**.
3. Find **Exposed Fixable Hosts**.
4. Record the last update time for one widget.

![Dashboard with threat, compliance, and exposure widgets](images/dashboard.png)

**Checkpoint:** Record one count from each widget. Label it as activity, compliance, or exposure.
Record the update time that you found.

For example, **Non-compliant resources** counts resources that fail an assessment.
It does not count incidents. One resource can appear in several views.

### Step 3: Find the work areas

| Area | Use it to answer |
|---|---|
| Threat Center | What activity needs investigation? |
| Risk Center | Which conditions need attention? |
| Explorer | How are these resources related? |
| Policy Manager | What query, policy, or framework defines this result? |
| Reports | What evidence should be delivered, and to whom? |
| Inventory and Coverage | What exists, and what data is being collected? |

Locate each area in the navigation. Open **Threat Center > Alerts** for the next lab.

**Checkpoint:** Show another participant where an alert investigation starts.

## Discussion

Does a zero alert count prove that an account is secure?
Check coverage, filters, and collection times before you answer.

---
Next: [Lab 2: Composite alerts: is this host compromised?](../lab-02/README.md).

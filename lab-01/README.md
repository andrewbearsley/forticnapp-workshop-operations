# Lab 1: Read the console and confirm scope

**Environment:** FORTIDEMO-2026-04. **Access:** Read-only.

## Objectives

Find the main work areas. Confirm the tenant before you inspect data.
Explain which evidence comes from configuration collection, activity logs, and workload telemetry.

## Concepts

The console shows different types of evidence about the same resources.
Configuration collection supports compliance checks. Activity logs record cloud actions.
Workload telemetry shows processes and connections.
Check the tenant, scope, and collection time to interpret each result.

## Prerequisites

Use your approved console account. Open [the console](https://partner-demo.lacework.net/).

## Lab steps

### Step 1: Confirm the tenant

1. Read the tenant name at the bottom of the navigation.
2. Open the tenant selector if another tenant is active.
3. Select **FORTIDEMO-2026-04**.
4. Open **Dashboard**.

**Checkpoint:** The tenant selector reads `FORTIDEMO-2026-04`.

### Step 2: Read the overview

1. Find **Threat alert overview**.
2. Find **Non-compliant resources**.
3. Find **Exposed Fixable Hosts**.
4. Record the last update time for one widget.

![Dashboard with threat, compliance, and exposure widgets](images/dashboard.png)

**Checkpoint:** Explain what each widget counts. State the collection time with your answer.

The counts answer different questions. An exposed vulnerability is a risk condition.
An alert describes detected activity or a policy event. A compliance finding records an assessment result.
One resource can appear in several views.

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
Next: [Lab 2: Investigate a composite alert](../lab-02/README.md).

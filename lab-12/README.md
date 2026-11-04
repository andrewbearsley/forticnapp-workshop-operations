# Lab 12: Can you trust the data behind your findings?

**Environment:** FORTINETAPACDEMO. **Access:** Read-only review.

## Concepts

An investigation can miss activity when collection is stale or incomplete.
Even a useful alert needs to reach a responsible team.
Collection health, alert routing, and report delivery are separate checks.
Checking each one helps you find gaps between collected evidence and the people who need it.

## Objectives

- Check whether cloud and workload evidence is current.
- Trace notification settings and write a handover for a collection issue or status update.

## Prerequisites

Complete Lab 11. Do not change shared integrations or channels.

## Lab steps

### Step 1: Check collection

1. Open **Settings > Cloud accounts**.
2. Inspect the configuration integration for an AWS or Azure scope.
3. Check its state and last successful collection.
4. Inspect the activity log integration separately.
5. Open **Coverage > Agents**.
6. Check agent status and last check-in.
7. Open **Coverage > Agentless**.
8. Compare that coverage with the agent view.

![Agent coverage and inventory](images/agent-coverage.png)

Check collection state in the sandpit.

**Checkpoint:** Record one collection source and its latest successful update.
An enabled integration and a healthy collection state are different checks.

### Step 2: Review routing

1. Open **Settings > Channels**.
2. Inspect a channel without changing its recipients.
3. Examine the alert-routing controls available to your role.
4. Trace the intended route for a composite alert.
5. Compare that route with the email channel in your report configuration.

**Checkpoint:** Record one policy, the alert route you inspected, and the report email channel.
Label which defines the condition, routes the alert, and delivers the report.

> **What matters:** Check that alert notifications reach the responsible team.

### Step 3: Record an operational issue

Write a short handover for one failed or stale collection.
If none is present, use a healthy collection as a status update.
Include the integration type, time, observed state, and next check.
Keep credentials and unrelated identifiers out of the handover.

**Checkpoint:** Your handover reports the observed issue without claiming an unverified cause.

---
Next: [Lab 13: Ask the same questions through the CLI](../lab-13/README.md).

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

### Step 1: Would missing data change your conclusion?

A quiet alert list can look reassuring. Check whether the relevant data is arriving before relying on it.

1. Open **Settings > Cloud accounts**.
2. Inspect the configuration integration for an AWS or Azure scope.
3. Check its state and last successful collection.
4. Inspect the activity log integration separately.
5. Open **Coverage > Agents**.
6. Check agent status and last check-in.
7. Open **Coverage > Agentless**.
8. Compare that coverage with the agent view.

![Agent coverage and inventory](images/agent-coverage.png)

**Checkpoint:** Is the collection current enough to support your investigation window?
Use its state and last successful update to decide. An enabled integration alone is not enough.

### Step 2: Would anyone receive the alert?

1. Open **Settings > Channels**.
2. Inspect a channel without changing its recipients.
3. Examine the alert-routing controls available to your role.
4. Trace the intended route for a composite alert.
5. Compare that route with the email channel in your report configuration.

**Checkpoint:** If this composite alert needed action, which team would receive it?
Trace the route you inspected. Check report delivery separately.

> **What matters:** Check that alert notifications reach the responsible team.

### Step 3: Hand over the next action

Write a short handover for one failed or stale collection.
If none is present, use a healthy collection as a status update.
Include the integration type, time, observed state, and next check.
Keep credentials and unrelated identifiers out of the handover.

**Checkpoint:** A teammate can see what is working or missing and which check to perform next.
They do not need to repeat your investigation to understand the handover.

---
Next: [Lab 13: Ask the same questions through the CLI](../lab-13/README.md).

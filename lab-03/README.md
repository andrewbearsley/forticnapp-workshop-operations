# Lab 3: Follow cloud activity and individual alerts

**Environment:** FORTIDEMO-2026-04. **Access:** Read-only.

## Objectives

Use individual alerts and cloud activity to support an investigation.
Separate a detected event from your explanation of its cause.

## Concepts

Individual alerts and cloud activity records help you test an incident hypothesis.
An anomaly is a detected deviation. Its cause can be legitimate or malicious.
A cloud activity record supplies evidence about an action, its actor, and its outcome.

## Prerequisites

Complete Lab 2. Keep the composite alert's activity window in your worksheet.

## Lab steps

### Step 1: Inspect a policy alert

1. Open **Threat Center > Alerts**.
2. Change **Alert category** to **Policy**.
3. Start with the activity window from Lab 2.
4. Open an available alert.
5. Read its description and source.
6. Record its activity window, affected entity, and policy.

If no example appears, widen the date range. Record the new window separately from your composite investigation.

**Checkpoint:** Record the triggering condition and its affected entity.
Use the description to check your answer.

### Step 2: Inspect an anomaly

1. Change **Alert category** to **Anomaly**.
2. Open an available example.
3. Record what is unusual and which entity is involved.
4. List the operational context needed to explain it.

**Checkpoint:** Give one legitimate explanation and one security explanation.
Name one check that would help distinguish them.

### Step 3: Examine cloud activity

Use your selected alert if it describes a cloud API action.
If it concerns host activity, use a separate cloud activity example.

1. Open **Threat Center > Cloud Activity**.
2. Set the time range to your selected alert's activity window.
3. Use the visible filters to locate its identity or resource, if known.
4. Select a record that matches the alert, or an available record for a separate example.
5. Read its action, actor, time, and available outcome.

If no records appear, widen the date range.
Record a separate example as separate evidence. Do not infer a connection to the host alert.

![Cloud Activity investigation view](images/cloud-activity.png)

**Checkpoint:** Record one cloud action, its actor, time, and available outcome.
State whether it matches your alert or is a separate example.

> **Hint:** A host process event and a cloud API event have different sources.
> Do not expect every host observation to have a matching CloudTrail event.

## Discussion

Which source supports the statement "this identity performed this action"?
Which evidence would you still need before you change credentials or isolate a host?

---
Next: [Lab 4: Find resources with Explorer and Inventory](../lab-04/README.md).

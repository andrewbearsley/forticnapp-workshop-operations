# Lab 3: Follow the activity behind an alert

**Environment:** FORTIDEMO-2026-04. **Access:** Read-only.

## Concepts

An alert gives you a reason to investigate. The underlying activity helps you test the explanation.
An anomaly is a detected deviation with a cause that can be legitimate or malicious.
Cloud activity records help you check who performed an action and what happened.

## Objectives

- Identify what triggered a policy alert and what is unusual in an anomaly.
- Use a cloud activity record to check an action, actor, and outcome.

## Prerequisites

Complete Lab 2. Keep the composite alert's activity window in your worksheet.

## Lab steps

### Step 1: What triggered this alert?

1. Open **Threat Center > Alerts**.
2. Change **Alert category** to **Policy**.
3. Start with the activity window from Lab 2.
4. Open an available alert.
5. Read its description and source.
6. Identify the condition that triggered it and the affected entity.

If no example appears, widen the date range. Record the new window separately from your composite investigation.

**Checkpoint:** What would have to change for this condition to stop matching?
Use the policy description to support your answer.

### Step 2: Could this be normal?

1. Change **Alert category** to **Anomaly**.
2. Open an available example.
3. Find what is unusual and which entity is involved.
4. Consider what legitimate work could produce the same activity.

**Checkpoint:** Would you escalate this now or check with the resource owner first?
Name the evidence that would help you decide.

### Step 3: Check who did what

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

**Checkpoint:** Could you use this record to support the statement "this identity performed this action"?
Check its actor, time, and outcome. Keep it separate from your incident if no link is established.

> **Hint:** A host process event and a cloud API event have different sources.
> Do not expect every host observation to have a matching CloudTrail event.

## Discussion

Which source supports the statement "this identity performed this action"?
Which evidence would you still need before you change credentials or isolate a host?

---
Next: [Lab 4: Find the resources behind the alert](../lab-04/README.md).

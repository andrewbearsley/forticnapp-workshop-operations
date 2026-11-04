# Lab 3: Explore Threat Center beyond composite alerts

**Environment:** FORTIDEMO-2026-04. **Access:** Read-only.

## Concepts

Threat Center also lets you investigate individual policy and anomaly alerts and inspect cloud activity.
A composite alert already brings related observations and investigation context together.
Use the separate views when you have a specific question about another alert or a cloud action.
Here, explore each view using its own example.

## Objectives

- Distinguish an individual policy alert from an anomaly.
- Use Cloud Activity to answer a question about a cloud API action.

## Prerequisites

Complete Lab 1.

## Lab steps

### Step 1: What triggered this alert?

1. Open **Threat Center > Alerts**.
2. Change **Alert category** to **Policy**.
3. Open an available alert.
4. Read its description and source.
5. Identify the condition that triggered it and the affected entity.

If no example appears, widen the date range.

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

Use Cloud Activity to examine a cloud action independently of an alert.

1. Open **Threat Center > Cloud Activity**.
2. Choose a time range with available activity.
3. Select an available activity record.
4. Read its action, actor, time, and available outcome.
5. Use the visible filters to focus on that identity or resource.

If no records appear, widen the date range.

![Cloud Activity investigation view](images/cloud-activity.png)

**Checkpoint:** Did the action succeed, fail, or leave the outcome unclear?
Use the actor and outcome fields to explain what the record establishes.

## Discussion

A teammate asks who changed a cloud resource. Which view would you use?
When would a composite alert be a better starting point?

---
Next: [Lab 4: Find the resources behind the alert](../lab-04/README.md).

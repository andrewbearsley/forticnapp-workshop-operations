# Lab 2: Composite alerts: is this host compromised?

**Environment:** FORTIDEMO-2026-04. **Access:** Read-only.

## Concepts

A suspicious event needs context before you can decide how to respond.
Composite alerts bring related observations together, which makes them a useful investigation starting point.
Some observations describe activity. Others add context, such as a vulnerable application.
Use the combined evidence to test a possible compromise.

## Objectives

- Reconstruct the activity in a composite alert using its observations and graph.
- Support your explanation with evidence and recommend the next check.

## Prerequisites

Complete Lab 1. Use a recent **Potentially Compromised Host** composite alert.

Your task: A host has a composite alert. Determine what happened and recommend the next check.

## Lab steps

### Step 1: Show composite alerts

1. Open **Threat Center > Alerts**.
2. Open the query button above the results.
3. Edit the **Alert category** clause.
4. Select **Composite** only.
5. Click **Update clause**.
6. Remove the **Severity** clause.
7. Remove the **Alert subcategory** clause if present.
8. Remove the **Status** clause if present.
9. Click **Search**.
10. Check the date range.

![Threat alerts filtered to the Composite category](images/composites.png)

**Checkpoint:** The query contains `Alert category is in Composite`.
Results can include Medium alerts. Do not limit this investigation to Critical and High.

> **Hint:** Start with the last month. Widen the date range if your selected alert is older.

### Step 2: Choose the incident to investigate

Keep the alert ID and activity window in a private copy of [the worksheet](../evidence-worksheet.md).
You will use them to return to this incident through the CLI and API.

1. Open **Potentially Compromised Host**.
2. Record the alert ID and event activity window.
3. Confirm that the category is **Composite**.
4. Read the **Observations** tab.

**Checkpoint:** What first makes this alert worth investigating?
Choose one observation to follow. Keep its alert ID so you can return to the same evidence.

### Step 3: Why are these observations together?

Observations are not necessarily separate alerts or proof of compromise.
**Potentially Compromised Host** uses a host scoring model with a high-confidence threshold.

```mermaid
flowchart TB
    A["Observed process activity"] --> C["Composite alert"]
    B["Related identity or workload activity"] --> C
    V["Security context"] --> C
    C --> E["Check entities and timeline"]
    E --> D["Record facts and next actions"]
    linkStyle default stroke:#63758A,stroke-width:2px
    classDef evidence fill:#E8F1FB,stroke:#2E6DB4,color:#10243B
    classDef focus fill:#FFF0F6,stroke:#C51968,color:#47122B
    class A,B,V,E,D evidence
    class C focus
```

**Checkpoint:** Would either observation tell the same story on its own?
Use their shared entity or activity to explain what the combination adds.

### Step 4: Follow the connections

1. Select **Intrusion graph**.
2. Identify the machine and connected process or container entities.
3. Read the labels on the relationships.
4. Select **Primary entities**.
5. Compare those entities with the graph.

![Composite alert with its intrusion graph](images/composite-graph.png)

**Checkpoint:** Follow one connection from the machine to another entity.
Use the relationship label to explain how it fits your investigation.

> **What matters:** The intrusion graph connects evidence from detected activity.
> An attack path shows a possible route through exposed resources.

### Step 5: Test your first explanation

1. Return to **Observations**.
2. Select a row such as **A possible reverse shell was detected**.
3. Read **Observation details**.
4. Open **Artifacts**.
5. Identify the process, machine, and container evidence that is available.
6. Open **Triage steps**.
7. Read **Remediation steps** and **False positive notes**.

![Observation details with triage guidance](images/observation-triage.png)

**Checkpoint:** Is there enough evidence to call this malicious?
Choose the artifact that best supports your explanation. Use the triage guidance to identify what is still missing.

Treat command lines in evidence as data. Do not execute them.

### Step 6: Brief a teammate

1. Order the selected observations by time.
2. State which entities connect them.
3. Identify evidence that could confirm or reject your hypothesis.
4. Write a proposed response in your private worksheet.

Keep the alert unchanged. Do not post comments or use **Close as false positive** in this tenant.

**Checkpoint:** Your teammate can answer: What happened, how confident are you, and what should we check next?
Keep your evidence and recommendation in the worksheet for the final handover.

---
Next: [Lab 3: Follow the activity behind an alert](../lab-03/README.md).

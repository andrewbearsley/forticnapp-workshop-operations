# Lab 2: Investigate a composite alert

**Environment:** FORTIDEMO-2026-04. **Access:** Read-only.

## Objectives

Start with the highest-value alert type: a composite alert.
Use its related observations to determine what happened, which resources are involved, and what to check next.

## Prerequisites

Complete Lab 1. Use a recent **Potentially Compromised Host** composite alert.

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

### Step 2: Open Potentially Compromised Host

1. Open **Potentially Compromised Host**.
2. Record the alert ID and event activity window.
3. Confirm that the category is **Composite**.
4. Read the **Observations** tab.

**Checkpoint:** Your worksheet identifies one alert, one activity window, and its tenant.

### Step 3: Understand what is combined

A composite alert relates observations that warrant investigation together.
An observation can describe suspicious activity or useful security context.
For example, a vulnerable application is context. A possible reverse shell describes detected activity.
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

Conceptual view of a composite alert.

### Step 4: Read the intrusion graph

1. Select **Intrusion graph**.
2. Identify the machine and connected process or container entities.
3. Read the labels on the relationships.
4. Select **Primary entities**.
5. Compare those entities with the graph.

![Composite alert with its intrusion graph](images/composite-graph.png)

**Checkpoint:** Explain one relationship using the entities and activity shown.

> **What matters:** This graph relates evidence from the alert.
> The Attack Path view in Lab 5 describes exposure conditions. The two graphs answer different questions.

### Step 5: Examine an observation

1. Return to **Observations**.
2. Select a row such as **A possible reverse shell was detected**.
3. Read **Observation details**.
4. Open **Artifacts**.
5. Identify the process, machine, and container evidence that is available.
6. Open **Triage steps**.
7. Read **Remediation steps** and **False positive notes**.

![Observation details with triage guidance](images/observation-triage.png)

**Checkpoint:** Record two observed facts and one hypothesis that needs checking.

Treat command lines in evidence as data. Do not execute them.
Use the triage guidance to test your hypothesis.

### Step 6: Explain the incident

1. Order the selected observations by time.
2. State which entities connect them.
3. Identify evidence that could confirm or reject your hypothesis.
4. Write a proposed response in your private worksheet.

Keep the alert unchanged. Do not post comments or use **Close as false positive** in this tenant.

**Checkpoint:** Another participant can distinguish your confirmed facts from your proposed explanation.

## Extension: Cloud credentials

Open **Potentially Compromised AWS Credentials** if an example is available.
Repeat the investigation for identities, API activity, and related resources.

---
Next: [Lab 3: Follow cloud activity and individual alerts](../lab-03/README.md).

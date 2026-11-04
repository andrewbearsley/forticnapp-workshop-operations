# Lab 5: Investigate risk and attack paths

**Environment:** FORTIDEMO-2026-04. **Access:** Read-only.

## Objectives

Identify conditions that permit exposure. Select a practical way to interrupt an attack path.
Keep exposure analysis separate from evidence of exploitation.

## Prerequisites

Complete Lab 4. Keep the affected resource from your composite investigation.

## Lab steps

### Step 1: Compare the two alert views

1. Open **Risk Center > Alerts**.
2. Open an available risk alert.
3. Identify the resource and condition.
4. Compare its question with the composite alert from Lab 2.

**Checkpoint:** Explain the difference between detected suspicious activity and a dangerous resource condition.

### Step 2: Find the top work items

1. Open **Risk Center > Findings > Attack Path**.
2. Select **Top Work Items**.
3. Examine **Top risky hosts**.
4. Examine **Top risky paths with exposed secrets**.
5. Identify the resource that you would investigate first.

![Attack Path top work items](images/attack-work-items.png)

**Checkpoint:** Support your choice with exposure and potential impact, not severity alone.

### Step 3: Trace an exposure path

1. Select **Path Investigation**.
2. Select an AWS or Azure path with an exposure graph.
3. Scroll to the **EXPOSURE POLYGRAPH**.
4. Trace the relationships from the entry point to the target.
5. Inspect the available resource details, vulnerabilities, or compliance violations.

![Path Investigation with exposure relationships](images/path-investigation.png)

**Checkpoint:** Name an entry point, a target, and one relationship that permits the path.

```mermaid
flowchart LR
    I["Internet"] --> E["Reachable service"]
    E --> H["Affected workload"]
    H --> P["Permission or secret"]
    P --> D["Target data"]
    linkStyle default stroke:#63758A,stroke-width:2px
    classDef node fill:#E8F1FB,stroke:#2E6DB4,color:#10243B
    class I,E,H,P,D node
```

Example exposure path. The path shows what could happen, not evidence that it happened.

### Step 4: Propose a path interruption

1. Select one relationship that you could change.
2. Explain how that change removes or reduces exposure.
3. Identify the service owner who must assess the operational effect.
4. Record how you would verify the change.

**Checkpoint:** Your proposal states the security result and the required operational check.

Do not change cloud resources during this lab.

---
Next: [Lab 6: Examine identity and vulnerability context](../lab-06/README.md).

# Lab 10: Build a custom compliance framework

**Environment:** FORTINETAPACDEMO. **Access:** Read/write. **Time:** 30 minutes.

## Objectives

Group policies for a specific reporting purpose. Keep a custom framework distinct from the original CIS benchmark.

## Prerequisites

Complete Lab 7. Use your participant ID.
Use the AWS or Azure framework that the instructor selects.
Screenshots show the demo tenant. Save only in the sandpit.

## Lab steps

### Step 1: Inspect the framework catalog

1. Confirm **FORTINETAPACDEMO**.
2. Open **Policy Manager > Frameworks**.
3. Compare **Lacework managed** with **Managed by you**.
4. Open a built-in framework.
5. Inspect its sections and policy mappings.

![Framework Catalog](images/framework-catalog.png)

**Checkpoint:** Explain the difference between a policy and a framework.

```mermaid
flowchart TB
    subgraph definitions["Definitions"]
    direction LR
    Q["Query: which resources match?"] --> P["Policy: assessment or detection condition"]
    P --> F["Framework: selected compliance policies"]
    end
    subgraph delivery["Reporting"]
    direction LR
    C["Report configuration: scope and delivery"]
    C --> R["Report: assessment evidence"]
    end
    definitions --> delivery
    linkStyle default stroke:#63758A,stroke-width:2px
    classDef item fill:#E8F1FB,stroke:#2E6DB4,color:#10243B
    class Q,P,F,C,R item
    style definitions fill:#F6F8FA,stroke:#D1D9E0,color:#10243B
    style delivery fill:#F6F8FA,stroke:#D1D9E0,color:#10243B
```

This diagram shows the compliance reporting relationship. Other policy categories have different workflows.

### Step 2: Create a custom framework

1. Return to the catalog.
2. Click **Add Framework**.
3. Select the instructor's source framework.
4. Continue to the framework editor.
5. Set a unique name: `Workshop-YOURID-AWS-review` or `Workshop-YOURID-Azure-review`.
6. Select **Networking** in the copied framework.
7. Click **Add / Edit policies**.
8. Select **Selected policies**.
9. Clear one selected policy.
10. Click **Update section**.
11. Save your custom framework.

**Checkpoint:** Your framework appears under **Managed by you**. The source framework is unchanged.

> **What matters:** A modified CIS-based framework is a custom control set.
> Do not present it as the complete, unchanged CIS benchmark.

### Step 3: Review revision and evaluation state

1. Reopen your framework.
2. Record its revision and policy selection.
3. Check for **Pending changes**.
4. Explain which assessment results may still reflect the earlier configuration.

**Checkpoint:** Your worksheet records the framework name, provider, revision, and reporting purpose.

Framework changes can take up to 24 hours to appear in assessment results.
Do not trigger repeated scans to force a classroom result.
Keep this framework for cleanup. Lab 11 uses the built-in CIS frameworks for its main reports.

---
Next: [Lab 11: Configure AWS and Azure CIS reports](../lab-11/README.md).

# Lab 4: Find resources with Explorer and Inventory

**Environment:** FORTIDEMO-2026-04. **Access:** Read-only. **Time:** 35 minutes.

## Objectives

Find the resources behind a finding. Use relationships to explain exposure.
Compare cloud inventory with workload telemetry.

## Prerequisites

Complete Lab 2. Keep one affected entity in your worksheet.

## Lab steps

### Step 1: Build an Explorer query

1. Open **Explorer**.
2. Select **Or use the Query Builder** if the plain-language search page opens.
3. Open the query button beside the search bar if the builder is closed.
4. Select **Hosts** as the return type.
5. Add **Internet Exposed** as a clause.
6. Set its value to **True**.
7. Apply the clause.
8. Click **Search Results**.

![Explorer with an internet exposure query](images/explorer-query.png)

**Checkpoint:** The query asks for internet-exposed hosts.
If no hosts match, check the scope and data collection before changing the query.

### Step 2: Read a graph

1. Select a host that has alerts or attack paths.
2. Open **Graph**.
3. Follow the resource relationships that permit exposure.
4. Compare the host with the entity from your alert.

**Checkpoint:** Explain the route using the resources shown.
Do not assume that the first host in a list is the alert's affected host.

### Step 3: Compare inventory views

1. Open **Inventory > Resource Inventory**.
2. Locate an AWS or Azure resource.
3. Examine the resource properties and related findings.
4. Open **Inventory > Hosts**.
5. Examine the **Machines** and **Processes** views.

**Checkpoint:** Explain which view describes cloud configuration and which view describes observed workload activity.

> **What matters:** A resource in cloud inventory does not prove that a workload agent is installed.
> Check **Coverage > Agents** when the investigation needs agent telemetry.

---
Next: [Lab 5: Investigate risk and attack paths](../lab-05/README.md).

# Lab 16: Present your findings and clean up

**Environment:** Demo for investigation; sandpit for cleanup.

## Concepts

An investigation is useful when another person can understand the evidence and act on your recommendation.
Keep detected activity, possible exposure, and compliance results distinct in your explanation.
Removing your saved lab objects leaves the shared sandpit ready for the next exercise.

## Objectives

- Present an investigation with supported conclusions and a proposed response.
- Explain your risk and compliance evidence.
- Remove your saved objects and verify that they are gone.

## Prerequisites

Keep your evidence worksheet and the IDs of every object that you created.

## Lab steps

### Step 1: Present the investigation

1. Confirm **FORTIDEMO-2026-04**.
2. Present the composite alert and its activity window.
3. Explain two related observations.
4. State the affected entities and evidence sources.
5. Separate confirmed facts from hypotheses.
6. Propose a response and a verification method.

**Checkpoint:** Another participant can trace each main conclusion to its evidence.
Do not change the demo alert's status or comments.

**Extension:** Investigate **Potentially Compromised AWS Credentials** if available.
Apply the same method to identities, API activity, and related resources.

### Step 2: Explain the risk and compliance evidence

1. Explain an exposure path and a possible interruption.
2. State why that path does not prove exploitation.
3. Identify the CIS framework provider and version.
4. Explain one failed control and one assessment gap.
5. Show the scope of each sandpit report configuration.

**Checkpoint:** Your explanation keeps incident evidence, exposure, and compliance assessment distinct.

### Step 3: Remove your report configurations

1. Switch to **FORTINETAPACDEMO**.
2. Open **Reports**.
3. Find each configuration from your created-object record.
4. Confirm its exact name and framework.
5. Remove only your workshop configurations using the available action.
6. Verify that they no longer appear.

**Checkpoint:** No workshop report configuration remains for your participant ID.

### Step 4: Remove your policies, framework, and queries

1. Open **Policy Manager > Policies**.
2. Remove your disabled workshop policy by its recorded ID.
3. Open **Policy Manager > Frameworks**.
4. Remove your custom workshop framework.
5. Open **Policy Manager > Queries**.
6. Remove your QBL and LQL workshop queries.
7. Verify that each recorded ID is absent.

Remove dependent objects first. Do not remove a query that an existing shared policy uses.
Never select all objects for cleanup.

**Checkpoint:** Your created-object record shows the removal of every object you created.

### Step 5: Close the session

Close private exports and credential files.
Remove temporary credential files that you no longer need.
Do not revoke a shared key or remove another participant's local profile.

**Checkpoint:** Your workshop objects and temporary credential files are removed.

---
Return to the [workshop overview](../README.md).

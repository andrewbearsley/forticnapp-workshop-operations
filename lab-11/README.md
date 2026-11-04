# Lab 11: Configure AWS and Azure CIS reports

**Environment:** FORTINETAPACDEMO. **Access:** Read/write.

## Objectives

Configure separate CIS reports for AWS and Azure.
Select the correct framework version, data scope, assessment statuses, and delivery settings.

## Concepts

A report configuration selects the framework, resource scope, assessment statuses, and delivery settings.
The generated report contains the assessment evidence for those selections.
Separate AWS and Azure configurations keep each provider's benchmark and scope clear.

## Prerequisites

Complete Labs 7 and 10. Have your assigned AWS and Azure resource groups ready.
Screenshots show demo report controls. Create reports only in the sandpit.

## Lab steps

### Step 1: Inspect existing configurations

1. Confirm **FORTINETAPACDEMO**.
2. Open **Reports**.
3. Inspect an AWS report configuration.
4. Inspect an Azure report configuration.
5. Record the framework and data scope for each.

![Report configurations](images/reports.png)

**Checkpoint:** Distinguish a report configuration from a generated assessment report.

### Step 2: Configure the AWS report

1. Return to **Reports**.
2. Click **Configure report**.
3. Select the required AWS CIS framework and version.
4. Set **Name** to `Workshop-YOURID-AWS-CIS`.
5. Select the approved AWS **Data scope**.
6. Review **Severity**.
7. Review **Status**.
8. Turn off **Enabled** under **Delivery**.
9. Select the **Email channel** assigned for this lab.
10. Review **Delivery frequency**.
11. Create the configuration.
12. Open the saved configuration.
13. Confirm that **Report configuration** is **Disabled**.
14. Turn off its switch if the saved configuration is enabled.

![Report configuration fields](images/report-form.png)

**Checkpoint:** The saved configuration has the required AWS framework and scope. Delivery is disabled.

An email channel is required even when delivery is off.
Check the saved configuration's state. Do not rely only on the creation form's switch.

> **What matters:** Keep **Manual** and **Could Not Assess** visible when the report must show assessment gaps.
> Hiding these statuses can remove evidence that the report reader needs.

### Step 3: Configure the Azure report

Repeat Step 2 with the required Azure CIS framework.
Use `Workshop-YOURID-Azure-CIS` as the name.
Select the approved Azure subscription scope. Keep delivery disabled.

**Checkpoint:** You have two separate configurations. Each uses the correct provider, version, and data scope.

### Step 4: Review the delivery plan

1. Record the intended recipients and frequency in your worksheet.
2. Compare them with the selected email channel.
3. Identify the owner who approves enabling delivery.
4. Check the available report preview from **Cloud Compliance > Frameworks**.

**Checkpoint:** Explain what each recipient will receive and which resources the report covers.

Do not enable delivery to a shared email channel during the lab.
Keep both configurations for cleanup in Lab 16.

---
Next: [Lab 12: Check coverage and notification routing](../lab-12/README.md).

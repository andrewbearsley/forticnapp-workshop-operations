# Instructor guide

## Positioning

Use **FortiCNAPP Operations Workshop** as the course title.
Use **Investigate threats, assess risk, and automate daily work** as the subtitle.
The existing AWS course teaches integration. This course starts with connected environments.

## Protect the demo environment

FORTIDEMO-2026-04 is read-only for this workshop, including instructor work.
Do not change alert status, post comments, create exceptions, run scans, or save configuration there.
Do not use its admin key as a student credential.
The wrapper in `tools/lw-read.sh` limits selected commands. It does not replace restricted API permissions.

Use FORTINETAPACDEMO for every saved object.
Create no cloud resources for this course.
Use unique names and record object IDs. Remove only objects that you created.
Do not disable existing policies or change shared notification routes.

## Prepare the class

1. Verify student permissions in both tenants.
2. Check integration collection times and agent coverage.
3. Select one host composite alert with several observations.
4. Select one cloud credential composite alert if available.
5. Record the alert IDs and time windows in a private delivery sheet.
6. Select AWS and Azure attack path examples.
7. Check the exact CIS versions in the tenant.
8. Prepare one AWS account scope and one Azure subscription scope.
9. Check the policy controls for every category available in the tenant.
10. Confirm the permitted CLI and AI agent runtimes.
11. Test every lab with student-equivalent permissions.

Do not depend on an alert appearing during the class.
The demo screenshots use a historical month view. Extend the date range when an example ages out.
Use another composite when the original alert is unavailable.

## Teaching checkpoints

In Lab 2, ask for facts before conclusions. A composite alert is a high-value investigation starting point.
It does not remove the need to validate activity and scope.
In Lab 5, ask which relationship permits exposure. An attack path does not prove exploitation.
In Lab 7, ask which controls were assessed. A report does not prove complete certification.
In Lab 9, test query results before saving a policy. An empty result needs a coverage check.
In Lab 11, check the provider, version, and data scope separately.
In Lab 15, compare the agent's conclusion with evidence. Keep AI Assist distinct from the external skill.

## Shared tenant effects

Keep new policies disabled during creation and review.
Keep report delivery disabled during the lab.
Review proposed changes before any policy activation or email delivery.
Do not ask every participant to run an adhoc compliance scan.
Use existing assessments. Framework results can take up to 24 hours to update.

## Screenshot checks

Close integration notices, promotions, and empty assistant panels before capture.
Do not select persistent dismissal preferences in the demo tenant.
Keep the navigation and relevant controls visible.
Use one viewport width throughout the workshop.
Redact cloud account IDs, emails, access keys, internal addresses, and unrelated resource names.
Check each final image after redaction. Confirm that the target control remains readable.

## Delivery readiness

Do not describe an untested procedure as verified.
Rebuild and inspect the PDF after any lab change.

The authoring pass tested QBL query creation, LQL query and disabled policy creation,
a policy severity update, custom framework creation, AWS report creation, and cleanup.
The API GET and read-only search examples ran successfully.

Before delivery, test the Azure report save path with the intended student role.
Test any optional vulnerability policy clone exercise in the permitted sandpit scope.
Check installation and skill invocation in the runtime that students will use.
The managed-policy review is a guided investigation. It does not promise direct editing for every policy category.

# Instructor guide

## Positioning

Use **FortiCNAPP Operations Workshop** as the course title.
Use **Investigate threats, assess risk, and automate daily work** as the subtitle.
The existing AWS course teaches integration. This course starts with connected environments.

## Protect the demo environment

FORTIDEMO-2026-04 is read-only for this workshop, including instructor work.
Do not change alert status, post comments, create exceptions, run scans, or save configuration there.
The instructor API key has admin permissions. A profile name does not restrict those permissions.
Give students separate credentials with read-only permissions for this tenant.
Never distribute the instructor key.
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

## What each lab should teach

Keep one main point in focus. Use the tasks and discussion to help students apply it.

| Lab | Main point |
|---|---|
| [1](lab-01/README.md) | Know what is in the environment. Use resource context and possible impact to choose where to act. |
| [2](lab-02/README.md) | Related observations provide context for an investigation. Test the possible compromise against the combined evidence. |
| [3](lab-03/README.md) | Test an alert explanation against the underlying activity before deciding how to respond. |
| [4](lab-04/README.md) | Resource relationships connect an alert entity to its environment and exposure. |
| [5](lab-05/README.md) | Interrupting a relationship can reduce exposure. An attack path does not prove that an attacker used it. |
| [6](lab-06/README.md) | Use exposure, permissions, and available fixes to choose remediation priorities. |
| [7](lab-07/README.md) | An assessment needs its benchmark version, scope, time, and gaps to give its score meaning. |
| [8](lab-08/README.md) | Choose a tuning control that addresses the problem without hiding useful evidence. |
| [9](lab-09/README.md) | Test what a query matches before using it in a policy. Review the disabled policy before activation. |
| [10](lab-10/README.md) | A framework selects the controls for a review. A changed CIS selection is a custom control set. |
| [11](lab-11/README.md) | Useful reports give the right recipients evidence for their scope, including assessment gaps. |
| [12](lab-12/README.md) | Check collection health and notification routing before relying on findings or a quiet inbox. |
| [13](lab-13/README.md) | CLI commands make checks repeatable. Match scope and time before comparing their results with the console. |
| [14](lab-14/README.md) | Reliable API automation needs matching evidence, the correct response structure, and complete results. |
| [15](lab-15/README.md) | An agent can help investigate. Verify its conclusions against the underlying evidence. |
| [16](lab-16/README.md) | A useful handover lets another person act. Remove your saved objects to leave the sandpit ready. |

In Lab 1, ask what information would change the student's first choice. Do not reward the largest-count answer.
In Lab 2, ask for facts before conclusions. Keep composite alerts central to the investigation.
In Lab 7, distinguish a failed check from missing assessment evidence.
In Lab 15, keep console AI Assist distinct from the external skill.

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

## Session planning

Allow two full days with discussion and breaks. These times are estimates.
Collection and assessment can continue after a lab ends.

| Labs | Estimated minutes per lab |
|---|---|
| 1 to 8 | 20, 60, 35, 35, 45, 30, 45, 45 |
| 9 to 16 | 60, 30, 40, 20, 35, 40, 35, 30 |

For a shorter session, select one path:

- Investigation: Labs 1 to 5 and the investigation steps in Lab 16.
- Compliance: Labs 1, 7, 10, and 11.
- Automation: Labs 2 and 13 to 15.

Include each selected lab's prerequisites. Include cleanup for any objects created.
For an automation-only session, complete Lab 9 Step 3 before Lab 13.
Lab 9 now configures the sandpit profile before its first CLI command.
Lab 13 adds the demo profile.

## Build the offline copy

Install Python dependencies from `requirements.txt`. Install Google Chrome.
Run `python tools/build_pdf.py` after changes to student pages or images.
Run `python tools/preflight.py` before publishing.
Inspect the rendered PDF. Commit it with the source changes.
The PDF contains the overview, labs, and evidence worksheet. It excludes this guide.

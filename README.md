# FortiCNAPP Operations Workshop
Reading offline? Download the [workshop PDF](forticnapp-workshop-operations.pdf).

Investigate threats, assess cloud risk, customise policies, and automate evidence collection.

Start with a composite alert. Follow its observations to the affected resources.
Then use compliance findings, custom policies, and reports to support daily operations.

## Who this workshop is for

Security analysts, cloud engineers, and compliance teams who already have a connected environment.
You need basic AWS and Azure knowledge. You do not need previous LQL experience.

Allow two full days, including discussions and breaks. The instructor can select a shorter path below.
Lab times are planning estimates. Data collection and assessment can continue after a lab ends.

This is a workshop draft. Complete the delivery checks in the [instructor guide](instructor-guide.md) before teaching it.

## Environments

| Environment | Use | Student access |
|---|---|---|
| **FORTIDEMO-2026-04** | Investigate prepared alerts and findings | Read-only |
| **FORTINETAPACDEMO** | Create workshop queries, policies, frameworks, and reports | Read/write |

> [!IMPORTANT]
> Check the tenant name before each lab. Never change **FORTIDEMO-2026-04**.
> The instructor's demo API key has admin permissions. Its profile name does not restrict those permissions.
> Students must use their own approved credentials. Never share the instructor key.

Use a unique participant ID, such as `ab04`.
Use `Workshop-ab04-` at the start of every object name that you create.
Record each object's ID in [your evidence worksheet](evidence-worksheet.md).

Screenshots show one verified session. Counts, alert IDs, and dates change.
Black boxes conceal identifiers. Magenta boxes identify controls.

## Day 1: Investigate and assess

| Lab | Task | Environment | Time |
|---|---|---|---:|
| [1](lab-01/README.md) | Read the console and confirm scope | Demo | 20 min |
| [2](lab-02/README.md) | Investigate a composite alert | Demo | 60 min |
| [3](lab-03/README.md) | Follow cloud activity and individual alerts | Demo | 35 min |
| [4](lab-04/README.md) | Find resources with Explorer and Inventory | Demo | 35 min |
| [5](lab-05/README.md) | Investigate risk and attack paths | Demo | 45 min |
| [6](lab-06/README.md) | Examine identity and vulnerability context | Demo | 30 min |
| [7](lab-07/README.md) | Interpret AWS and Azure CIS findings | Demo, then sandpit | 45 min |
| [8](lab-08/README.md) | Understand policy types and tuning controls | Sandpit | 45 min |

## Day 2: Configure and automate

| Lab | Task | Environment | Time |
|---|---|---|---:|
| [9](lab-09/README.md) | Build and test a custom query and policy | Sandpit | 60 min |
| [10](lab-10/README.md) | Build a custom compliance framework | Sandpit | 30 min |
| [11](lab-11/README.md) | Configure AWS and Azure CIS reports | Sandpit | 40 min |
| [12](lab-12/README.md) | Check coverage and notification routing | Sandpit | 20 min |
| [13](lab-13/README.md) | Use the CLI with explicit tenant scope | Both, read-only | 35 min |
| [14](lab-14/README.md) | Retrieve evidence through the API | Both, read-only | 40 min |
| [15](lab-15/README.md) | Investigate with the FortiCNAPP agent skill | Both, read-only | 35 min |
| [16](lab-16/README.md) | Complete the investigation and remove lab objects | Both | 30 min |

## Shorter sessions

For an investigation session, use Labs 1 to 5 and the investigation part of Lab 16.
For a compliance session, use Labs 1, 7, 10, and 11.
For an automation session, use Labs 2 and 13 to 15.
Include the relevant prerequisites before each selected lab.

## Before you start

- Obtain approved console access to both environments.
- Ask the instructor for your participant ID and permitted sandpit scope.
- For automation labs, install `lacework`, `jq`, Git, and an approved AI coding agent.
- Configure separate CLI profiles with approved credentials.
- Read the [instructor guide](instructor-guide.md) before delivering the class.

Cloud onboarding is a separate course: [AWS integration workshop](https://github.com/andrewbearsley/forticnapp-workshop-aws-automated).
Use it when participants need to connect an AWS account or install workload agents.

## Workshop family

| Offering | Outcome | Suggested repository name |
|---|---|---|
| AWS integration | Connect AWS and verify data collection | Keep the existing AWS workshop |
| **Operations** | Investigate, assess, configure, and automate | `forticnapp-workshop-operations` |
| Detection engineering | Develop and test deeper custom detection use cases | `forticnapp-workshop-detection-engineering` |

Operations is the working title for this course. Its subtitle states the scope.
Detection engineering is a possible future course, not an existing offering.

## References

- [FortiCNAPP documentation](https://docs.fortinet.com/product/forticnapp)
- [CLI reference](https://docs.fortinet.com/document/forticnapp/latest/cli-reference)
- [API endpoint documentation](https://api.lacework.net/api/v2/docs)
- [FortiCNAPP agent skill](https://github.com/andrewbearsley/forticnapp-lacework-skill)

## Build the offline copy

Install Python dependencies from `requirements.txt`. Install Google Chrome.
Run `python tools/build_pdf.py`. Run `python tools/preflight.py` before delivery.
The PDF includes this overview, every lab, and the evidence worksheet. Instructor notes remain separate.

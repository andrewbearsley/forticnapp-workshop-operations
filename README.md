# FortiCNAPP Operations Workshop
Reading offline? Download the [workshop PDF](forticnapp-workshop-operations.pdf).

Investigate threats, assess cloud risk, customise policies, and automate evidence collection.

Start with a composite alert. Follow its observations to the affected resources.
Then build custom policies and CIS reports for AWS and Azure.

## Who this workshop is for

Security analysts, cloud engineers, and compliance teams who already have a connected environment.
You need basic AWS and Azure knowledge. You do not need previous LQL experience.

## Environments

| Environment | Use | Access |
|---|---|---|
| **FORTIDEMO-2026-04** | Investigate prepared alerts and findings | Read-only |
| **FORTINETAPACDEMO** | Create workshop queries, policies, frameworks, and reports | Read/write |

Use a unique participant ID, such as `ab04`.
Use `Workshop-ab04-` at the start of every object name that you create.
Record each object's ID in [your evidence worksheet](evidence-worksheet.md).

## Investigate and assess

| Lab | Task | Environment |
|---|---|---|
| [1](lab-01/README.md) | Read the console and confirm scope | Demo |
| [2](lab-02/README.md) | Investigate a composite alert | Demo |
| [3](lab-03/README.md) | Follow cloud activity and individual alerts | Demo |
| [4](lab-04/README.md) | Find resources with Explorer and Inventory | Demo |
| [5](lab-05/README.md) | Investigate risk and attack paths | Demo |
| [6](lab-06/README.md) | Examine identity and vulnerability context | Demo |
| [7](lab-07/README.md) | Interpret AWS and Azure CIS findings | Demo, then sandpit |
| [8](lab-08/README.md) | Understand policy types and tuning controls | Sandpit |

## Configure and automate

| Lab | Task | Environment |
|---|---|---|
| [9](lab-09/README.md) | Build and test a custom query and policy | Sandpit |
| [10](lab-10/README.md) | Build a custom compliance framework | Sandpit |
| [11](lab-11/README.md) | Configure AWS and Azure CIS reports | Sandpit |
| [12](lab-12/README.md) | Check coverage and notification routing | Sandpit |
| [13](lab-13/README.md) | Use the CLI with explicit tenant scope | Both, read-only |
| [14](lab-14/README.md) | Retrieve evidence through the API | Both, read-only |
| [15](lab-15/README.md) | Investigate with the FortiCNAPP agent skill | Both, read-only |
| [16](lab-16/README.md) | Complete the investigation and remove lab objects | Both |

## Before you start

- Sign in to both lab environments.
- Have your participant ID and assigned AWS and Azure scopes ready.
- For automation labs, install `lacework`, `jq`, Git, and an approved AI coding agent.
- Configure separate CLI profiles with approved credentials.

Cloud onboarding is a separate course: [AWS integration workshop](https://github.com/andrewbearsley/forticnapp-workshop-aws-automated).
Use it to connect an AWS account or install workload agents.

## References

- [FortiCNAPP documentation](https://docs.fortinet.com/product/forticnapp)
- [CLI reference](https://docs.fortinet.com/document/forticnapp/latest/cli-reference)
- [API endpoint documentation](https://api.lacework.net/api/v2/docs)
- [FortiCNAPP agent skill](https://github.com/andrewbearsley/forticnapp-lacework-skill)

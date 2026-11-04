# FortiCNAPP Operations Workshop
Reading offline? Download the [workshop PDF](forticnapp-workshop-operations.pdf).

Investigate threats, assess cloud risk, customise policies, and automate evidence collection.

Start with a composite alert. Follow its observations to the affected resources.
Then build custom policies and CIS reports for AWS and Azure.
Use your findings to present a short investigation at the end.

## Who this workshop is for

Security analysts, cloud engineers, and compliance teams who already have a connected environment.
You need basic AWS and Azure knowledge. You do not need previous LQL experience.

## Environments

| Environment | Use | Access |
|---|---|---|
| **FORTIDEMO-2026-04** | Investigate prepared alerts and findings | Read-only |
| **FORTINETAPACDEMO** | Create workshop queries, policies, frameworks, and reports | Read/write |

## Investigate and assess

| Lab | Task | Environment |
|---|---|---|
| [1](lab-01/README.md) | What can FortiCNAPP tell you? | Demo |
| [2](lab-02/README.md) | Composite alerts: is this host compromised? | Demo |
| [3](lab-03/README.md) | Explore Threat Center beyond composite alerts | Demo |
| [4](lab-04/README.md) | Find the resources behind the alert | Demo |
| [5](lab-05/README.md) | Where could an attacker go next? | Demo |
| [6](lab-06/README.md) | Decide what to fix first | Demo |
| [7](lab-07/README.md) | What do your CIS results tell you? | Demo, then sandpit |
| [8](lab-08/README.md) | Choose the right policy control | Sandpit |

## Configure and automate

| Lab | Task | Environment |
|---|---|---|
| [9](lab-09/README.md) | Turn a security question into a policy | Sandpit |
| [10](lab-10/README.md) | Build a compliance framework for your review | Sandpit |
| [11](lab-11/README.md) | Build AWS and Azure CIS reports your team can use | Sandpit |
| [12](lab-12/README.md) | Can you trust the data behind your findings? | Sandpit |
| [13](lab-13/README.md) | Ask the same questions through the CLI | Both, read-only |
| [14](lab-14/README.md) | Get the evidence behind an alert through the API | Both, read-only |
| [15](lab-15/README.md) | Repeat your investigation with the FortiCNAPP agent skill | Both, read-only |
| [16](lab-16/README.md) | Present your findings and clean up | Both |

Cloud onboarding is a separate course: [AWS integration workshop](https://github.com/andrewbearsley/forticnapp-workshop-aws-automated).
Use it to connect an AWS account or install workload agents.

## References

- [FortiCNAPP documentation](https://docs.fortinet.com/product/forticnapp)
- [CLI reference](https://docs.fortinet.com/document/forticnapp/latest/cli-reference)
- [API endpoint documentation](https://api.lacework.net/api/v2/docs)
- [FortiCNAPP agent skill](https://github.com/andrewbearsley/forticnapp-lacework-skill)

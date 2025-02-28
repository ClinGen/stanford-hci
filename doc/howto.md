# How-To Guides

How-to guides take the reader through the steps required to solve a real-world
problem. They are recipes, directions to achieve a specific end. Unlike
tutorials, they typically assume a fair amount of prerequisite knowledge.

## Contents

- [How to deploy the HCI](#how-to-deploy-the-hci)
- [How to resolve Terraform state lock error](#how-to-resolve-terraform-state-lock-error)
- [How to authenticate to ECR](#how-to-authenticate-to-ecr)

## How to deploy the HCI

I (Liam) wrote a script to deploy the HCI. There's an explanation of the
script [here](./explanation.md#the-deploy-script). To use the script,
invoke the following command, replacing `<environment>` with `stag` for
the staging environment (`hci-test.clinicalgenome.org`) or `prod` for the
production environment (`hci.clinicalgenome.org`).

```
./run deploy:<environment>
```

## How to create a superuser for the HCI

When you first build the infrastructure for the HCI, you'll need to
create a Django superuser. If the HCI were deployed on a platform with
SSH access, you could SSH in, and create the superuser on the command
line. Using Fargate means we don't have SSH access, so we have an ECS
task that we can run via a script. The script can be found
[here](../scripts/superuser.py).

## How to resolve Terraform state lock error

I (Liam) have run into an issue a couple of times where if I hit `ctrl-c` when
running `terraform apply`, the next time I run it, I see an error like:

```
Error: Error acquiring the state lock
[...]
```

I think this has to do with the first `terraform apply` acquiring but not
releasing the state file lock when I press `ctrl-c`. I found
[this](https://stackoverflow.com/a/62190032) Stack Overflow answer. TL;DR, the
solution is to:

```
cd infra
terraform force-unlock -force <ID>
```

The `<ID>` should be replaced by the one mentioned in the error message.

## How to authenticate to ECR

To push a Docker image to ECR, you need to first authenticate to ECR. There's
a task in the `run` script that does this. Sometimes it will fail. If you are
using Colima, you might be able to fix this by restarting Colima:
`colima restart`.

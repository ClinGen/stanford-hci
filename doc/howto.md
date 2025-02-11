# How-To Guides

How-to guides take the reader through the steps required to solve a real-world
problem. They are recipes, directions to achieve a specific end. Unlike
tutorials, they typically assume a fair amount of prerequisite knowledge.

## Contents

- [How to resolve Terraform state lock error](#how-to-resolve-terraform-state-lock-error)
- [How to authenticate to ECR](#how-to-authenticate-to-ecr)

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

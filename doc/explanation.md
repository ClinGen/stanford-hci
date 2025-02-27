# Explanation

## Contents

- [Environment variables and secrets](#environment-variables-and-secrets)
- [Infrastructure](#infrastructure)
- [Using Colima](#using-colima)
- [The deploy script](#the-deploy-script)

## Environment variables and secrets

Applications usually need some variables that depend on where they're running.
These are called environment variables. They also need variables that should be
kept secret, like API keys, passwords, etc. Lots of applications list these
variables in a `.env` file. Before the application is started, the environment
variables defined in a `.env` file are set so that the application can access
them during runtime. The neat part is that these environment variables aren't
included in the source code of the application. For most applications, this is
easy enough to do. When we introduce containers, code pipelines, etc. making
environment variables and secrets available to the application is more
difficult. This is why most cloud service providers have a service like AWS's
Secrets Manager service. Services like AWS's Secrets Manager allow us to
securely store the secrets the application needs. At runtime, the application
can access the secrets stored in AWS Secrets Manager by making an HTTP request
to the service. Most AWS services also allow you to set non-secret environment
variables. For example, in our `ecs.tf` file, we set a handful of environment
variables that are needed by the HCI app.

We use AWS's Secrets Manager for the HCI. We define the secrets we want to store
in AWS's Secrets Manager service in our Terraform code, and we set those secrets
in a `secrets.tfvars` file that is encrypted using OpenSSL with the AES-256-CBC
encryption algorithm. (It needs to be decrypted before it can be used.) Check
the `run` script for how to encrypt and decrypt the `secrets.tfvars` file. The
`secrets.tf` file declares the secrets to be stored in AWS's Secrets Manager
service.

## Infrastructure

For an in-depth discussion of how I (Liam) made infrastructure decisions for
this project, see [this PDF](./explanation-infrastructure.pdf).

The core AWS services we use for the HCI are Elastic Container Service
(ECS) and Relational Database Service (RDS). There's a lot more to the
infrastructure than ECS and RDS, but they are the core services that we
rely on. Everything else in the Terraform code can be thought of as
stuff we need to wire everything up. ECS allows us to run our
containerized application. We leverage Fargate, which (in theory) makes
scaling the application and managing its infrastructure easier. RDS
allows us to have a managed Postgres database.

The beauty of having a containerized application is that we could (in
theory) run it anywhere. We could move to a different cloud provider, we
could run the container on a cheap virtual private server in the cloud,
or we could run it on an on-prem server. Of course, that would be a fair
bit of work, but the application code is decoupled from the
infrastructure it runs on.

## Using Colima

I (Liam) experienced several issues with Docker Desktop. I googled around and
found [Colima](https://github.com/abiosoft/colima). Colima seems to solve some
(maybe all) of the problems I was having with Docker Desktop. Docker Desktop was
slow, and it seemed to be fairly resource-intensive. It also had some issues
with certificates that I didn't want to deal with.

## The deploy script

I (Liam) have written a script to deploy the HCI to either the staging
environment or the production environment. This script can be found
[here](../scripts/deploy.py). I don't want to document the specifics of
the deployment process because it's possible the specific commands will
change. If you're interested in the specific commands, I encourage you
to read the script. I will document how the deploy script works at a
high level.

Before getting into how the deploy script works, it should be noted that
if you have modified the cloud infrastructure for the HCI using
Terraform, you need to apply those changes before running the deploy
script. The deploy script does not concern itself with the creation of
infrastructure.

Here are the steps the deploy script takes:

### Database migration

The deploy script will ask the user whether they want to migrate the
database. If any of the object relational mapper (ORM) models have
changed, that will probably necessitate changes in the way the database
tables are structured. This is because generally each Django model
corresponds to a database table.

### Authenticate to the container registry

The deploy script will ask the user whether they want to authenticate to
the container registry. A container registry is where container images
are stored. Since we build our container images locally, we have to push
them up to the container registry. To do that, we have to essentially
"log in" to the container registry before we push our container image.
You probably only need to do this if you haven't done it in a while.

### Build a new container image

The deploy script will ask the user whether they want to build a new
container image. A container image is basically a set of static files
that contain all the code and dependencies necessary to run an
application. If you've changed the source code of the application,
you'll need to create a new container image.

### Push the container image to the container registry

The deploy script will ask the user whether they want to push the
container image to the container registry. If you created a new
container image, then push it.

### Update the container service

The deploy script will ask the user whether they want to update the
service that runs the container. If you built a new container image,
then you should push it.

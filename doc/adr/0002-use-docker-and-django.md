# 2. Use Docker and Django

Date: 2024-10-22

## Status

Accepted

## Context

I (Liam) want to use Docker for the HCI because it makes the following
things easier:

- setting up a development environment
- CI/CD
- moving the HCI to a different cloud services provider
- running a test instance of the HCI on the on-prem server

I want to get away from the [Serverless](https://serverless.com/)
framework we use for the GCI and the VCI because it requires you to use
AWS's Lambda service, which has a data transfer limit and an execution
time limit. Docker and a cloud service like AWS's Elastic Container
Service (ECS) don't have these limits.

I want to use Django because it's an opinionated, tried-and-true web
framework that has many useful features and excellent documentation.
Also, the developers on our team have Python expertise.

To Dockerize the HCI, I copied and modified
[docker-django-example](https://github.com/nickjj/docker-django-example).
This example sets up a lot of stuff that I would have otherwise had to
set up myself, which (A) would have been tedious, and (B) probably
wouldn't be as good.

## Decision

The HCI will use Docker and [docker-django-example](https://github.com/nickjj/docker-django-example).

## Consequences

On the one hand, we avoid some of the problems we've encountered with
the Serverless framework, and gain the benefits listed in the context
section of this ADR. On the other hand, we have to learn a new
development workflow, and we have to use a different set of AWS
services.

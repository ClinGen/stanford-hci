// This file configures AWS Identity and Access Management (IAM) for the HCI.

resource "aws_iam_role" "hci_ecs_task_execution_role" {
  name               = "hci_ecs_task_execution_role_${terraform.workspace}"
  assume_role_policy = file("policies/ecs.json")
}

resource "aws_iam_role_policy" "hci_ecs_task_execution_role_policy" {
  name   = "hci_ecs_task_execution_role_policy_${terraform.workspace}"
  policy = file("policies/ecs_task_execution.json")
  role   = aws_iam_role.hci_ecs_task_execution_role.id
}

resource "aws_iam_role" "hci_ecs_service_role" {
  name               = "hci_ecs_service_role_${terraform.workspace}"
  assume_role_policy = file("policies/ecs.json")
}

resource "aws_iam_role_policy" "hci_ecs_service_role_policy" {
  name   = "hci_ecs_service_role_policy_${terraform.workspace}"
  policy = file("policies/ecs_service.json")
  role   = aws_iam_role.hci_ecs_service_role.id
}
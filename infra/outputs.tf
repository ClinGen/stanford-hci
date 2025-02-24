// Outputs values that are obtained when you run `terraform apply`.

output "alb_hostname" {
  value = aws_lb.hci.dns_name
}

output "ecs_task_execution_role_arn" {
  value       = aws_iam_role.hci_ecs_task_execution_role.arn
  description = "ARN for the ECS Task Execution Role"
}

output "subnets" {
  value = [aws_subnet.hci_public_subnet_1.id, aws_subnet.hci_public_subnet_2.id]
}

output "security_group" {
  value = aws_security_group.hci_ecs_fargate.id
}
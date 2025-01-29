// This file configures our ECS cluster.

resource "aws_ecs_cluster" "hci" {
  name = "hci_cluster_${terraform.workspace}"
}

resource "aws_ecs_task_definition" "hci" {
  family                   = "hci_${terraform.workspace}"
  network_mode             = "awsvpc" // This is required for Fargate.
  requires_compatibilities = ["FARGATE"]
  cpu                      = var.hci_fargate_cpu
  memory                   = var.hci_fargate_memory
  execution_role_arn       = aws_iam_role.hci_ecs_task_execution_role.arn
  task_role_arn            = aws_iam_role.hci_ecs_task_execution_role.arn
  container_definitions = jsonencode([
    {
      name      = "hci_${terraform.workspace}"
      image     = var.hci_docker_image_url
      essential = true
      cpu       = 10
      memory    = 512
      portMappings = [
        {
          containerPort = 80
          hostPort      = 80
        }
      ]
      logConfiguration = {
        logDriver = "awslogs"
        options = {
          awslogs-group         = "/ecs/hci_${terraform.workspace}"
          awslogs-region        = "us-west-2"
          awslogs-stream-prefix = "hci_logs_${terraform.workspace}"
        }
      }
    }
  ])
}

resource "aws_ecs_service" "hci" {
  name            = "hci_service_${terraform.workspace}"
  cluster         = aws_ecs_cluster.hci.id
  task_definition = aws_ecs_task_definition.hci.arn
  launch_type     = "FARGATE"
  desired_count   = var.hci_app_count
  network_configuration {
    subnets          = [aws_subnet.hci_public_subnet_1.id, aws_subnet.hci_public_subnet_2.id]
    security_groups  = [aws_security_group.hci_ecs_fargate.id]
    assign_public_ip = true
  }
  load_balancer {
    target_group_arn = aws_alb_target_group.hci_target_group.arn
    container_name   = "hci_${terraform.workspace}"
    container_port   = 8000
  }
}
// Configures our ECS service.

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
          containerPort = 8000
          hostPort      = 8000
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
      environment = [
        {
          name = "HCI_HOST",
          value = var.hci_host
        },
        {
          name = "RDS_DB_NAME"
          value = var.hci_rds_db_name
        },
        {
          name = "RDS_USERNAME"
          value = var.hci_rds_username
        },
        {
          name = "RDS_HOSTNAME"
          value = aws_db_instance.hci_rds.address
        },
        {
          name = "RDS_PORT"
          value = "5432"
        }
      ]
    }
  ])
  depends_on = [aws_db_instance.hci_rds]
}

resource "aws_ecs_service" "hci" {
  name                 = "hci_service_${terraform.workspace}"
  cluster              = aws_ecs_cluster.hci.id
  task_definition      = aws_ecs_task_definition.hci.arn
  launch_type          = "FARGATE"
  desired_count        = var.hci_app_count
  force_new_deployment = true
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

resource "aws_ecs_task_definition" "hci_db_migration" {
  family                = "hci_db_migration_task"
  network_mode          = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  cpu                   = var.hci_fargate_cpu
  memory                = var.hci_fargate_memory
  execution_role_arn    = aws_iam_role.hci_ecs_task_execution_role.arn
  container_definitions = jsonencode([
    {
      name  = "hci_db_migration_container"
      image = var.hci_docker_image_url
      environment: [
        {
          name = "HCI_HOST",
          value = var.hci_host
        },
        {
            "name": "RDS_DB_NAME",
            "value": var.hci_rds_db_name
        },
        {
            "name": "RDS_USERNAME",
            "value": var.hci_rds_username
        },
        {
            "name": "RDS_PASSWORD",
            "value": var.hci_rds_password
        },
        {
            "name": "RDS_HOSTNAME",
            "value": aws_db_instance.hci_rds.address
        },
        {
            "name": "RDS_PORT",
            "value": "5432"
        }
      ],
      command = ["./run", "migrate"]
      logConfiguration = {
        logDriver = "awslogs"
        options = {
          awslogs-group         = "/ecs/hci_${terraform.workspace}"
          awslogs-region        = "us-west-2"
          awslogs-stream-prefix = "hci_logs_${terraform.workspace}"
        }
      }
      portMappings = [
        {
          containerPort = 8000
        }
      ]
    }
  ])
}

// When you first create the infrastructure for the HCI, you'll need a
// superuser. You can't SSH into Fargate ECS containers, so we have this
// task.
resource "aws_ecs_task_definition" "hci_createsuperuser" {
  family                = "hci_createsuperuser_task"
  network_mode          = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  cpu                   = var.hci_fargate_cpu
  memory                = var.hci_fargate_memory
  execution_role_arn    = aws_iam_role.hci_ecs_task_execution_role.arn
  container_definitions = jsonencode([
    {
      name  = "hci_createsuperuser_container"
      image = var.hci_docker_image_url
      environment: [
        {
          name = "HCI_HOST",
          value = var.hci_host
        },
        {
          "name": "RDS_DB_NAME",
          "value": var.hci_rds_db_name
        },
        {
          "name": "RDS_USERNAME",
          "value": var.hci_rds_username
        },
        {
          "name": "RDS_PASSWORD",
          "value": var.hci_rds_password
        },
        {
          "name": "RDS_HOSTNAME",
          "value": aws_db_instance.hci_rds.address
        },
        {
          "name": "RDS_PORT",
          "value": "5432"
        },
        {
          "name": "DJANGO_SUPERUSER_USERNAME",
          "value": var.hci_django_superuser_username
        },
        {
          "name": "DJANGO_SUPERUSER_PASSWORD",
          "value": var.hci_django_superuser_password
        },
        {
          "name": "DJANGO_SUPERUSER_EMAIL",
          "value": var.hci_django_superuser_email
        },
      ],
      command = ["./run", "createsuperuser"]
      logConfiguration = {
        logDriver = "awslogs"
        options = {
          awslogs-group         = "/ecs/hci_${terraform.workspace}"
          awslogs-region        = "us-west-2"
          awslogs-stream-prefix = "hci_logs_${terraform.workspace}"
        }
      }
      portMappings = [
        {
          containerPort = 8000
        }
      ]
    }
  ])
}

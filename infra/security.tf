// Configures the security groups for the HCI.

// Configure the application load balancer (ALB) security group.
// (Internet -> ALB)
resource "aws_security_group" "hci_load_balancer" {
  name        = "hci_load_balancer_security_group_${terraform.workspace}"
  description = "This security group controls access to the ALB."
  vpc_id      = aws_vpc.hci_vpc.id

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

// Configure the ECS Fargate security group.
// (ALB -> Fargate)
resource "aws_security_group" "hci_ecs_fargate" {
  name        = "hci_ecs_fargate_security_group_${terraform.workspace}"
  description = "This security group allows inbound access from the ALB."
  vpc_id      = aws_vpc.hci_vpc.id

  ingress {
    from_port       = 0
    to_port         = 0
    protocol        = "-1"
    security_groups = [aws_security_group.hci_load_balancer.id]
  }

  // There is no SSH ingress rule since Fargate tasks are abstracted and not
  // directly accessible via SSH.

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

// Configure the RDS security group.
// (Fargate -> RDS)
resource "aws_security_group" "rds" {
  name        = "rds-security-group"
  description = "This allows traffic into RDS from Fargate."
  vpc_id      = aws_vpc.hci_vpc.id

  ingress {
    protocol        = "tcp"
    from_port       = "5432"
    to_port         = "5432"
    security_groups = [aws_security_group.hci_ecs_fargate.id]
  }

  egress {
    protocol    = "-1"
    from_port   = 0
    to_port     = 0
    cidr_blocks = ["0.0.0.0/0"]
  }
}
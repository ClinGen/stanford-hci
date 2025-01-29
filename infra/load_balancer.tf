// Configure the load balancer for the HCI.

// Create the load balancer.
resource "aws_lb" "hci" {
  name               = "hci-alb-${terraform.workspace}"
  load_balancer_type = "application"
  internal           = false
  security_groups    = [aws_security_group.hci_load_balancer.id]
  subnets            = [aws_subnet.hci_public_subnet_1.id, aws_subnet.hci_public_subnet_2.id]
}

// Create the target group.
resource "aws_alb_target_group" "hci_target_group" {
  name        = "hci-tg-${terraform.workspace}"
  port        = 80
  protocol    = "HTTP"
  vpc_id      = aws_vpc.hci_vpc.id
  target_type = "ip"

  health_check {
    path                = var.hci_health_check_path
    port                = "traffic-port"
    healthy_threshold   = 5
    unhealthy_threshold = 2
    timeout             = 2
    interval            = 5
    matcher             = "200"
  }
}

// Redirect traffic from the load balancer to the target group.
resource "aws_alb_listener" "hci_ecs_alb_http_listener" {
  load_balancer_arn = aws_lb.hci.id
  port              = "80"
  protocol          = "HTTP"
  depends_on        = [aws_alb_target_group.hci_target_group]

  default_action {
    type             = "forward"
    target_group_arn = aws_alb_target_group.hci_target_group.arn
  }
}
// Configures how we auto-scale our ECS service.

resource "aws_appautoscaling_target" "hci_ecs_target" {
  max_capacity       = var.hci_autoscale_max
  min_capacity       = var.hci_autoscale_min
  resource_id        = "service/${aws_ecs_cluster.hci.name}/${aws_ecs_service.hci.name}"
  scalable_dimension = "ecs:service:DesiredCount"
  service_namespace  = "ecs"
}

resource "aws_appautoscaling_policy" "hci_ecs_policy" {
  name               = "hci_ecs_auto_scaling_policy"
  policy_type        = "TargetTrackingScaling"
  resource_id        = aws_appautoscaling_target.hci_ecs_target.resource_id
  scalable_dimension = aws_appautoscaling_target.hci_ecs_target.scalable_dimension
  service_namespace  = aws_appautoscaling_target.hci_ecs_target.service_namespace

  target_tracking_scaling_policy_configuration {
    predefined_metric_specification {
      predefined_metric_type = "ECSServiceAverageCPUUtilization"
    }
    target_value       = 75
    scale_in_cooldown  = 300
    scale_out_cooldown = 300
  }
}
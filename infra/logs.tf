// Configures logging for the HCI.

resource "aws_cloudwatch_log_group" "hci_log_group" {
  name              = "/ecs/hci_${terraform.workspace}"
  retention_in_days = var.hci_log_retention_in_days
}
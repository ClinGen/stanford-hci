// This module establishes secrets needed by the HCI application. These secrets
// are stored in AWS's Secrets Manager service.

resource "aws_secretsmanager_secret" "hci_django_secret_key" {
  name        = "hci_django_secret_key"
  description = "This is the secret key for the HCI's Django application."
  tags = {
    Environment = terraform.workspace
    Project     = "HCI"
  }
}

resource "aws_secretsmanager_secret_version" "hci_django_secret_key_version" {
  secret_id     = aws_secretsmanager_secret.hci_django_secret_key.id
  secret_string = var.hci_django_secret_key
}
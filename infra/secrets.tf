// This module establishes secrets needed by the HCI application. These secrets
// are stored in AWS's Secrets Manager service.

resource "aws_secretsmanager_secret" "hci_django_secret_key" {
  name        = "hci_django_secret_key_${terraform.workspace}"
  description = "This is the secret key for the HCI's Django application."
}

resource "aws_secretsmanager_secret_version" "hci_django_secret_key_version" {
  secret_id     = aws_secretsmanager_secret.hci_django_secret_key.id
  secret_string = var.hci_django_secret_key
}
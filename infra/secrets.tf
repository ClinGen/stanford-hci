// This module establishes secrets needed by the HCI application. These secrets
// are stored in AWS's Secrets Manager service.

resource "aws_secretsmanager_secret" "hci-django-secret-key-secret" {
  name        = "hci-django-secret-key"
  description = "This is the secret key for the HCI's Django application."
}

resource "aws_secretsmanager_secret_version" "hci-django-secret-key-version" {
  secret_id     = aws_secretsmanager_secret.hci-django-secret-key-secret.id
  secret_string = var.hci_django_secret_key
}
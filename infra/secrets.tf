// Establishes secrets needed by the HCI application. These secrets are stored
// in AWS's Secrets Manager service.

resource "aws_secretsmanager_secret" "hci_django_secret_key" {
  name        = "hci_django_secret_key_${terraform.workspace}"
  description = "This is the secret key for the HCI's Django application."
  tags = {
    Environment = terraform.workspace
    Project     = "HCI"
  }
  recovery_window_in_days = 0
}

resource "aws_secretsmanager_secret_version" "hci_django_secret_key_version" {
  secret_id     = aws_secretsmanager_secret.hci_django_secret_key.id
  secret_string = var.hci_django_secret_key
}

resource "aws_secretsmanager_secret" "hci_rds_password" {
  name        = "hci_rds_password_${terraform.workspace}"
  description = "This is the password for the HCI's RDS database."
  tags = {
    Environment = terraform.workspace
    Project     = "HCI"
  }
  recovery_window_in_days = 0
}

resource "aws_secretsmanager_secret_version" "hci_rds_password_version" {
  secret_id     = aws_secretsmanager_secret.hci_rds_password.id
  secret_string = var.hci_rds_password
}

resource "aws_secretsmanager_secret" "hci_django_superuser_username" {
  name        = "hci_django_superuser_username_${terraform.workspace}"
  description = "This is the username for the HCI's superuser."
  tags = {
    Environment = terraform.workspace
    Project     = "HCI"
  }
  recovery_window_in_days = 0
}

resource "aws_secretsmanager_secret_version" "hci_django_superuser_username_version" {
  secret_id     = aws_secretsmanager_secret.hci_django_superuser_username.id
  secret_string = var.hci_django_superuser_username
}

resource "aws_secretsmanager_secret" "hci_django_superuser_email" {
  name        = "hci_django_superuser_email_${terraform.workspace}"
  description = "This is the email for the HCI's superuser."
  tags = {
    Environment = terraform.workspace
    Project     = "HCI"
  }
  recovery_window_in_days = 0
}

resource "aws_secretsmanager_secret_version" "hci_django_superuser_email_version" {
  secret_id     = aws_secretsmanager_secret.hci_django_superuser_email.id
  secret_string = var.hci_django_superuser_email
}

resource "aws_secretsmanager_secret" "hci_django_superuser_password" {
  name        = "hci_django_superuser_password_${terraform.workspace}"
  description = "This is the password for the HCI's superuser."
  tags = {
    Environment = terraform.workspace
    Project     = "HCI"
  }
  recovery_window_in_days = 0
}

resource "aws_secretsmanager_secret_version" "hci_django_superuser_password_version" {
  secret_id     = aws_secretsmanager_secret.hci_django_superuser_password.id
  secret_string = var.hci_django_superuser_password
}

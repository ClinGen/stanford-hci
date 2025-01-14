// This module houses anything related to the Elastic Container Registry
// repository where the Docker images for the HCI are stored.

// Create the ECR repository.
resource "aws_ecr_repository" "hci" {
  name                 = var.hci_registry_name
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }
}
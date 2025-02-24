// Houses anything related to the Elastic Container Registry repository where
// the Docker images for the HCI are stored.

// Create the ECR repository.
resource "aws_ecr_repository" "hci" {
  name                 = "hci_registry_${terraform.workspace}"
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }
}
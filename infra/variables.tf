// In this module we declare (but we don't define) the variables we will use.

//==============================================================================
// Declare sensitive variables
//==============================================================================

variable "hci_django_secret_key" {
  description = "This is the secret key for the HCI's Django application."
  type        = string
  sensitive   = true
}

//==============================================================================
// Declare non-sensitive variables
//==============================================================================

variable "hci_registry_name" {
  description = "This is the name of the registry where the HCI's Docker images live."
  type = string
}
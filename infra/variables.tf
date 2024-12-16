// In this module we declare (but we don't define) the variables we will use.

variable "hci_django_secret_key" {
  description = "This is the secret key for the HCI's Django application."
  type        = string
  sensitive   = true
}
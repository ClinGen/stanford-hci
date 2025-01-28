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

// Classless Inter-Domain Routing (CIDR) allows network routers to route data
// packets to the respective device based on the indicated subnet. Instead of
// classifying the IP address based on classes, routers retrieve the network
// and host address as specified by the CIDR suffix.
variable "hci_public_subnet_1_cidr" {
  description = "This is the CIDR block for the HCI's public subnet 1."
  default     = "10.0.1.0/24"
}
variable "hci_public_subnet_2_cidr" {
  description = "This is the CIDR block for the HCI's public subnet 2."
  default     = "10.0.2.0/24"
}
variable "hci_private_subnet_1_cidr" {
  description = "This is the CIDR block for the HCI's private subnet 1."
  default     = "10.0.3.0/24"
}
variable "hci_private_subnet_2_cidr" {
  description = "This is the CIDR block for the HCI's private subnet 2."
  default     = "10.0.4.0/24"
}

// AWS has the concept of a Region, which is a physical location around the
// world where we cluster data centers. We call each group of logical data
// centers an Availability Zone. Each AWS Region consists of a minimum of three,
// isolated, and physically separate AZs within a geographic area. An AZ is one
// or more discrete data centers with redundant power, networking, and
// connectivity in an AWS Region. In this case the region is us-west-2 (Oregon).
variable "hci_availability_zones" {
  description = "This is a list of the HCI's availability zones."
  type        = list(string)
  default     = ["us-west-2b", "us-west-2c"]
}
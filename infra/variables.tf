// In this file we declare (but we don't define) the variables we will use.

//==============================================================================
// Declare sensitive variables
//==============================================================================

variable "hci_django_secret_key" {
  description = "This is the secret key for the HCI's Django application."
  type        = string
  sensitive   = true
}

variable "hci_rds_password" {
  description = "This is the password for the HCI's RDS database."
  type = string
  sensitive = true
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

variable "hci_health_check_path" {
  description = "This is the health check path for the HCI."
  default     = "/ping/"
}

variable "hci_log_retention_in_days" {
  default = 30
}

variable "hci_docker_image_url" {
  description = "This is the URL for the Docker image to run in the ECS cluster."
  default     = "<AWS_ACCOUNT_ID>.dkr.ecr.us-west-2.amazonaws.com/<HCI_ECR_NAME>:latest"
}

variable "hci_app_count" {
  description = "This is the number of Docker containers to run."
  default     = 2
}

// Establish Fargate variables.
variable "hci_fargate_cpu" {
  description = "This is the amount of CPU for the Fargate task, e.g. '256' (.25 vCPU)."
  default     = "256"
}
variable "hci_fargate_memory" {
  description = "This is the amount of memory for the Fargate task, e.g. '512' (0.5GB)."
  default     = "512"
}

// Establish autoscale variables.
variable "hci_autoscale_min" {
  description = "This is the minimum number of tasks the HCI will run."
  default     = "1"
}
variable "hci_autoscale_max" {
  description = "This is the maximum number of tasks the HCI will run."
  default     = "10"
}

// Establish RDS variables.
variable "hci_rds_db_name" {
  description = "This is the name of the HCI's RDS database."
}
variable "hci_rds_username" {
  description = "This is the username for the HCI's RDS database."
}
variable "hci_rds_instance_class" {
  description = "This is the instance type for the HCI's RDS database."
  default     = "db.t3.micro"
}
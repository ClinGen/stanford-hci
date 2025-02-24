// Defines the network resources for the HCI.

// Create a virtual private cloud (VPC).
resource "aws_vpc" "hci_vpc" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_support   = true
  enable_dns_hostnames = true
}

// Create public subnets.
resource "aws_subnet" "hci_public_subnet_1" {
  cidr_block        = var.hci_public_subnet_1_cidr
  vpc_id            = aws_vpc.hci_vpc.id
  availability_zone = var.hci_availability_zones[0]
}
resource "aws_subnet" "hci_public_subnet_2" {
  cidr_block        = var.hci_public_subnet_2_cidr
  vpc_id            = aws_vpc.hci_vpc.id
  availability_zone = var.hci_availability_zones[1]
}

// Create private subnets.
resource "aws_subnet" "hci_private_subnet_1" {
  cidr_block        = var.hci_private_subnet_1_cidr
  vpc_id            = aws_vpc.hci_vpc.id
  availability_zone = var.hci_availability_zones[0]
}
resource "aws_subnet" "hci_private_subnet_2" {
  cidr_block        = var.hci_private_subnet_2_cidr
  vpc_id            = aws_vpc.hci_vpc.id
  availability_zone = var.hci_availability_zones[1]
}

// Create route tables.
resource "aws_route_table" "hci_public_route_table" {
  vpc_id = aws_vpc.hci_vpc.id
}
resource "aws_route_table" "hci_private_route_table" {
  vpc_id = aws_vpc.hci_vpc.id
}

// Associate the route tables.
resource "aws_route_table_association" "hci_public_route_1_association" {
  route_table_id = aws_route_table.hci_public_route_table.id
  subnet_id      = aws_subnet.hci_public_subnet_1.id
}
resource "aws_route_table_association" "hci_public_route_2_association" {
  route_table_id = aws_route_table.hci_public_route_table.id
  subnet_id      = aws_subnet.hci_public_subnet_2.id
}
resource "aws_route_table_association" "hci_private_route_1_association" {
  route_table_id = aws_route_table.hci_private_route_table.id
  subnet_id      = aws_subnet.hci_private_subnet_1.id
}
resource "aws_route_table_association" "hci_private_route_2_association" {
  route_table_id = aws_route_table.hci_private_route_table.id
  subnet_id      = aws_subnet.hci_private_subnet_2.id
}

// Create an Elastic IP address for our network address translation (NAT)
// gateway.
resource "aws_eip" "hci_elastic_ip_for_nat_gw" {
  domain                    = "vpc"
  associate_with_private_ip = "10.0.0.5"
  depends_on                = [aws_internet_gateway.hci_igw]
}

// Create a NAT gateway.
resource "aws_nat_gateway" "hci_nat_gw" {
  allocation_id = aws_eip.hci_elastic_ip_for_nat_gw.id
  subnet_id     = aws_subnet.hci_public_subnet_1.id
  depends_on    = [aws_eip.hci_elastic_ip_for_nat_gw]
}
resource "aws_route" "hci_nat_gw_route" {
  route_table_id         = aws_route_table.hci_private_route_table.id
  nat_gateway_id         = aws_nat_gateway.hci_nat_gw.id
  destination_cidr_block = "0.0.0.0/0"
}

// Create an internet gateway.
resource "aws_internet_gateway" "hci_igw" {
  vpc_id = aws_vpc.hci_vpc.id
}

// Route the public subnet traffic through the internet gateway.
resource "aws_route" "hci_public_internet_igw_route" {
  route_table_id         = aws_route_table.hci_public_route_table.id
  gateway_id             = aws_internet_gateway.hci_igw.id
  destination_cidr_block = "0.0.0.0/0"
}
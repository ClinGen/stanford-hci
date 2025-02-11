// This file configures our RDS database.

resource "aws_db_subnet_group" "hci_rds" {
  name       = "hci_rds_${terraform.workspace}"
  subnet_ids = [aws_subnet.hci_private_subnet_1.id, aws_subnet.hci_private_subnet_2.id]
}

resource "aws_db_instance" "hci_rds" {
  identifier              = "hci-rds-${terraform.workspace}"
  db_name                 = var.hci_rds_db_name
  username                = var.hci_rds_username
  password                = var.hci_rds_password
  port                    = "5432"
  engine                  = "postgres"
  engine_version          = "17.2"
  instance_class          = var.hci_rds_instance_class
  allocated_storage       = "20"
  storage_encrypted       = false
  vpc_security_group_ids  = [aws_security_group.rds.id]
  db_subnet_group_name    = aws_db_subnet_group.hci_rds.name
  multi_az                = false
  storage_type            = "gp2"
  publicly_accessible     = false
  backup_retention_period = 7
  skip_final_snapshot     = true
}
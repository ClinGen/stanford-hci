// Configure the subdomain for the HCI.

data "aws_route53_zone" "hci" {
  provider     = aws.route-53
  name         = "clinicalgenome.org"
  private_zone = false
}

resource "aws_route53_record" "hci" {
  provider = aws.route-53
  zone_id  = data.aws_route53_zone.hci.id
  name     = var.hci_subdomain
  type     = "CNAME"
  ttl      = 300
  records = [aws_lb.hci.dns_name]
}
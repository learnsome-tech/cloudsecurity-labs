# Cloud Security & DevSecOps Engineering — lesson m05l01 — Static IaC Scanning: Linting Terraform with Checkov
# https://learnsome.tech/courses/cloudsecurity-course/watch?lesson=m05l01
# © LearnSome.tech
resource "aws_security_group" "bastion" {
  name   = "bastion-ssh"
  vpc_id = var.vpc_id

  ingress {
    description = "SSH for the on-call engineer"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "bastion" {
  ami                    = var.bastion_ami
  instance_type          = "t3.micro"
  vpc_security_group_ids = [aws_security_group.bastion.id]

  root_block_device {
    encrypted = false
  }
}

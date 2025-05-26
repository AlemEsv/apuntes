terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.79.0"
    }
  }

}

provider "aws" {
  # region que estés usando en AWS
  region = "us-east-1"
  # variables de entorno
  access_key = var.access_key
  secret_key = var.secret_key
}

locals {
  extra_tag = "extra_tag"
}

# -----  "instancia" "nombre de la instancia"
resource "aws_instance" "example" {

  count = terraform.workspace == "prod" ? 2 : 1
  # si el workspace es prod se crean 2 instancias
  # sino se crea solo 1

  #for_each = var.service_names

  ami           = "ami-0953476d60561c955" # Amazon Linux 2023 AMI
  instance_type = "t2.micro"

  subnet_id                   = module.vpc.public_subnets[0]
  vpc_security_group_ids      = [module.terraform-sg.security_group_id]
  associate_public_ip_address = true

  tags = {
    ExtraTag = local.extra_tag
    Name     = format("%s-%s",terraform.workspace,count.index)
  }
}
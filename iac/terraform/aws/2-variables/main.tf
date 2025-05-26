terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.0"
    }
  }

}

provider "aws" {
  # region que estés usando en AWS
  region     = "us-east-1"
  # variables de entorno
  access_key = var.access_key
  secret_key = var.secret_key
}

locals{
  extra_tag = "extra_tag"
}

# -----  "instancia" "nombre de la instancia"
resource "aws_instance" "example" {

  # Imagen ID
  ami           = "ami-0953476d60561c955" # Amazon Linux 2023 AMI
  instance_type = "t2.micro"

  tags = {
    ExtraTag = local.extra_tag
  }
}
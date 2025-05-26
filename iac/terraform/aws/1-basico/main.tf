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
  access_key = "AKIAUKXBUA3WE4P7KHUA"
  secret_key = "O4uNkRdRn3LvrabV4b4LwgZ2J8C1JLwoShFkJoyi"
}

# -----  "instancia" "nombre de la instancia"
resource "aws_instance" "example" {

  # Imagen ID
  ami           = "ami-0953476d60561c955" # Amazon Linux 2023 AMI
  instance_type = "t2.micro"
}
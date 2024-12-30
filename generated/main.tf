resource "aws_instance" "example" {
  ami           = "ami-12345678" // AMI ID of the instance
  instance_type = "t2.micro" // Instance type
  region        = "us-east-1" // Region
}
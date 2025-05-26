# muestra comandos en consola
output "instance_ip_addr" {
  # value = aws_instance.example.private_ip
  value = {
    for service, i in aws_instance.example : service => i.private_ip }
  
}
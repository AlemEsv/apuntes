# muestra comandos en consola
output "instance_ip_addr" {
    value = aws_instance.example.private_ip
}
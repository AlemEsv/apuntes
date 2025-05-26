variable "access_key" {
  description = "access_key"
  type        = string
  sensitive   = true # no se muestra en consola
  # default     = "1"
  # sino hay valor default, se pedira que se agrege 
  # su valor al usar el comando terraform apply
}
variable "secret_key" {
  description = "secret_key"
  type        = string
  sensitive   = true
}
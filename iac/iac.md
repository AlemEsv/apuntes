# Infraestructura como código

## Infraestructura

Servicios y plataformas

- servidores
- plataformas de orquestación: kubernetes

## Ventajas de la IaC

- Manejo de infraestructura.

- Automatización de cambios.

- Estandarizar configuraciones.

- Colaboración entre diferentes personas que estén manipulando nuestra infraestructura.

## Principios de IaC

### 1. Reproductibilidad

Un archivo de IaC debe permitir recrear un entorno idéntico cada vez que se aplique.

### 2. Idempotencia

Aplicar varias veces el mismo código no debe cambiar el estado si ya está en el resultado deseado.

### 3. Composabilidad

Definir módulos o bloques reutilizables que puedan combinarse para construir infraestructuras complejas.

### 4. Evolvabilidad

Facilitar la extensión y adaptación de la configuración a medida que cambian los requisitos.

## Configuración drift

## IAM

práctica de seguridad que controla el acceso a los recursos de infraestructura mediante la **asignación de roles** y permisos a usuarios

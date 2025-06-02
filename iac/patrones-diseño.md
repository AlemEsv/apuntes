# Patrones de diseño aplicados a módulos de Terraform

## Patrones de diseño

### Singleton

Asegura que una clase tenga una **única instancia** durante el ciclo de vida de la aplicación y provee un **punto de acceso global**.

- Evitar instancias duplicadas.

### Composite

Trata de manera homogénea objetos indivisibles (hojas) y conjuntos de objetos (compuestos).

- Representar jerarquías compuestas.

### Factory

Define una interfaz para crear objeto, por medio de bloques delega la responsabilidad concreta a subclases.

- Desacoplar la lógica de creación.

### Prototype

Permite crear nuevos objetos copiando una instancia prototipo y modificando solo los atributos necesarios.

- Reutilizar configuraciones base.

### Builder

 Abstrae la creación de un objeto complejo mediante una secuencia de pasos encadenados.

- Construir objetos complejos por pasos.

## Criterio de selección

d

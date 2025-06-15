# Tareas para Sprint 2

## Tarea 1: Script de verificación

- Implementar `script/verificar_estado.py` que lea `tfstate` y genere un JSON/report mínimo con resultados.

## Tarea 2: Refactorizar Sprint 1

- Refactorizar código para corregir errores detectados (por ejemplo, manejo de fallos, validación de parámetros).

## Tarea 3: Actualizar hooks

- Ajustar `.git/hooks/pre-push` para que invoque `verificar_estado.py` y bloquee push si alguna comprobación falla.

## Tarea 4: Implementar Modulo Singleton

- Definir un recurso `null_resource` que cree un archivo único `singleton.lock`.
- Añadir lógica en Bash para impedir múltiples invocaciones simultáneas (crear PID file en /tmp).

## Tarea 5: Implementar Modulo Composite

- Definir múltiples `null_resource` en serie (p. ej., crucial_task, subtask1, subtask2) que representen una jerarquía
- Variables que permitan activar/desactivar subcomponentes.

## Tarea 6: Implementar Modulo Factory

- Módulo Terraform que, según una variable `factory_type`, incluya distintos recursos (usar condicionales `count = var.factory_type == "A" ? 1 : 0`).
- Bash wrapper que genere automáticamente un archivo `factory_config.json` con parámetros por defecto y llame a Terraform con esa configuración.

## Tarea 7: Implementar Modulo Prototype

- Módulo que reciba un bloque HCL completo como string (variable) y lo inyecte usando `templatefile`, generando un recurso a partir de esa plantilla.
- Script Python `clone_prototype.py` que reciba un path a un archivo .tf y lo copie a `prototype/example_timestamp.tf`, reemplazando ciertas variables.

## Tarea 8: Implementar Modulo Builder

- Módulo que permita "encadenar" configuraciones:
    -Variables para definir pasos (step1_enabled, step2_enabled).
    -Provisione recursos en orden si están habilitados.
- Script Bash `build.sh` que lea un archivo de configuración `build_config.yaml` y llame a Terraform de forma encadenada.

## Tarea 9: Mejorar script documentar_modulos.py

- Enlazar la descripción breve del script con la propuesta en el README de cada patrón.
- Colocar 1 o 2 ejemplos para cada patrón
- Implementar código de ejemplo para la invocación en bash.

## Tarea 10: Mejorar script de diagramas

- Generar un diagrama que muestre la relación entre módulos. (por ejemplo, Builder invoca Factory y Prototype).
- El gráfico DOT debe estar dentro de `docs/`

## Tarea 11: Actualizar documentación general

- Completar `README.md` con instrucciones extendidas para Carpeta `src/, scripts/, tests/`.
- Añadir ejemplo de salida de `verificar_estado.py` en Markdown.

# Proyecto 3: "Diseño y compartición de módulos IaC con patrones de software"

## Enunciado general

Crear un **monorepo local** de módulos Terraform que implementen los patrones de diseño: **Singleton**, **Composite**, **Factory**, **Prototype** y **Builder**. Cada patrón se encapsulará en un módulo independiente, con su propio conjunto de variables y outputs, y deberá incluir un **script Bash** para demostrar su uso. El proyecto debe:

- Mostrar claramente la diferencia entre cada patrón.
- Permitir la invocación de cada módulo desde un script Bash `main.sh` que reciba un parámetro (p. ej., `./main.sh --pattern factory`) y despliegue el ejemplo correspondiente.
- Generar, mediante un **script Python** (`documentar_modulos.py`), un **sitio estático local** (carpeta `docs/`) con:

  - Documentación Markdown para cada módulo (explicando patrón, variables y ejemplos de uso).

  - Un diagrama generado con Diagrams.py que represente cómo se combinan los módulos entre sí (por ejemplo, un módulo Factory que llama a Prototype).

El total de líneas de **Terraform + Bash + Python** debe superar las **1000 líneas**, estructuradas en al menos **6 carpetas** para cada patrón más la carpeta de documentación.

## Sprint 1 (días 1-3)

- Estructura inicial del monorepo:

  - Carpetas: `singleton/`, `composite/`, `factory/`, `prototype/`, `builder/`, `scripts/`, `docs/` (vacía).
  - En cada carpeta de patrón, crear:

    - `main.tf` con recurso `null_resource` dummy.
    - `variables.tf` con al menos 2 variables.
    - `outputs.tf` con al menos 1 output.
  - En `scripts/` crear `main.sh` que parse parámetros (`getopts`) e invoque el módulo Terraform que corresponda.
  - Script Python `documentar_modulos.py` que:

    - Lea cada carpeta de patrón.
    - Genere un archivo Markdown inicial en `docs/<patrón>.md` con título, descripción breve ("Ejemplo básico") y listado de variables.
  - Incluir en cada carpeta de patrón un archivo `README.md` explicando brevemente el concepto, con una frase original que no se haya copiado de Internet.

- Configurar **Git submódulos** (vacíos por el momento) para simular futuras versiones de módulos externalizados (no es obligatorio clonarlos, pero la referencia debe existir).
- **Video (10 min)** que muestre:

  - Estructura de monorepo y carpetas creadas.
  - Ejecución de `main.sh --pattern singleton` (debe fallar por falta de implementación, pero mostrar parsing de parámetros).
  - Uso de submódulos Git (agregar un submódulo vacío en `modules/ejemplo_externo`).
  - Primeros contenidos generados en `docs/` por `documentar_modulos.py`.

## Sprint 2 (días 4-8)

- Completar la implementación de cada patrón:

  - **Singleton**:

    - Definir un recurso `null_resource` que cree un archivo único `singleton.lock`.
    - Añadir lógica en Bash para impedir múltiples invocaciones simultáneas (crear PID file en `/tmp`).
  - **Composite**:

    - Definir múltiples `null_resource` en serie (p. ej., `crucial_task`, `subtask1`, `subtask2`) que representen una jerarquía.
    - Variables que permitan activar/desactivar subcomponentes.
  - **Factory**:

    - Módulo Terraform que, según una variable `factory_type`, incluya distintos recursos (usar condicionales `count = var.factory_type == "A" ? 1 : 0`).
    - Bash wrapper que genere automáticamente un archivo `factory_config.json` con parámetros por defecto y llame a Terraform con esa configuración.
  - **Prototype**:

    - Módulo que reciba un bloque HCL completo como string (variable) y lo inyecte usando `templatefile`, generando un recurso a partir de esa plantilla.
    - Script Python `clone_prototype.py` que reciba un path a un archivo `.tf` y lo copie a `prototype/example_<timestamp>.tf`, reemplazando ciertas variables.
  - **Builder**:

    - Módulo que permita "encadenar" configuraciones:

      - Variables para definir pasos (`step1_enabled`, `step2_enabled`).
      - Provisione recursos en orden si están habilitados.
    - Script Bash `build.sh` que lea un archivo de configuración `build_config.yaml` y llame a Terraform de forma encadenada.
- En `docs/`, completar Markdown de cada módulo con:

  - **Descripción original** del patrón (mínimo 100 palabras en español escritas por el equipo).
  - Ejemplos de variables e outputs.
  - Código de ejemplo de invocación en Bash.
- Generar diagrama con Diagrams.py que muestre la relación entre módulos (por ejemplo, Builder invoca Factory y Prototype).
- **Video (10 min)** que muestre:

  - Invocación de cada módulo con `main.sh` y ejemplos de outputs en consola.
  - Funcionamiento del complemento Bash de Singleton (creación de `singleton.lock`).
  - `script Python clone_prototype.py` copiando un archivo HCL.
  - Diagrama actualizado en `docs/`.

## Sprint 3 (días 9-12)

- Refinar módulos y documentación:

  - En cada módulo, agregar al menos **2 variables adicionales** y **un output extra**, comprobando que las pruebas `tfvalidate` pasen.
  - Escribir **tests básicos** de validación local (por ejemplo, un script Bash `test_module_<patrón>.sh` que:

    - Corra `terraform init && terraform apply -auto-approve` y luego valide la creación de archivos dummy o outputs.
    - Ejecute `terraform destroy -auto-approve` al finalizar.
  - En `documentar_modulos.py`:

    - Añadir sección "Patrones combinados" donde se ejemplifique la invocación de Factory dentro de Builder.
    - Generar automáticamente un índice en `docs/README.md` con enlaces a cada `<patrón>.md`.
  - Crear un **script Python** adicional `verificar_ia_docs.py` que:

    - Busque en cada Markdown (docs) coincidencias sospechosas de copiar/parafrasear contenido de línea en Internet (puede usar heurística básica de longitud de oraciones o frases genéricas).
    - Informe en consola posibles secciones "no originales".
- Actualizar `README.md` principal del monorepo con:

  - Instrucciones de uso global (`git clone`, `main.sh --pattern <patrón>`, cómo construir docs).
  - Ejemplos de ejecución de `test_module_*.sh`.
- **Video final (10 min)** que muestre:

  - Ronda de pruebas de cada módulo con `test_module_<patrón>.sh`.
  - Generación final del sitio estático en `docs/` y revisión de contenido.
  - Resultados de `verificar_ia_docs.py` y justificación de originalidad de cada sección.
  - Revisión del tablero Kanban: cerrar todas las Cards y issues de revisión de documentación.

## Rúbrica (pesos y criterios)

- **Implementación de patrones IaC**

  - **Singleton** funciona correctamente y previene invocaciones simultáneas
  - **Composite** con jerarquía de recursos configurables
  - **Factory** que genere recursos condicionales según `factory_type`
  - **Prototype** que inyecte plantillas HCL vía `templatefile` y `clone_prototype.py`
  - **Builder** con flujo encadenado y uso de YAML
- **Modularidad y líneas de código**

  - ≥ 1000 líneas totales entre Terraform, Bash y Python
  - Separación lógica en al menos 6 carpetas/módulos
  - Scripts Bash con validaciones de parámetros y manejo de errores
- **Documentación y originalidad**

  - Markdown de cada módulo con descripción original (≥ 100 palabras)
  - Diagrama generado con Diagrams.py que muestre interdependencias
  - `verificar_ia_docs.py` detecta frases genéricas y equipo justifica en video
- **Pruebas locales de módulos**

  - Existencia de `test_module_<patrón>.sh` para cada patrón
  - Tests validan creación de archivos dummy o outputs
  - Limpieza automática (`terraform destroy`) al finalizar tests
- **Automatización de documentación**

  - `documentar_modulos.py` genera Markdown correctos y actualiza índice
  - Índice en `docs/README.md` con enlaces funcionales
- **Calidad de código y buenas prácticas Git**

  - Commits atómicos, mensajería clara y GPG firmados
  - Uso de submódulos correctamente referenciados
  - Branching coherente: ramas `feature/patrón` y merges limpios
- **Videos y presentación**

  - Cada sprint documentado con claridad
  - Participación completa de todos los miembros
- **Prevención de copias de IA** (- evaluación cualitativa)

  - Criterio estricto: cualquier párrafo con alta probabilidad de contenido genérico o parafraseo riesgoso anula puntos de documentación.
  - En caso de sospecha de IA, se pedirá justificación en vivo.

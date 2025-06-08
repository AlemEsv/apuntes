# Rúbricas importantes

## Commits

1. commits que introducen gran parte del código de golpe, sin historial previo ("Initial commit"), o **commits enormes sin división lógica**.

2. **commit con archivos de distintos módulos** o capas sin un hilo conductor claro (por ejemplo, una mezcla de Terraform, Bash, Python y Markdown).

3. commits repetitivos y genéricos, se busca **documentar bien** el commit.

## Ramas y pull requests

1. funcionalidades directamente en `main` o **caos de ramas** sin merges claros. (`rama_juan`, `ramita`, etc).

2. **Funcionalidades completas** deben estar revisadas y **hacerles un pull requests**.

3. PR con cientos de líneas de una sola vez, sin comentarios en la descripción y sin **comentarios detallados**.

4. **No usar "Merge pull request #X".**

5. Hacer uso de la pestalla de discusiones.

## Consistencia de código

1. No usar algoritmos excesivamente complejos.

2. Dar un formato único en todo el código.

3. No copiar código al 100% de internet.

## Documentación

1. No comentar obviedades ni colocar comentarios cortos.

2. Uso de docstrings (`"""DOC"""`).

3. No copiar documentación de tutoriales o IA.

## Restricciones

1. No usar librerias que importen funciones relacionadas a la nube.

2. Corregir código extraño por bloques y no de golpe cientos de lineas.

## Linters, hooks y formateo

1. No permite código que no haya sido formateado sin commits intermedios.

2. hooks sin ejecución.

3. No hacer un commit gigante con formateo a todo el proyecto.

## Pruebas

1. No tener Tests triviales, marcados con @pytest.skip o que no fallan aunque el código esté roto.

## Scripts bash y herramientas auxiliares

1. Scripts muy complejos y sin comentarios.

2. Scripts autogenerados por IA.

## QUÉ SÍ HACER

1. Uso consistente e incremental de linters** (`flake8`, `shellcheck`, `tflint`) durante el desarrollo

2. Hooks Git funcionales** (`pre-commit`, `pre-push`, `commit-msg`) que realmente validen reglas y fallen en caso de incumplimiento.

3. Código formateado progresivamente, con commits que muestren correcciones paso a paso.

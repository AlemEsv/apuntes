# Reglas generales para los commits

1. **Atómicos y coherentes**: Cada commit debe agrupar cambios relacionados.
2. **Tamaño moderado**: Idealmente, ningún commit debería superar las 200-300 líneas de cambio (sumando adiciones y eliminaciones).
3. **Mensajes descriptivos**: Usar un formato claro.

   ```yaml
   feat(tf-module): agregar variables iniciales en network-module
   fix(hooks): corregir validación de commit-msg para pattern "feat[#n]"
   docs(readme): añadir sección de "Ejemplo de uso" para módulo compute
   test(py): añadir pruebas parametrizadas de pytest para función XYZ
   ```

4. **Commits frecuentes**: No esperar a "tener todo listo" para subir 1.000 líneas de golpe. Mejor dividir en pequeños pasos y pushear cada avance significativo.

## Esquema recomendado por sprint

### Sprint 1

Se recomienda entre **5 y 7 commits**. Por ejemplo:

1. **Commit 1** (estructura inicial):

   * Crear repositorio y carpeta raíz.
   * Añadir directorios base (`src/`, `tests/`, `docs/`, etc.).
   * Archivos vacíos con esqueleto.

2. **Commit 2** (configuración Git hooks):

   * Agregar `pre-commit` y `commit-msg` en `.git/hooks/` con validación básica.
   * Documentar en `README.md` cómo funcionan los hooks.

3. **Commit 3** (Módulo Terraform mínimo):

   * Implementar un `network-module/main.tf` con un `null_resource`.

4. **Commit 4** (Script de validación básica):

   * Escribir `scripts/validate.sh` para correr `terraform fmt -check` y `terraform validate`.
   * Ajustar mensaje de commit según patrón de la rúbrica (ej. `feat(tf): validar formato y sintaxis`).

5. **Commit 5** (Python para diagramas o reporting mínimo):

   * Agregar `src/generar_diagrama.py` con función vacía o "print(‘función de parseo pendiente’)".
   * Crear archivos de configuración inicial (`.gitignore`, `.flake8`, `.bandit`).

6. **Commit 6** (Primeras pruebas Pytest básicas):

   * Agregar en `tests/test_basic.py` dos pruebas triviales de ejemplo.
   * Configurar `pytest.ini` o similar para cobertura mínima.

7. **Commit 7** (Documentación y vídeo de Sprint 1):

   * Completar `README.md` con instrucciones de instalación.
   * Subir enlace (o anotación) del video de 10 min mostrando todo lo anterior.

Si alguno de esos pasos reúne demasiado código (por ejemplo, un módulo Terraform **y** el script Python completo), conviene dividirlo en dos commits distintos: "feat(tf): crear módulo network con null_resource" y "feat(py): implementar función parseo de tfstate".

### Sprint 2

Se recomiendan entre **7 y 10 commits**, desglosados así:

1. **Commit 1 (feature)**:

   * Añadir segundo módulo Terraform (por ejemplo, `compute-module/` con su propio `main.tf`, `variables.tf` y `validate_compute.sh`).

2. **Commit 2 (feat/scripts)**:

   * Crear o mejorar `scripts/deploy_all.sh` que itere sobre todos los módulos en `iac/` y ejecute `terraform init && terraform apply`.

3. **Commit 3 (feat/validation)**:

   * Implementar `src/verificar_estado.py` que lea `tfstate` y genere un JSON/report mínimo con resultados.

4. **Commit 4 (test/iac_tests)**:

   * En `iac_tests/`, añadir `test_network.py` y `test_compute.py` que validen outputs de Terraform.
   * Configurar las fixtures necesarias en `conftest.py`.

5. **Commit 5 (docs/intermediate)**:

   * Actualizar `docs/<módulo>.md` con contenido original (mínimo 100 palabras) para cada módulo.
   * Incluir gráficos DOT simples generados por `generar_diagrama.py`.

6. **Commit 6 (feat/hooks mejorados)**:

   * Ajustar `.git/hooks/pre-push` para que invoque `verificar_estado.py` y bloquee push si alguna comprobación falla.

7. **Commit 7 (test/python_tests)**:

   * Agregar al menos 2 pruebas parametrizadas en `tests/test_python_logic.py` (por ejemplo, Hypothesis o `@pytest.mark.parametrize`).

8. **Commit 8 (refactor)**:

   * Refactorizar código Bash para corregir errores detectados (por ejemplo, manejo de fallos, validación de parámetros).

9. **Commit 9 (docs/actualización sprint)**:

   * Completar `README.md` con instrucciones extendidas para Carpeteta `iac/`, `scripts/`, `tests/`.
   * Añadir ejemplo de salida de `verificar_estado.py` en Markdown.

10. **Commit 10 (video y cierre Sprint 2)**:

    * Incluir enlace o comentario al video de 10 min explicando lo implementado en Sprint 2.

Si la adición de un módulo nuevo implica más de 200 líneas de Terraform y Bash, conviene separar en:

* "feat(tf): agregar compute-module con variables e outputs"
* "feat(sh): script validate_compute.sh para compute-module"

### Sprint 3

Este sprint suele incluir funcionalidades avanzadas (rollback, drift, dashboard HTML, generación de badges, etc.). Se recomienda entre **7 y 10 commits** igualmente:

1. **Commit 1 (feat/rollback)**:

   * Implementar `scripts/rollback.sh` que restaure estado a partir de un tag Git.

2. **Commit 2 (feat/drift)**:

   * Crear `scripts/simular_drift.sh` para modificar un recurso y detectar drift.
   * Adaptar `src/generar_diagrama.py` para marcar recursos con drift en el grafo.

3. **Commit 3 (feat/dashboard)**:

   * Implementar `scripts/generate_dashboard.py` o similar para leer JSON de tests y generar un HTML o gráfico SVG.

4. **Commit 4 (test/drift_tests)**:

   * Añadir pruebas en `tests/test_drift.py` que simulen un cambio y verifiquen que drift sea detectado correctamente.

5. **Commit 5 (docs/final)**:

   * Completar toda la documentación en `docs/`, incluyendo ejemplos de uso de rollback y drift.
   * Incluir diagramas finales en `docs/diagrama_red.svg`.

6. **Commit 6 (ci/correcciones)**:

   * Ajustar scripts `ci.sh` o workflow YAML para incluir las nuevas etapas (drift, rollback, dashboard).

7. **Commit 7 (refactor/general)**:

   * Unificar estilo de código en Python (PEP8) y Bash (`shellcheck`).
   * Corregir cualquier warning de linters.

8. **Commit 8 (test/final)**:

   * Añadir pruebas finales de cobertura (pytest con `--cov`) y generar badge de cobertura ≥ 85%.

9. **Commit 9 (docs/video)**:

   * Anotar en `README.md` el enlace al video final de presentación de Sprint 3.

10. **Commit 10 (release/version)**:

    * Crear tag semántico final del proyecto (por ejemplo, `v1.0.0-final`).
    * Merge de la rama de release a `main` (si se siguió Git Flow).

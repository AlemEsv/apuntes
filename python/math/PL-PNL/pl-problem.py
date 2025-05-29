from pulp import LpMaximize, LpProblem, LpVariable, LpInteger, LpStatus

def resolver_problema():
    # Crear el modelo de maximización
    model = LpProblem("Maximizar_Z", LpMaximize)

    # Definir variables
    x1 = LpVariable("x1", lowBound=0, cat=LpInteger)
    x2 = LpVariable("x2", lowBound=0, cat=LpInteger)
    # x3, x4

    # Función objetivo: Max Z
    model += 1 * x1 + 2 *x2, "Z"

    # Restricciones
    model += -12 * x1 + 2 >= 2, "R1"
    model += -1 * x1 + 1 * x2 <= 4, "R2"
    model += 3 * x1 + 8 * x2 <= 30, "R3"

    # Resolver el modelo
    status = model.solve()

    # Imprimir resultados
    print(f"\nEstado del modelo: {LpStatus[status]}")

    if LpStatus[status] == 'Optimal':
        print("Solución óptima entera:")
        print(f"x1: {x1.value()}")
        print(f"x2: {x2.value()}")
        print(f"Z: {model.objective.value():,.2f}")
    elif LpStatus[status] == 'Unbounded':
        print("El problema es no acotado (unbounded).")
    elif LpStatus[status] == 'Infeasible':
        print("El problema es infactible (sin solución factible).")
    else:
        print("No se pudo resolver el problema correctamente.")

# Ejecutar
resolver_problema()

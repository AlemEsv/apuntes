# codigo
from scipy.optimize import linprog

# Coeficientes de la funcion objetivo (costos)
# Min Z = 20x + 10y
c = [20, 10]

# Coeficientes de las restricciones (lado izquierdo)
# 2x + y ≥ 6  →  -2x - y ≤ -6
# x + 2y ≥ 6  →  -x - 2y ≤ -6
A = [
    [-2, -1],
    [-1, -2]
]

# Lado derecho de las restricciones
b = [-6, -6]

# Restricciones de no negatividad:
x_bounds = (0, None)  # x ≥ 0
y_bounds = (0, None)  # y ≥ 0

# Resolver con método Simplex big M
res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

# Mostrar resultados
if res.success:
    print("Costo mínimo: $", round(res.fun, 2))
    print(f"Unidades de A (x): {res.x[0]:.2f}")
    print(f"Unidades de B (y): {res.x[1]:.2f}")
else:
    print("No se encontró solución.")

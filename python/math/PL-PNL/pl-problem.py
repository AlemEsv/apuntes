from pulp import LpMaximize, LpProblem, LpVariable, lpSum, LpInteger

# Crear el problema de maximización
model = LpProblem("Maximizar_ganancia_zapatos", LpMaximize)

# Variables: x1 = Botas retro, x2 = Tenis deportivos, x3 = Colegial
x1 = LpVariable("Botas_retro", lowBound=0, cat=LpInteger)
x2 = LpVariable("Tenis_deportivos", lowBound=0, cat=LpInteger)
x3 = LpVariable("Colegial", lowBound=0, cat=LpInteger)

# Función objetivo: maximizar la ganancia
model += 60000 * x1 + 40000 * x2 + 35000 * x3, "Ganancia_total"

# Restricciones de recursos
model += 2 * x1 + 2 * x2 + 2 * x3 <= 1200, "Suelas"
model += 25 * x1 + 60 * x2 <= 12500, "Nailon"
model += 80 * x1 + 15 * x2 + 100 * x3 <= 15000, "Cuero"
model += 220 * x1 + 200 * x2 + 180 * x3 <= 20000, "Cordones"

# Resolver el modelo
model.solve()

# Imprimir resultados
print("Solución óptima entera:")
print(f"Botas retro (x1): {x1.value()}")
print(f"Tenis deportivos (x2): {x2.value()}")
print(f"Colegial (x3): {x3.value()}")
print(f"Ganancia total: ${model.objective.value():,.2f} COP")
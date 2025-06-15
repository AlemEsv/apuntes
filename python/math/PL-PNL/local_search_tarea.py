import random

# Datos del problema
pesos = [4, 3, 5, 2]
valores = [10, 40, 30, 20]
capacidad = 8
n_objetos = len(pesos)

# Función para calcular valor y peso total
def evaluar(sol):
    peso_total = sum(peso * s for peso, s in zip(pesos, sol))
    valor_total = sum(valor * s for valor, s in zip(valores, sol))
    return valor_total if peso_total <= capacidad else -1  # -1 si no es factible

# Generar una solución inicial aleatoria factible
def generar_solucion_inicial():
    while True:
        sol = [random.randint(0, 1) for _ in range(n_objetos)]
        if sum(p * s for p, s in zip(pesos, sol)) <= capacidad:
            return sol

# Generar vecino cambiando un solo bit
def generar_vecino_factible(sol_actual):
    intentos = 0
    max_intentos = 20
    while intentos < max_intentos:
        vecino = sol_actual[:]
        i = random.randint(0, n_objetos - 1)
        vecino[i] = 1 - vecino[i]  # Flip
        peso_total = sum(p * s for p, s in zip(pesos, vecino))
        if peso_total <= capacidad:
            return vecino
        intentos += 1
    return sol_actual  # Si no se encuentra la sol factible, retorna el valor actual

# Búsqueda local
def busqueda_local(max_iter=10):
    x0 = generar_solucion_inicial()
    print(f"Solución inicial: {x0}, valor = {evaluar(x0)}")

    for iteracion in range(1, max_iter + 1):
        xv = generar_vecino_factible(x0)
        if evaluar(xv) > evaluar(x0):
            x0 = xv
            print(f"Iteración {iteracion}:\nmejora: {x0},\nvalor = {evaluar(x0)}\n")
        else:
            print(f"Iteración {iteracion}:\nsin mejora: {x0},\nvalor = {evaluar(x0)}\n")

    return x0, evaluar(x0)

# Ejecutar
mejor_sol, mejor_valor = busqueda_local()
print(f"\nMejor solución encontrada: {mejor_sol}, valor = {mejor_valor}")
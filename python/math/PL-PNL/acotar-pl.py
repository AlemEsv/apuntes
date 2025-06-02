from scipy.optimize import linprog

# Funciones auxiliares
def obtener_lista_flotantes(mensaje):
    return list(map(float, input(mensaje).split()))

def formatear_expresion(coeficientes, variables):
    terminos = []
    for i, coef in enumerate(coeficientes):
        if coef == 0:
            continue
        signo = "+ " if coef > 0 and i > 0 else ""
        terminos.append(f"{signo}{coef}x{i+1}")
    return " ".join(terminos) if terminos else "0"

# Entrada de datos
def leer_funcion_objetivo():
    cantidad = int(input("Cuántas variables tiene la función objetivo? "))
    coef = obtener_lista_flotantes(f"Ingrese los coeficientes de la función objetivo Z (ej. 5 4 ...):\nZ = ")
    return cantidad, coef

def leer_restricciones(cantidad_variables):
    cantidad = int(input("\n¿Cuántas restricciones tiene el problema? "))
    A = []
    b = []
    signos = []
    texto_restricciones = []

    print("\nIngrese las restricciones una por una:")
    for i in range(cantidad):
        coeficientes = obtener_lista_flotantes(f"* Restricción {i+1} - coeficientes (ej. 1 -8 5 ...): ")

        print("    Tipo de restricción:")
        print("      1: <= (menor o igual)\n      2: >= (mayor o igual)")
        tipo = int(input("Ingrese el número correspondiente al tipo: "))
        if tipo not in [1, 2]:
            print("Tipo inválido. Usa solo 1 o 2")
            exit()

        bi = float(input("    resultado (b): "))
        simbolo = {1: "<=", 2: ">="}[tipo]
        expresion = formatear_expresion(coeficientes, cantidad_variables)
        texto_restricciones.append((expresion, simbolo, bi))

        if tipo == 1:  # <=
            A.append(coeficientes)
            b.append(bi)
            signos.append("<=")
        else:  # >=
            A.append([-a for a in coeficientes])
            b.append(-bi)
            signos.append("<=")

    return cantidad, A, b, signos, texto_restricciones

# Imprimir modelo
def mostrar_modelo(coef_objetivo, A, b, cantidad_variables):
    print("\nModelo:")
    print("Max:")
    print("  Z =", formatear_expresion(coef_objetivo, cantidad_variables))
    print("s.a.")
    for i in range(len(A)):
        print(f"  {formatear_expresion(A[i], cantidad_variables)} <= {b[i]}")

# Resolución y resultado
def resolver_simplex(coef_objetivo, A, b, cantidad_variables):
    # para minimización
    coef_min = [-ci for ci in coef_objetivo]  
    limites = [(0, None) for _ in range(cantidad_variables)]
    resultado = linprog(coef_min, A_ub=A, b_ub=b, bounds=limites, method='highs')
    return resultado

def mostrar_resultado(resultado):
    print("\nResultado:")

    # SE ENCONTRÓ SOLUCIÓN OPTIMA
    if resultado.status == 0:
        print("Solución óptima encontrada:")
        for i, val in enumerate(resultado.x):
            print(f"  x{i+1} = {val:.2f}")
        print(f"Valor óptimo de Z = {-resultado.fun:.2f}")

    # NO HAY SOLUCIÓN 1
    elif resultado.status == 2:
        print("El problema es inviable (no hay soluciones posibles que cumplan todas las restricciones)")

    # NO ES ACOTADO
    elif resultado.status == 3:
        print("El problema es no acotado (Z puede crecer infinitamente)")

    else:
        print("Error desconocido.")

# Función principal
def main():
    print("Maximización con método Simplex")
    print("---------------------------------------------\n")

    cantidad_variables, coef_objetivo = leer_funcion_objetivo()
    cantidad_restricciones, A, b, signos, texto_restricciones = leer_restricciones(cantidad_variables)

    mostrar_modelo(coef_objetivo, A, b, cantidad_variables)

    resultado = resolver_simplex(coef_objetivo, A, b, cantidad_variables)
    mostrar_resultado(resultado)

# Ejecutar programa
if __name__ == "__main__":
    main()

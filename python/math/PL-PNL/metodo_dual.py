from scipy.optimize import linprog
import numpy as np

def obtener_lista_flotantes(mensaje):
    while True:
        try:
            valores = list(map(float, input(mensaje).split()))
            return valores
        except ValueError:
            print("Error: Ingrese valores numéricos separados por espacios. Intente nuevamente.")

def formatear_expresion(coeficientes, variables):
    terminos = []
    for i, coef in enumerate(coeficientes):
        if coef == 0:
            continue
        signo = "+ " if coef > 0 and i > 0 else ""
        terminos.append(f"{signo}{coef}x{i+1}")
    return " ".join(terminos) if terminos else "0"

def leer_funcion_objetivo():
    print("\n--- Función Objetivo ---")
    cantidad = int(input("¿Cuántas variables tiene la función objetivo? "))
    coef = obtener_lista_flotantes(f"Ingrese los coeficientes de la función objetivo (ej. 3 8 para 3x₁ + 8x₂):\nZ = ")
    
    print("\n¿Qué tipo de optimización es?")
    print("1: Minimización\n2: Maximización")
    tipo_opt = int(input("Seleccione 1 o 2: "))
    if tipo_opt not in [1, 2]:
        print("Tipo inválido. Usando minimización por defecto.")
        tipo_opt = 1
    
    return cantidad, coef, tipo_opt

def leer_restricciones(cantidad_variables):
    print("\n--- Restricciones ---")
    cantidad = int(input("¿Cuántas restricciones tiene el problema? "))
    A = []
    b = []
    texto_restricciones = []
    tipos_restricciones = []

    print("\nIngrese las restricciones una por una:")
    for i in range(cantidad):
        print(f"\n* Restricción {i+1}:")
        coeficientes = obtener_lista_flotantes("  Coeficientes (ej. 1 4 para x₁ + 4x₂): ")
        
        if len(coeficientes) != cantidad_variables:
            print(f"Error: Debe ingresar exactamente {cantidad_variables} coeficientes.")
            exit()

        print("\n  Tipo de restricción:")
        print("  1: <= (menor o igual)\n  2: >= (mayor o igual)\n  3: = (igualdad)")
        tipo = int(input("  Seleccione el tipo (1/2/3): "))
        if tipo not in [1, 2, 3]:
            print("Tipo inválido. Usando <= por defecto.")
            tipo = 1

        bi = float(input("  Término independiente (b): "))
        simbolo = {1: "<=", 2: ">=", 3: "="}[tipo]
        expresion = formatear_expresion(coeficientes, cantidad_variables)
        texto_restricciones.append((expresion, simbolo, bi))
        tipos_restricciones.append(tipo)
        
        A.append(coeficientes)
        b.append(bi)

    return cantidad, A, b, texto_restricciones, tipos_restricciones

def mostrar_modelo(coef_objetivo, texto_restricciones, cantidad_variables, tipo_opt):
    print("\n--- Modelo ---")
    print("Minimizar:" if tipo_opt == 1 else "Maximizar:")
    print(f"  Z = {formatear_expresion(coef_objetivo, cantidad_variables)}")
    print("Sujeto a:")
    for expr, simbolo, bi in texto_restricciones:
        print(f"  {expr} {simbolo} {bi}")
    print("Condiciones de no negatividad:")
    print("  " + ", ".join(f"x{i+1} ≥ 0" for i in range(cantidad_variables)))

def resolver_simplex_dual(coef_objetivo, A, b, tipos_restricciones, tipo_opt):
    # Construir matrices para el solver
    A_ub = []
    b_ub = []
    A_eq = []
    b_eq = []
    
    for i, tipo in enumerate(tipos_restricciones):
        if tipo == 1:  # <=
            A_ub.append(A[i])
            b_ub.append(b[i])
        elif tipo == 2:  # >=
            A_ub.append([-x for x in A[i]])
            b_ub.append(-b[i])
        else:  # = (igualdad)
            A_eq.append(A[i])
            b_eq.append(b[i])
    
    # Convertir a arrays numpy
    A_ub = np.array(A_ub) if A_ub else None
    b_ub = np.array(b_ub) if b_ub else None
    A_eq = np.array(A_eq) if A_eq else None
    b_eq = np.array(b_eq) if b_eq else None
    
    # Configurar función objetivo
    coef_obj = np.array(coef_objetivo) if tipo_opt == 1 else np.array([-x for x in coef_objetivo])
    
    # Límites de variables (no negatividad)
    bounds = [(0, None) for _ in range(len(coef_objetivo))]
    
    # Resolver con simplex dual
    resultado = linprog(c=coef_obj, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, 
                       bounds=bounds, method='highs-ds')
    return resultado

def mostrar_resultado(resultado, metodo, tipo_opt):
    print(f"\n--- Resultados usando método {metodo} ---")

    if resultado.status == 0:
        print("Solución óptima encontrada:")
        for i, val in enumerate(resultado.x):
            print(f"  x{i+1} = {val:.6f}")
        print(f"Valor óptimo de Z = {resultado.fun if tipo_opt == 1 else -resultado.fun:.6f}")
    elif resultado.status == 2:
        print("El problema es inviable (no hay soluciones posibles)")
    elif resultado.status == 3:
        print("El problema es no acotado (Z puede crecer/decrecer infinitamente)")
    else:
        print("Error desconocido o el método no pudo converger.")

def main():
    print("Método: Simplex Dual")
    
    cantidad_variables, coef_objetivo, tipo_opt = leer_funcion_objetivo()
    cantidad_restricciones, A, b, texto_restricciones, tipos_restricciones = leer_restricciones(cantidad_variables)

    mostrar_modelo(coef_objetivo, texto_restricciones, cantidad_variables, tipo_opt)

    resultado = resolver_simplex_dual(coef_objetivo, A, b, tipos_restricciones, tipo_opt)
    mostrar_resultado(resultado, "Simplex Dual", tipo_opt)

if __name__ == "__main__":
    main()
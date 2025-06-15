import numpy as np

class DietProblemSolver:
    def __init__(self, nutritional_requirements, food_data, M=1e6):
        """
        nutritional_requirements: Lista de requerimientos mínimos [proteínas, calorías, ...]
        food_data: Lista de tuplas (nombre, costo, [nutrientes_por_kg...])
        """
        self.M = M
        self.food_names = [food[0] for food in food_data]
        self.costs = np.array([food[1] for food in food_data])
        self.nutritional_values = np.array([food[2] for food in food_data]).T
        self.requirements = np.array(nutritional_requirements)
        
    def solve(self):
        """Resuelve el problema de dieta usando Simplex Big-M"""
        # Paso 1: Construir tabla inicial
        m, n = len(self.requirements), len(self.food_names)
        tableau = self._build_initial_tableau()
        
        # Paso 2: Eliminar términos M de la función objetivo
        self._eliminate_M_terms(tableau)
        
        # Fase simplex
        while True:
            # Paso 3: Seleccionar columna pivote (variable entrante)
            entering_col = self._select_entering_variable(tableau)
            if entering_col is None:  # Solución óptima
                break
                
            # Paso 4: Seleccionar fila pivote (variable saliente)
            leaving_row = self._select_leaving_variable(tableau, entering_col)
            if leaving_row is None:  # Problema no acotado
                raise Exception("El problema es no acotado")
                
            # Paso 5: Operación de pivote
            self._pivot(tableau, leaving_row, entering_col)
        
        # Verificar factibilidad
        if self._has_artificial_in_basis(tableau):
            raise Exception("El problema no tiene solución factible")
            
        return self._extract_solution(tableau)
    
    def _build_initial_tableau(self):
        """Construye la tabla inicial del simplex Big-M"""
        m, n = len(self.requirements), len(self.food_names)
        
        # Matriz de coeficientes con variables de holgura y artificiales
        slack_vars = -np.eye(m)  # Variables de holgura para >=
        artificial_vars = np.eye(m)  # Variables artificiales
        
        A = np.hstack([self.nutritional_values, slack_vars, artificial_vars])
        
        # Función objetivo extendida (incluyendo M para variables artificiales)
        c_ext = np.hstack([self.costs, np.zeros(m), self.M * np.ones(m)])
        
        # Tabla simplex completa
        tableau = np.vstack([
            np.hstack([A, self.requirements.reshape(-1, 1)]),
            np.hstack([c_ext, 0])
        ])
        
        return tableau
    
    def _eliminate_M_terms(self, tableau):
        """Elimina los términos M de la función objetivo"""
        m = len(self.requirements)
        n = len(self.food_names)
        
        # Identificar filas de variables artificiales (después de variables de decisión y holgura)
        artificial_rows = range(n + m, n + 2*m)
        
        # Restar M * fila de cada variable artificial de la función objetivo
        for i in range(m):
            tableau[-1, :] -= self.M * tableau[i, :]
    
    def _select_entering_variable(self, tableau):
        """Selecciona la variable entrante (columna pivote)"""
        last_row = tableau[-1, :-1]  # Excluir el valor Z
        entering_col = np.argmin(last_row)
        return entering_col if last_row[entering_col] < -1e-8 else None
    
    def _select_leaving_variable(self, tableau, entering_col):
        """Selecciona la variable saliente (fila pivote)"""
        ratios = []
        m = len(self.requirements)
        
        for i in range(m):
            if tableau[i, entering_col] > 1e-8:  # Evitar división por cero
                ratio = tableau[i, -1] / tableau[i, entering_col]
                ratios.append((i, ratio))
        
        if not ratios:
            return None  # Problema no acotado
            
        leaving_row = min(ratios, key=lambda x: x[1])[0]
        return leaving_row
    
    def _pivot(self, tableau, leaving_row, entering_col):
        """Realiza la operación de pivote"""
        # Normalizar fila pivote
        pivot_val = tableau[leaving_row, entering_col]
        tableau[leaving_row, :] /= pivot_val
        
        # Actualizar otras filas
        for i in range(len(tableau)):
            if i != leaving_row and abs(tableau[i, entering_col]) > 1e-8:
                multiplier = tableau[i, entering_col]
                tableau[i, :] -= multiplier * tableau[leaving_row, :]
    
    def _has_artificial_in_basis(self, tableau):
        """Verifica si hay variables artificiales en la base"""
        m = len(self.requirements)
        n = len(self.food_names)
        
        # Las variables artificiales están en las columnas [n+m : n+2m]
        artificial_cols = range(n + m, n + 2*m)
        
        # Verificar si alguna variable artificial es básica (tiene 1 en su columna)
        for col in artificial_cols:
            if any(abs(tableau[i, col] - 1) < 1e-8 and abs(tableau[i, -1]) > 1e-8 for i in range(m)):
                return True
        return False
    
    def _extract_solution(self, tableau):
        """Extrae la solución óptima de la tabla final"""
        m = len(self.requirements)
        n = len(self.food_names)
        solution = np.zeros(n)
        
        for i in range(m):
            for j in range(n):
                if abs(tableau[i, j] - 1) < 1e-8 and all(abs(tableau[k, j]) < 1e-8 for k in range(m) if k != i):
                    solution[j] = tableau[i, -1]
                    break
        
        total_cost = -tableau[-1, -1]  # El valor Z está negado en la tabla
        
        return {
            'foods': {self.food_names[i]: solution[i] for i in range(n)},
            'total_cost': total_cost,
            'nutrients': (self.nutritional_values @ solution).tolist()
        }


# Ejemplo de uso: Problema de la dieta con arroz y frijoles
if __name__ == "__main__":
    # Datos del problema
    nutritional_requirements = [10, 15]  # [proteínas, calorías]
    food_data = [
        ("Arroz", 2, [1, 2]),    # $2/kg, 1 proteína/kg, 2 calorías/kg
        ("Frijoles", 3, [2, 1])  # $3/kg, 2 proteínas/kg, 1 caloría/kg
    ]
    
    # Resolver el problema
    solver = DietProblemSolver(nutritional_requirements, food_data)
    solution = solver.solve()
    
    # Mostrar resultados
    print("Solución óptima:")
    for food, amount in solution['foods'].items():
        print(f"{food}: {amount:.2f} kg")
    
    print(f"\nCosto total: ${solution['total_cost']:.2f}")
    print(f"\nNutrientes obtenidos:")
    print(f"Proteínas: {solution['nutrients'][0]:.2f} unidades")
    print(f"Calorías: {solution['nutrients'][1]:.2f} unidades")
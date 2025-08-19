import numpy as np
import matplotlib.pyplot as plt

# minimizar
def rastrigin(X):
    A = 10
    return A * len(X) + sum([(x ** 2 - A * np.cos(2 * np.pi * x)) for x in X])

def artificial_bee_colony_rastrigin(n_iter=100, n_bees=30, dim=2, bound=(-5.12, 5.12)):
    bees = np.random.uniform(bound[0], bound[1], (n_bees, dim))
    best_bee = bees[0]
    best_fitness = rastrigin(best_bee)
    
    best_fitnesses = []
    
    for iteration in range(n_iter):
        # Fase de abejas empleadas
        for i in range(n_bees):
            # Genera una nueva solucion candidata
            new_bee = bees[i] + np.random.uniform(-1, 1, dim)
            new_bee = np.clip(new_bee, bound[0], bound[1]) # mantiene limites
            
            # Evalua la aptitud (fitness) de la nueva solucion
            new_fitness = rastrigin(new_bee)
            if new_fitness < rastrigin(bees[i]):
                bees[i] = new_bee  # Actualiza
        
        # Fase de abejas observadoras
        fitnesses = np.array([rastrigin(bee) for bee in bees])
        probabilities = 1 / (1 + fitnesses)  # Mejor fitness → mayor probabilidad
        probabilities /= probabilities.sum()  # Normaliza las probabilidades
        
        for i in range(n_bees):
            if np.random.rand() < probabilities[i]:
                selected_bee = bees[i]
                # Genera una nueva solucion
                new_bee = selected_bee + np.random.uniform(-0.5, 0.5, dim)
                new_bee = np.clip(new_bee, bound[0], bound[1])
                if rastrigin(new_bee) < rastrigin(selected_bee):
                    bees[i] = new_bee
        
        # Fase de exploracion
        if np.random.rand() < 0.1:  # 10% de probabilidad de reinicializar una abeja
            scout_index = np.random.randint(n_bees)
            bees[scout_index] = np.random.uniform(bound[0], bound[1], dim)
        
        # Guarda la mejor solucion encontrada hasta el momento
        current_best_bee = bees[np.argmin(fitnesses)]
        current_best_fitness = min(fitnesses)
        
        if current_best_fitness < best_fitness:
            best_fitness = current_best_fitness
            best_bee = current_best_bee
        
        best_fitnesses.append(best_fitness)
    
    return best_bee, best_fitness, best_fitnesses

# Aplicar el algoritmo ABC
best_solution, best_fitness, best_fitnesses = artificial_bee_colony_rastrigin()

# Mostrar los resultados
print("Mejor solución (x, y):", best_solution)
print("Mejor aptitud (valor mínimo):", best_fitness)

# Graficar el rendimiento del algoritmo a lo largo de las iteraciones
plt.figure()
plt.plot(best_fitnesses)
plt.title('Rendimiento del ABC en la optimización de Rastrigin')
plt.xlabel('Iteraciones')
plt.ylabel('Mejor aptitud (más bajo es mejor)')
plt.grid(True)
plt.show()

# Graficar la superficie de la función Rastrigin
x = np.linspace(-5.12, 5.12, 200)
y = np.linspace(-5.12, 5.12, 200)
X, Y = np.meshgrid(x, y)
Z = 10 * 2 + (X ** 2 - 10 * np.cos(2 * np.pi * X)) + (Y ** 2 - 10 * np.cos(2 * np.pi * Y))

plt.figure(figsize=(8, 6))
plt.contourf(X, Y, Z, levels=50, cmap='viridis')
plt.colorbar(label='Valor de la función')
plt.scatter(best_solution[0], best_solution[1], c='red', label='Mejor solución')
plt.title('Optimización de la función Rastrigin con ABC')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.show()
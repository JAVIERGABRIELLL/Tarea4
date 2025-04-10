import numpy as np

# Generación de datos aleatorios para los puntajes de amor entre 0 y 100
generator = np.random.default_rng(1010)
puntajes = np.round(generator.uniform(low=0, high=100, size=10))

# Crear una matriz 2D con la diferencia absoluta entre los puntajes de amor
diferencias = np.abs(puntajes[:, None] - puntajes)
print("Matriz de diferencias absolutas:")
print(diferencias)

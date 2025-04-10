import numpy as np

# Generar un arreglo 1-D con puntuaciones aleatorias
generator = np.random.default_rng(1010)
calificaciones = np.round(generator.uniform(low=0, high=100, size=10))

# Reemplazar los tres primeros valores menores a 60 con cero
contador = 0
for i in range(len(calificaciones)):
    if calificaciones[i] < 60 and contador < 3:
        calificaciones[i] = 0
        contador += 1

print("Arreglo después de reemplazar los tres primeros menores a 60 por cero:")
print(calificaciones)

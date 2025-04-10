import numpy as np

# Coordenadas de los peces
locs = np.array([
    [0, 0, 0],
    [1, 1, 2],
    [0, 0, 0],
    [2, 1, 3],
    [5, 5, 4],
    [5, 0, 0],
    [5, 0, 0],
    [0, 0, 0],
    [2, 1, 3],
    [1, 3, 1]
])

# Pesos de los peces
generator = np.random.default_rng(1010)
weights = generator.normal(size=10)

# Matriz 5x5x5 para los lugares de los peces
acuarios = np.zeros((5, 5, 5))

# Filtrar coordenadas fuera de los límites
locs_validas = [loc for loc in locs if all(0 <= coord < 5 for coord in loc)]

# Colocar los peces en las posiciones válidas
for i, loc in enumerate(locs_validas):
    acuarios[tuple(loc)] = weights[i]

# Determinar los peces que sobreviven
peces_vivos = []
for i, loc in enumerate(locs_validas):
    if np.sum(acuarios[tuple(loc)] == weights[i]) == 1:
        peces_vivos.append(i)

print("Peces que sobreviven:", peces_vivos)


import json
import random
from generate_problem import generate_random_tree
from recursive_dp_solver import count_valid_splits as solver


min_vertices = 3  # Número mínimo de vértices
max_vertices = 1000  # Número máximo de vértices
examples_per_size = 2  # Número de ejemplos por tamaño de árbol

results = []  

for n in range(min_vertices, max_vertices + 1):
    for _ in range(examples_per_size):
        black_count = random.randint(1, n)  # Al menos un vértice negro
        edges, black_vertices = generate_random_tree(n, black_count)
        
        # Obtener el resultado usando el enfoque de fuerza bruta
        (valid_splits, time) = solver(n, edges, black_vertices)

        # Almacenar la configuración y el resultado
        results.append({
            "vertices": n,
            "edges": edges,
            "black_vertices": list(black_vertices),
            "solution": valid_splits,
            "time": time
        })

with open("tree_examples.json", "w") as f:
    json.dump(results, f, indent=4)

print(f"Se generaron y guardaron ejemplos en 'test_recursive.json'.")
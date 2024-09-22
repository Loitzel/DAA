
import json
import random
from divide_and_conquer import solve_a_good_string as solver


max_amount_of_characters = 1000  # Número máximo de vértices
examples_per_size = 2  # Número de ejemplos por tamaño de árbol

results = []  

for n in range(1, max_amount_of_characters + 1):
    for _ in range(examples_per_size):
        random_string = "".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=n))
        solution, time = solver(random_string)
        
        # Almacenar la configuración y el resultado
        results.append({
            "string": random_string,
            "solution": solution,
            "time": time
        })

with open("tree_examples.json", "w") as f:
    json.dump(results, f, indent=4)

print(f"Se generaron y guardaron ejemplos en 'test_recursive.json'.")
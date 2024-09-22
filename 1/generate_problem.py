import random

def generate_random_tree(n, black_count):
    if black_count > n:
        raise ValueError("La cantidad de vértices negros no puede exceder la cantidad de vértices totales.")

    p = [random.randint(0, i) for i in range(n-1)]
    edges = [(i+1, p[i]) for i in range(n-1)]  

    colors = [0] * n
    
    black_vertices = random.sample(range(n), black_count)
    for v in black_vertices:
        colors[v] = 1
    
    black_set = {v for v in black_vertices} 
    return edges, black_set

# Ejemplo de uso
n = 5  # Número de vértices
black_count = 2  # Número de vértices negros

edges, black_vertices = generate_random_tree(n, black_count)
print(f"Aristas del árbol: {edges}")
print(f"Vértices negros: {black_vertices}")
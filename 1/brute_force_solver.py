from itertools import combinations
from collections import defaultdict
from timing import timing

def dfs(node, adj_list, visited, component):
    visited[node] = True
    component.append(node)
    for neighbor in adj_list[node]:
        if not visited[neighbor]:
            dfs(neighbor, adj_list, visited, component)

def count_black_vertices(component, black_vertices):
    return sum(1 for v in component if v in black_vertices)

@timing
def count_valid_splits(n, edges, black_vertices):
    valid_splits = 0

    # Generamos todas las combinaciones posibles de aristas a eliminar (0 <= k < n)
    for k in range(n):
        for edge_comb in combinations(edges, k):  # Eliminar k aristas
            adj_list = defaultdict(list)
            for u, v in edges:
                if (u, v) not in edge_comb and (v, u) not in edge_comb:
                    adj_list[u].append(v)
                    adj_list[v].append(u)

            visited = [False] * n
            components = []
            for node in range(n):
                if not visited[node]:
                    component = []
                    dfs(node, adj_list, visited, component)
                    components.append(component)

            if all(count_black_vertices(component, black_vertices) == 1 for component in components):
                valid_splits += 1

    return valid_splits

# Ejemplo de uso
n = 5  # Número de vértices
edges = [(0, 1), (0, 2), (0, 3), (3, 4)]  # Aristas del árbol
black_vertices = {1, 2, 4}  # Vértices negros

result = count_valid_splits(n, edges, black_vertices)
print(f"El número de particiones válidas es: {result}")

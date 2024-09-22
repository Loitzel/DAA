import time
from timing import timing

class TreeNode:
    def __init__(self, color, index):
        self.color = color  # 0 para blanco, 1 para negro
        self.index = index
        self.children = []
        self.dp_black = 0
        self.dp_white = 0

def count_partitions(root):
    if not root:
        return

    # Caso base: hoja
    if not root.children:
        if root.color == 1:  # Negro
            root.dp_black = 1
            root.dp_white = 0
        else:  # Blanco
            root.dp_black = 0
            root.dp_white = 1
        return

    # Calcular DP para hijos
    for child in root.children:
        count_partitions(child)

    if root.color == 1:  # Nodo negro
        prod_black = 1

        for child in root.children:
            prod_black *= (child.dp_black + child.dp_white)

        root.dp_black = prod_black 
        root.dp_white = 0
    else:  # Nodo blanco
        dp_black = 0
        p_black = 1
        p_white = 1
        for child in root.children:
            for other_child in root.children:
                if other_child != child:
                    p_black *= (other_child.dp_black + other_child.dp_white)
            p_black = p_black * child.dp_black
            dp_black += p_black
            p_black = 1

        for child in root.children:
            p_white *= (child.dp_black + child.dp_white)

        root.dp_white = p_white
        root.dp_black = dp_black

def create_tree(n, edges, black_vertices):
    colors = [0] * n  # Inicializar todos los nodos como blancos
    for vertex in black_vertices:
        colors[vertex] = 1  # Marcar los nodos negros

    nodes = [TreeNode(colors[i], i) for i in range(n)]
    for u, v in edges:
        nodes[v].children.append(nodes[u]) 

    return nodes[0]

@timing
def count_valid_splits(n, edges, black_vertices):
    root = create_tree(n, edges, black_vertices)
    count_partitions(root)
    return root.dp_black

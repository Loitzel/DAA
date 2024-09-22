from collections import deque
from timing import timing

class Node:
    def __init__(self, id):
        self.id = id
        self.edges = {} 

    def add_edge(self, node, capacity):
        self.edges[node] = capacity

class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.in_node = Node(f'in_{row}_{col}')
        self.out_node = Node(f'out_{row}_{col}')
        self.source = Node('source')
        self.sink = Node('sink')
        self.in_node.add_edge(self.out_node, 1)

class Board:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.cells = [[Cell(row, col) for col in range(cols)] for row in range(rows)]
        self.source = Node('source')
        self.sink = Node('sink')
        self.connect_adjacent_cells()
        self.flow_network = {}
        self.node_count = rows * cols * 2 + 2

    def connect_adjacent_cells(self):
        for row in range(self.rows):
            for col in range(self.cols):
                current_cell = self.cells[row][col]
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Arriba, Abajo, Izquierda, Derecha
                    adj_row, adj_col = row + dr, col + dc
                    if 0 <= adj_row < self.rows and 0 <= adj_col < self.cols:
                        adjacent_cell = self.cells[adj_row][adj_col]
                        current_cell.out_node.add_edge(adjacent_cell.in_node, 1)

    def connect_source_sink(self, in_cells, out_cells):
        for cell in in_cells:
            self.source.add_edge(cell.in_node, 1)
        for cell in out_cells:
            cell.out_node.add_edge(self.sink, 1)

    def bfs(self, parent):
        visited = {node: False for node in self.flow_network}
        queue = deque([self.source])
        visited[self.source] = True

        while queue:
            current_node = queue.popleft()

            for adj, capacity in self.flow_network[current_node].items():
                if not visited[adj] and capacity > 0:  # Encontrar arista con capacidad positiva
                    queue.append(adj)
                    visited[adj] = True
                    parent[adj] = current_node

                    if adj == self.sink:  # Si llegamos al sumidero, terminamos la búsqueda
                        return True

        return False

    @timing
    def edmonds_karp(self):
        # Inicializar el grafo de flujo
        self.flow_network = {node: {} for node in self.get_all_nodes()}

        # Rellenar la capacidad de las aristas
        for row in range(self.rows):
            for col in range(self.cols):
                cell = self.cells[row][col]
                for adj, capacity in cell.out_node.edges.items():
                    self.flow_network[cell.out_node][adj] = capacity

                for adj, capacity in cell.in_node.edges.items():
                    self.flow_network[cell.in_node][adj] = capacity

        # También agregar las aristas de la fuente y el sumidero
        for adj, capacity in self.source.edges.items():
            self.flow_network[self.source][adj] = capacity
        for adj, capacity in self.sink.edges.items():
            if adj not in self.flow_network:
                self.flow_network[adj] = {}
            self.flow_network[adj][self.sink] = capacity

        parent = {}
        max_flow = 0

        # Mientras haya un camino aumentante, aplicar la búsqueda en amplitud
        while self.bfs(parent):
            path_flow = float('Inf')
            s = self.sink

            # Encontrar la capacidad mínima en el camino aumentante
            while s != self.source:
                path_flow = min(path_flow, self.flow_network[parent[s]][s])
                s = parent[s]

            # Actualizar las capacidades de las aristas
            v = self.sink
            while v != self.source:
                u = parent[v]
                self.flow_network[u][v] -= path_flow
                if v not in self.flow_network:
                    self.flow_network[v] = {}
                if u not in self.flow_network[v]:
                    self.flow_network[v][u] = 0
                self.flow_network[v][u] += path_flow
                v = parent[v]

            # Sumar al flujo total
            max_flow += path_flow

        return max_flow

    def get_all_nodes(self):
        nodes = set()
        nodes.add(self.source)
        nodes.add(self.sink)
        for row in range(self.rows):
            for col in range(self.cols):
                cell = self.cells[row][col]
                nodes.add(cell.in_node)
                nodes.add(cell.out_node)
        return nodes
    
    def draw_paths(self):
        """
        Dibujar el tablero y marcar las celdas con un camino saturado entre in_node y out_node.
        """
        for row in range(self.rows):
            for col in range(self.cols):
                cell = self.cells[row][col]
                in_node = cell.in_node
                out_node = cell.out_node

                if self.flow_network[in_node][out_node] == 0:  
                    print("X", end=" ")  
                else:
                    print(".", end=" ")  
            print()

board = Board(3, 3)

in_cells = [board.cells[0][0], board.cells[1][1]]  
out_cells = [board.cells[2][2], board.cells[0][2]]  

board.connect_source_sink(in_cells, out_cells)

max_flow = board.edmonds_karp()

print(f"Flujo máximo: {max_flow}")
# Dibujar los caminos saturados en el tablero
board.draw_paths()

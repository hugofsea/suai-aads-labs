class Graph:
    def __init__(self, is_directed: bool = False) -> None:
        self.matrix: list[dict[int, int]] = []
        self.is_directed = is_directed

    def add_vertex(self):
        self.matrix.append(dict())

    def add_edge(self, vertex1: int, vertex2: int, weight: int = 1) -> None:
        self.matrix[vertex1][vertex2] = weight

        if not self.is_directed:
            self.matrix[vertex2][vertex1] = weight

    def remove_vertex(self, vertex_to_remove: int) -> None:
        del self.matrix[vertex_to_remove]

        for vertex1 in self.matrix:
            try:
                vertex1.pop(vertex_to_remove)

                for vertex2 in list(vertex1.keys()):
                    if vertex2 > vertex_to_remove:
                        weight = vertex1.pop(vertex2)
                        vertex1[vertex2 - 1] = weight
            except KeyError:
                ...

    def remove_edge(self, vertex1: int, vertex2: int) -> None:
        del self.matrix[vertex1][vertex2]

        if not self.is_directed:
            del self.matrix[vertex2][vertex1]

    def is_edge(self, vertex1: int, vertex2: int) -> bool:
        if not self.is_directed:
            return self.matrix[vertex1].get(vertex2) is not None or self.matrix[vertex2].get(vertex1) is not None

        return self.matrix[vertex1].get(vertex2) is not None

    def get_adjacent_vertices(self, vertex: int):
        return list(self.matrix[vertex].keys())

    def display(self) -> None:
        print(
            '\n'.join([
                ' '.join([
                    "0"
                    if (weight := row.get(vertex)) is None
                    else str(weight)
                    for vertex, _ in enumerate(self.matrix)
                ])
                for row in self.matrix
            ])
        )

    def floyd_warshall(self):
        dist = [
            [
                float('inf')
                if (weight := row.get(vertex)) is None
                else weight
                for vertex, _ in enumerate(self.matrix)
            ]
            for row in self.matrix
        ]

        for i in range(len(dist)):
            dist[i][i] = 0

        for k, _ in enumerate(self.matrix):
            for i, _ in enumerate(self.matrix):
                for j, _ in enumerate(self.matrix):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        return dist

    def minimum_spanning_tree_prim(self):
        selected = [False] * len(self.matrix)
        edges = []
        selected[0] = True

        while len(edges) < len(self.matrix) - 1:
            min_weight = float('inf')
            min_edge = None
            for vertex1, _ in enumerate(self.matrix):
                if not selected[vertex1]:
                    continue

                for vertex2, _ in enumerate(self.matrix):
                    if not selected[vertex2] and self.matrix[vertex1].get(vertex2) is not None and \
                            self.matrix[vertex1][vertex2] < min_weight:
                        min_weight = self.matrix[vertex1][vertex2]
                        min_edge = (vertex1, vertex2, min_weight)
            if min_edge:
                vertex1, vertex2, weight = min_edge
                edges.append((vertex1, vertex2, weight))
                selected[vertex2] = True

        # Проверка на связность графа
        if len(edges) < len(self.matrix) - 1:
            return None  # Граф несвязный, возвращаем None

        min_spanning_tree = Graph()

        for _ in enumerate(self.matrix):
            min_spanning_tree.add_vertex()

        for edge in edges:
            vertex1, vertex2, weight = edge
            min_spanning_tree.add_edge(vertex1, vertex2, weight)

        return min_spanning_tree

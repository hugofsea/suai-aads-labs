import timeit

from my_collections.graph import Graph

ITERATIONS = 500


def get_benchmark_add_vertex():
    graph = Graph()

    def benchmark_add_vertex():
        graph.add_vertex()

    return benchmark_add_vertex


def get_benchmark_add_edge():
    graph = Graph()

    graph.add_vertex()
    graph.add_vertex()

    def benchmark_add_edge():
        graph.add_edge(0, 1)

    return benchmark_add_edge


def get_benchmark_remove_vertex():
    graph = Graph()

    for i in range(ITERATIONS):
        graph.add_vertex()
        for j in range(i):
            graph.add_edge(j, i)

    def benchmark_remove_vertex():
        graph.remove_vertex(0)

    return benchmark_remove_vertex


def get_benchmark_remove_edge():
    graph = Graph()

    graph.add_vertex()

    for i in range(ITERATIONS):
        graph.add_vertex()
        graph.add_edge(0, i + 1)

    vertexes = [0, 1]

    def benchmark_remove_edge():
        graph.remove_edge(vertexes[0], vertexes[1])

        vertexes[1] += 1

    return benchmark_remove_edge


def get_benchmark_is_edge():
    graph = Graph()

    graph.add_vertex()
    graph.add_vertex()

    graph.add_edge(0, 1)

    def benchmark_is_edge():
        graph.is_edge(0, 1)

    return benchmark_is_edge


def get_benchmark_get_adjacent_vertices():
    graph = Graph()

    for i in range(ITERATIONS):
        graph.add_vertex()

    for i in range(ITERATIONS - 1):
        graph.add_edge(0, i + 1)

    def benchmark_get_adjacent_vertices():
        graph.get_adjacent_vertices(0)

    return benchmark_get_adjacent_vertices


def get_benchmark_floyd_warshall():
    graph = Graph()

    for i in range(50):
        graph.add_vertex()
        for j in range(i):
            graph.add_edge(j, i)

    def benchmark_floyd_warshall():
        graph.floyd_warshall()

    return benchmark_floyd_warshall


def get_benchmark_minimum_spanning_tree_prim():
    graph = Graph()

    for i in range(50):
        graph.add_vertex()
        for j in range(i):
            graph.add_edge(j, i)

    def benchmark_minimum_spanning_tree_prim():
        graph.minimum_spanning_tree_prim()

    return benchmark_minimum_spanning_tree_prim


# Запуск бенчмарков и вывод результатов
if __name__ == "__main__":
    iterations = ITERATIONS
    print("add_vertex():", timeit.timeit(get_benchmark_add_vertex(), number=iterations))
    print("add_edge():", timeit.timeit(get_benchmark_add_edge(), number=iterations))
    print("remove_vertex():", timeit.timeit(get_benchmark_remove_vertex(), number=iterations))
    print("remove_edge():", timeit.timeit(get_benchmark_remove_edge(), number=iterations))
    print("is_edge():", timeit.timeit(get_benchmark_is_edge(), number=iterations))
    print("get_adjacent_vertices():", timeit.timeit(get_benchmark_get_adjacent_vertices(), number=iterations))
    print("floyd_warshall():", timeit.timeit(get_benchmark_floyd_warshall(), number=iterations))
    print("minimum_spanning_tree_prim():", timeit.timeit(get_benchmark_minimum_spanning_tree_prim(), number=iterations))

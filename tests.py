import unittest
from my_collections.graph import Graph


class TestGraph(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()

    def test_add_vertex(self):
        self.graph.add_vertex()
        self.assertEqual(len(self.graph.matrix), 1)

    def test_add_edge(self):
        self.graph.add_vertex()
        self.graph.add_vertex()
        self.graph.add_edge(0, 1, 5)
        self.assertTrue(self.graph.matrix[0].get(1) == 5)
        self.assertTrue(self.graph.matrix[1].get(0) == 5)

    def test_remove_vertex(self):
        self.graph.add_vertex()
        self.graph.add_vertex()
        self.graph.add_edge(0, 1, 5)
        self.graph.remove_vertex(0)
        self.assertEqual(len(self.graph.matrix), 1)
        self.assertEqual(len(self.graph.matrix[0]), 0)

    def test_remove_edge(self):
        self.graph.add_vertex()
        self.graph.add_vertex()
        self.graph.add_edge(0, 1, 5)
        self.graph.remove_edge(0, 1)
        self.assertEqual(len(self.graph.matrix[0]), 0)
        self.assertEqual(len(self.graph.matrix[1]), 0)

    def test_is_edge(self):
        self.graph.add_vertex()
        self.graph.add_vertex()
        self.graph.add_edge(0, 1, 5)
        self.assertTrue(self.graph.is_edge(0, 1))
        self.assertTrue(self.graph.is_edge(1, 0))

    def test_get_adjacent_vertices(self):
        self.graph.add_vertex()
        self.graph.add_vertex()
        self.graph.add_edge(0, 1, 5)
        self.assertEqual(self.graph.get_adjacent_vertices(0), [1])

    def test_floyd_warshall(self):
        self.graph.add_vertex()
        self.graph.add_vertex()
        self.graph.add_vertex()
        self.graph.add_vertex()
        self.graph.add_edge(0, 1, 5)
        self.graph.add_edge(0, 2, 3)
        self.graph.add_edge(1, 2, 2)
        self.graph.add_edge(1, 3, 7)
        self.graph.add_edge(2, 3, 1)

        expected_distances = [
            [0, 5, 3, 4],
            [5, 0, 2, 3],
            [3, 2, 0, 1],
            [4, 3, 1, 0]
        ]
        self.assertEqual(self.graph.floyd_warshall(), expected_distances)

    def test_minimum_spanning_tree_prim(self):
        self.graph.add_vertex()
        self.graph.add_vertex()
        self.graph.add_vertex()
        self.graph.add_vertex()
        self.graph.add_vertex()
        self.graph.add_edge(0, 1, 2)
        self.graph.add_edge(0, 3, 6)
        self.graph.add_edge(1, 2, 3)
        self.graph.add_edge(1, 3, 8)
        self.graph.add_edge(1, 4, 5)
        self.graph.add_edge(2, 4, 7)
        self.graph.add_edge(3, 4, 9)

        # Ожидаемое минимальное остовное дерево
        # Вершина 0 -- Вершина 1, вес: 2
        # Вершина 1 -- Вершина 2, вес: 3
        # Вершина 1 -- Вершина 4, вес: 5
        # Вершина 0 -- Вершина 3, вес: 6
        expected_min_spanning_tree = Graph()
        expected_min_spanning_tree.add_vertex()
        expected_min_spanning_tree.add_vertex()
        expected_min_spanning_tree.add_vertex()
        expected_min_spanning_tree.add_vertex()
        expected_min_spanning_tree.add_vertex()
        expected_min_spanning_tree.add_edge(0, 1, 2)
        expected_min_spanning_tree.add_edge(1, 2, 3)
        expected_min_spanning_tree.add_edge(1, 4, 5)
        expected_min_spanning_tree.add_edge(0, 3, 6)

        self.assertEqual(self.graph.minimum_spanning_tree_prim().matrix, expected_min_spanning_tree.matrix)


if __name__ == "__main__":
    unittest.main()

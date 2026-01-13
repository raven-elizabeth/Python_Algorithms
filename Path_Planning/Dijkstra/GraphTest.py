import unittest
from Graph import Graph

graph_values = {
            "A": {"B": 3, "C": 3},
            "B": {"A": 3, "D": 3.5, "E": 2.8},
            "C": {"A": 3, "E": 2.8, "F": 3.5},
            "D": {"B": 3.5, "E": 3.1, "G": 10},
            "E": {"B": 2.8, "C": 2.8, "D": 3.1, "G": 7},
            "F": {"G": 2.5, "C": 3.5},
            "G": {"F": 2.5, "E": 7, "D": 10},
        }
graph = Graph(graph_values)

class GraphTest(unittest.TestCase):
    def test_find_shortest_distances(self):
        self.assertEqual(
            graph.find_shortest_distances('B'),
            {'A': 3, 'B': 0, 'C': 5.6, 'D': 3.5, 'E': 2.8, 'F': 9.1, 'G': 9.8}
        )

    def test_find_predecessors(self):
        self.assertEqual(
            graph.find_predecessors({'A': 3, 'B': 0, 'C': 5.6, 'D': 3.5, 'E': 2.8, 'F': 9.1, 'G': 9.8}),
            {'A': 'B', 'B': None, 'C': 'E', 'D': 'B', 'E': 'B', 'F': 'C', 'G': 'E'}
        )

    def test_get_shortest_path(self):
        self.assertEqual(
            graph.get_shortest_path(
                "B",
                "F"
            ),
            ['B', 'E', 'C', 'F']
        )


if __name__ == '__main__':
    unittest.main()
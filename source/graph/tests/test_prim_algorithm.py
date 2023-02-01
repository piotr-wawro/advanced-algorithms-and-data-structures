import unittest
from graph.utilities.graph import Graph
from graph.utilities.datamodel import Edge
from graph.algorithms.prim_algorithm import prim_algorithm

class TestKurskalAlgorithm(unittest.TestCase):

    def test_graph_1(self):
        g = Graph()
        g.add_edge('a','b',4)
        g.add_edge('a','e',1)
        g.add_edge('a','f',1)
        g.add_edge('b','c',2)
        g.add_edge('b','e',2)
        g.add_edge('c','d',8)
        g.add_edge('d','e',3)
        g.add_edge('d','f',6)
        g.add_edge('e','f',2)

        edges = prim_algorithm(g)

        self.assertListEqual(
            edges,
            [
                Edge('a','e',1),
                Edge('a','f',1),
                Edge('e','b',2),
                Edge('b','c',2),
                Edge('e','d',3),
            ]
        )

if __name__ == '__main__':
    unittest.main()
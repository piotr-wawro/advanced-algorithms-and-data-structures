import unittest
from graph.utilities.graph import Graph
from graph.utilities.datamodel import Path
from graph.algorithms.dijkstras_algorithm import dijkstras_algorithm

class TestDijkstrasAlgorithm(unittest.TestCase):

    def test_graph_1(self):
        g = Graph(size=5, is_directed=False)
        g.add_edge('a','b',6)
        g.add_edge('a','d',1)
        g.add_edge('b','c',5)
        g.add_edge('b','d',2)
        g.add_edge('b','e',2)
        g.add_edge('d','e',1)
        g.add_edge('e','c',5)

        paths = dijkstras_algorithm(g, 'a')

        self.assertEqual(paths[0], Path(path=['A'], cost=0))
        self.assertEqual(paths[1], Path(path=['A','D','B'], cost=3))
        self.assertEqual(paths[2], Path(path=['A','D','E','C'], cost=7))
        self.assertEqual(paths[3], Path(path=['A','D'], cost=1))
        self.assertEqual(paths[4], Path(path=['A','D','E'], cost=2))

    def test_graph_2(self):
        g = Graph(size=4, is_directed=True)
        g.add_edge('a','b',1)
        g.add_edge('b','c',1)
        g.add_edge('c','d',1)

        paths = dijkstras_algorithm(g, 'a')

        self.assertEqual(paths[0], Path(path=['A'], cost=0))
        self.assertEqual(paths[1], Path(path=['A','B'], cost=1))
        self.assertEqual(paths[2], Path(path=['A','B','C'], cost=2))
        self.assertEqual(paths[3], Path(path=['A','B','C','D'], cost=3))

if __name__ == '__main__':
    unittest.main()
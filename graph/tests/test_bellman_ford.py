import unittest
from graph.utilities.graph import Graph
from graph.utilities.datamodel import Path
from graph.algorithms.bellman_ford import bellman_ford

class TestBellmanFord(unittest.TestCase):

    def test_graph_1(self):
        g = Graph(size=6, is_directed=True)
        g.add_edge('a','b',6)
        g.add_edge('a','c',4)
        g.add_edge('a','d',5)
        g.add_edge('b','e',-1)
        g.add_edge('c','b',-2)
        g.add_edge('c','e',3)
        g.add_edge('d','c',-2)
        g.add_edge('d','f',-1)
        g.add_edge('e','f',3)

        paths = bellman_ford(g, 'a')

        self.assertEqual(paths[0], Path(path=['A'], cost=0))
        self.assertEqual(paths[1], Path(path=['A','D','C','B'], cost=1))
        self.assertEqual(paths[2], Path(path=['A','D','C'], cost=3))
        self.assertEqual(paths[3], Path(path=['A','D'], cost=5))
        self.assertEqual(paths[4], Path(path=['A','D','C','B','E'], cost=0))
        self.assertEqual(paths[5], Path(path=['A','D','C','B','E','F'], cost=3))

    def test_graph_2(self):
        g = Graph(size=6, is_directed=True)
        g.add_edge('a','c',2)
        g.add_edge('b','a',1)
        g.add_edge('c','b',-2)
        g.add_edge('d','a',-4)
        g.add_edge('d','c',-1)
        g.add_edge('e','d',1)
        g.add_edge('f','a',10)
        g.add_edge('f','e',8)

        paths = bellman_ford(g, 'f')

        self.assertEqual(paths[0], Path(path=['F','E','D','A'], cost=5))
        self.assertEqual(paths[1], Path(path=['F','E','D','A','C','B'], cost=5))
        self.assertEqual(paths[2], Path(path=['F','E','D','A','C'], cost=7))
        self.assertEqual(paths[3], Path(path=['F','E','D'], cost=9))
        self.assertEqual(paths[4], Path(path=['F','E'], cost=8))
        self.assertEqual(paths[5], Path(path=['F'], cost=0))

    def test_graph_3(self):
        g = Graph(size=4, is_directed=True)
        g.add_edge('a','b',1)
        g.add_edge('b','c',1)
        g.add_edge('c','d',1)

        paths = bellman_ford(g, 'a')

        self.assertEqual(paths[0], Path(path=['A'], cost=0))
        self.assertEqual(paths[1], Path(path=['A','B'], cost=1))
        self.assertEqual(paths[2], Path(path=['A','B','C'], cost=2))
        self.assertEqual(paths[3], Path(path=['A','B','C','D'], cost=3))

if __name__ == '__main__':
    unittest.main()
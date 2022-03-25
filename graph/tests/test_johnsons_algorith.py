import unittest
from graph.algorithms.bellman_ford import bellman_ford
from graph.utilities.graph import Graph
from graph.utilities.datamodel import Path
from graph.algorithms.johnsons_algorithm import johnsons_algorith

class TestJohnsonsAlgorith(unittest.TestCase):

    def test_graph_1(self):
        g = Graph(is_directed=True)
        g.add_edge('a','b',-2)
        g.add_edge('b','c',-1)
        g.add_edge('c','a',4)
        g.add_edge('c','d',2)
        g.add_edge('c','e',-3)
        g.add_edge('f','d',1)
        g.add_edge('f','e',-4)

        new_g = johnsons_algorith(g)
        self.assertEqual(new_g['a','b'], 0)
        self.assertEqual(new_g['b','c'], 0)
        self.assertEqual(new_g['c','a'], 1)
        self.assertEqual(new_g['c','d'], 0)
        self.assertEqual(new_g['c','e'], 0)
        self.assertEqual(new_g['f','d'], 2)
        self.assertEqual(new_g['f','e'], 2)

        # pcg = johnsons_algorith(g)
        # for i in range(len(g)):
        #     self.assertEqual(pcg[i], bellman_ford(g, i))

if __name__ == '__main__':
    unittest.main()
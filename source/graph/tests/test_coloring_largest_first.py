import unittest
from graph.utilities.graph import Graph
from graph.algorithms.coloring_largest_first import coloring_largest_first

class TestColoringLargestFirst(unittest.TestCase):

    def test_graph_envelope(self):
        g = Graph()
        g.add_edge('a','b',1)
        g.add_edge('a','c',1)
        g.add_edge('a','d',1)
        g.add_edge('b','c',1)
        g.add_edge('b','e',1)
        g.add_edge('b','f',1)
        g.add_edge('b','g',1)
        g.add_edge('c','d',1)
        g.add_edge('c','f',1)
        g.add_edge('d','f',1)
        g.add_edge('e','f',1)
        g.add_edge('f','g',1)

        color_pool = coloring_largest_first(g)

        self.assertSetEqual(color_pool[0], {5, 0})
        self.assertSetEqual(color_pool[1], {1, 3})
        self.assertSetEqual(color_pool[2], {2, 4, 6})


if __name__ == '__main__':
    unittest.main()
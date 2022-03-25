import unittest
from graph.utilities.graph import Graph
from graph.utilities.support import alpha_to_numeric, numeric_to_alpha

class TestGraph(unittest.TestCase):

    def test_validate_vertex_as_string(self):
        Graph()._validate_vertex_as_string('asd')

        with self.assertRaises(ValueError):
            Graph()._validate_vertex_as_string('asd3')

    def test_validate_vertex_as_number(self):
        Graph()._validate_vertex_as_number(123)

        with self.assertRaises(ValueError):
            Graph()._validate_vertex_as_number(-123)

    def test_validate_vertex(self):
        Graph()._validate_vertex(123)
        Graph()._validate_vertex('asd')

        with self.assertRaises(ValueError):
            Graph()._validate_vertex({'asd'})

    def test_numeric_to_alpha(self):
        self.assertEqual(numeric_to_alpha(0), 'A')
        self.assertEqual(numeric_to_alpha(25), 'Z')
        self.assertEqual(numeric_to_alpha(26), 'AA')
        self.assertEqual(numeric_to_alpha(51), 'AZ')
        self.assertEqual(numeric_to_alpha(52), 'BA')
        self.assertEqual(numeric_to_alpha(26*27), 'AAA')

    def test_alpha_to_numeric(self):
        self.assertEqual(alpha_to_numeric('A'), 0)
        self.assertEqual(alpha_to_numeric('Z'), 25)
        self.assertEqual(alpha_to_numeric('AA'), 26)
        self.assertEqual(alpha_to_numeric('AZ'), 51)
        self.assertEqual(alpha_to_numeric('BA'), 52)
        self.assertEqual(alpha_to_numeric('AAA'), 26*27)

    def test_fits_in_graph(self):
        self.assertTrue(Graph(size=5)._fits_in_graph(0))
        self.assertTrue(Graph(size=5)._fits_in_graph(4))

        self.assertFalse(Graph(size=5)._fits_in_graph(5))

    def test_getitem(self):
        g = Graph()
        g.add_edge(0,1,1)

        self.assertEqual(g[0,0], None)
        self.assertEqual(g[0,1], 1)
        self.assertEqual(g[1,0], 1)
        self.assertEqual(g[1,1], None)

        self.assertEqual(g['a','a'], None)
        self.assertEqual(g['a','b'], 1)
        self.assertEqual(g['b','a'], 1)
        self.assertEqual(g['b','b'], None)

        self.assertEqual(g[0], [None, 1])
        self.assertEqual(g[1], [1, None])

        self.assertEqual(g['a'], [None, 1])
        self.assertEqual(g['b'], [1, None])

    def test_len(self):
        g = Graph(size=3)

        self.assertEqual(len(g), 3)

    def test_expand_graph(self):
        matrix = [
            [None,  1,    None, None, None, None],
            [1,     None, 1,    None, None, None],
            [None,  1,    None, None, 10,   None],
            [None,  None, None, None, None, None],
            [None,  None, 10,   None, None, None],
            [None,  None, None, None, None, None],
        ]

        g = Graph()
        g.add_edge(0,1,1)
        g.add_edge(1,2,1)
        g._expand_graph(5)
        g.add_edge(4,2,10)

        self.assertEqual(g.graph, matrix)

    def test_directed_graph(self):
        matrix = [
            [None, 1,    None],
            [None, None, 1,  ],
            [None, None, None],
        ]

        g = Graph(is_directed=True)
        g.add_edge(0,1,1)
        g.add_edge(1,2,1)

        self.assertEqual(g.graph, matrix)

    def test_undirected_graph(self):
        matrix = [
            [None, 1,    None],
            [1,    None, 1,  ],
            [None, 1,    None],
        ]

        g = Graph(is_directed=False)
        g.add_edge(0,1,1)
        g.add_edge(1,2,1)

        self.assertEqual(g.graph, matrix)

    def test_size_graph(self):
        matrix = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]

        g = Graph(size=3)

        self.assertEqual(g.graph, matrix)

    def test_cells_independency(self):
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]

        g = Graph(size=3, is_directed=True)
        for i in range(3):
            for j in range(3):
                g.add_edge(i, j, 1+i*3+j)

        self.assertEqual(g.graph, matrix)

    def test_path_cost(self):
        g = Graph()
        g.add_edge(0,0,0)
        g.add_edge(1,1,0)
        g.add_edge(2,2,0)
        g.add_edge(0,1,2)
        g.add_edge(1,2,4)

        self.assertEqual(g.path_cost(['A','B','C','B']), 10)

        with self.assertRaises(ValueError):
            self.assertEqual(g.path_cost(['A','B','C','A']), None)

if __name__ == '__main__':
    unittest.main()

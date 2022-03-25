import unittest
from graph.utilities.graph import Graph
from graph.utilities.datamodel import Path
from graph.algorithms.travelling_salesman_nearest_neighbour import travelling_salesman_nearest_neighbour

class TestTravellingSalesmanNearestNeighbour(unittest.TestCase):

    def test_graph_1(self):
        g = Graph(is_directed=True)
        g.graph = [
            [None,  4,      24,     16,     20,     15,     9,      22  ],
            [4,     None,   20,     20,     20,     14,     8,      21  ],
            [24,    20,     None,   9,      4,      22,     16,     7   ],
            [16,    20,     9,      None,   5,      14,     17,     6   ],
            [20,    20,     4,      5,      None,   18,     12,     3   ],
            [15,    14,     22,     14,     18,     None,   6,      19  ],
            [9,     8,      16,     17,     12,     6,      None,   13  ],
            [22,    21,     7,      6,      3,      19,     13,     None],
        ]

        paths = travelling_salesman_nearest_neighbour(g, 'g')

        self.assertEqual(paths[0], Path(['G','F','D','E','H','C','B','A','G'], 68))

if __name__ == '__main__':
    unittest.main()
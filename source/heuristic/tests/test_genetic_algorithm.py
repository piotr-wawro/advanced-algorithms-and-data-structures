import unittest
from heuristic.algorithms.genetic_algorithm import genetic_algorithm
from heuristic.utilities.canvas import Canvas, Interval, create_image
from heuristic.utilities.functions import rastrigin,rosenbrock,shubert,hyper_ellipsoid,sphere,styblinski_tang,sum_squares,weierstrass

class TestGeneticAlgorithm(unittest.TestCase):

    def test_shubert(self):
        create_image(shubert, Interval(-10,10), 'shubert.png')
        solution = genetic_algorithm(
            function=shubert,
            dimension=2,
            interval=Interval(-10,10),
            iterations=100,
            pop_num=400,
            dropout=0.1,
            mutation_prob=0.05,
            canvas=Canvas('shubert.png')
        )

        self.assertAlmostEqual(solution[0], 0, delta=0.1)
        self.assertAlmostEqual(solution[1], 0, delta=0.1)
        self.assertAlmostEqual(shubert(solution), -186.7, delta=0.1)

    def test_rosenbrock(self):
        create_image(rosenbrock, Interval(-10,10), 'rosenbrock.png')
        solution = genetic_algorithm(
            function=rosenbrock,
            dimension=2,
            interval=Interval(-10,10),
            iterations=100,
            pop_num=400,
            dropout=0.1,
            mutation_prob=0.05,
            canvas=Canvas('rosenbrock.png')
        )

        self.assertAlmostEqual(solution[0], 1, delta=0.1)
        self.assertAlmostEqual(solution[1], 1, delta=0.1)
        self.assertAlmostEqual(shubert(solution), 0, delta=0.1)

if __name__ == '__main__':
    unittest.main()

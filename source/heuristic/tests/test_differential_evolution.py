import unittest
from heuristic.algorithms.differential_evolution import differential_evolution
from heuristic.utilities.canvas import Canvas, Interval, create_image
from heuristic.utilities.functions import rastrigin,rosenbrock,shubert,hyper_ellipsoid,sphere,styblinski_tang,sum_squares,weierstrass

class TestDifferentialEvolution(unittest.TestCase):

    def test_shubert(self):
        create_image(shubert, Interval(-10,10), 'shubert.png')
        solution = differential_evolution(
            function=shubert,
            dimension=2,
            interval=Interval(-10,10),
            iterations=100,
            pop_num=50,
            cross_prob=0.1,
            mutation_var=0.5,
            canvas=Canvas('shubert.png')
        )

        self.assertAlmostEqual(solution[0], 0, delta=0.1)
        self.assertAlmostEqual(solution[1], 0, delta=0.1)
        self.assertAlmostEqual(shubert(solution), -186.7, delta=0.1)

    def test_rosenbrock(self):
        create_image(rosenbrock, Interval(-10,10), 'rosenbrock.png', override=True)
        solution = differential_evolution(
            function=rosenbrock,
            dimension=2,
            interval=Interval(-10,10),
            iterations=100,
            pop_num=400,
            cross_prob=0.1,
            mutation_var=0.5,
            canvas=Canvas('rosenbrock.png')
        )

        self.assertAlmostEqual(solution[0], 1, delta=0.1)
        self.assertAlmostEqual(solution[1], 1, delta=0.1)
        self.assertAlmostEqual(shubert(solution), 0, delta=0.1)

if __name__ == '__main__':
    unittest.main()

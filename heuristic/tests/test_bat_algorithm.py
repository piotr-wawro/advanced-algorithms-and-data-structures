import unittest
from heuristic.algorithms.bat_algorithm import bat_algorithm
from heuristic.utilities.canvas import Canvas, Interval, create_image
from heuristic.utilities.functions import rastrigin,rosenbrock,shubert,hyper_ellipsoid,sphere,styblinski_tang,sum_squares,weierstrass

class TestParticleSwarm(unittest.TestCase):

    def test_shubert(self):
        create_image(shubert, Interval(-10,10), 'shubert.png')
        solution = bat_algorithm(
            function=shubert,
            dimension=2,
            interval=Interval(-10,10),
            iterations=100,
            pop_num=50,
            frequency=Interval(0.1,0.5),
            A=1,
            A_cooling_factor=0.95,
            r=Interval(0.9,1),
            r_cooling_factor=0.05,
            canvas=Canvas('shubert.png')
        )

        self.assertAlmostEqual(solution[0], 0, delta=0.1)
        self.assertAlmostEqual(solution[1], 0, delta=0.1)

    def test_rosenbrock(self):
        create_image(rosenbrock, Interval(-10,10), 'rosenbrock.png')
        solution = bat_algorithm(
            function=rosenbrock,
            dimension=2,
            interval=Interval(-10,10),
            iterations=100,
            pop_num=50,
            frequency=Interval(0.1,0.5),
            A=1,
            A_cooling_factor=0.95,
            r=Interval(0.9,1),
            r_cooling_factor=0.05,
            canvas=Canvas('rosenbrock.png')
        )

        self.assertAlmostEqual(solution[0], 1, delta=0.1)
        self.assertAlmostEqual(solution[1], 1, delta=0.1)

if __name__ == '__main__':
    unittest.main()

import unittest
from heuristic.algorithms.particle_swarm import particle_swarm
from heuristic.utilities.canvas import Canvas, Interval, create_image
from heuristic.utilities.functions import rastrigin,rosenbrock,shubert,hyper_ellipsoid,sphere,styblinski_tang,sum_squares,weierstrass

class TestParticleSwarm(unittest.TestCase):

    def test_shubert(self):
        create_image(shubert, Interval(-10,10), 'shubert.png')
        solution = particle_swarm(
            function=shubert,
            dimension=2,
            interval=Interval(-10,10),
            iterations=100,
            pop_num=50,
            corelation_to_iter=0.3,
            corelation_to_best=0.7,
            canvas=Canvas('shubert.png')
        )

        self.assertAlmostEqual(solution[0], 0, delta=0.1)
        self.assertAlmostEqual(solution[1], 0, delta=0.1)
        self.assertAlmostEqual(shubert(solution), -186.7, delta=0.1)

    def test_rosenbrock(self):
        create_image(rosenbrock, Interval(-10,10), 'rosenbrock.png')
        solution = particle_swarm(
            function=rosenbrock,
            dimension=2,
            interval=Interval(-10,10),
            iterations=100,
            pop_num=400,
            corelation_to_iter=0.3,
            corelation_to_best=0.7,
            canvas=Canvas('rosenbrock.png')
        )

        self.assertAlmostEqual(solution[0], 1, delta=0.1)
        self.assertAlmostEqual(solution[1], 1, delta=0.1)
        self.assertAlmostEqual(shubert(solution), 0, delta=0.1)

if __name__ == '__main__':
    unittest.main()

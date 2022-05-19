import unittest
from clustering.algorithms.k_means import k_means
from clustering.utilities.blob import blob
from clustering.utilities.canvas import Canvas

class TestKMeans(unittest.TestCase):

    def test_case_1(self):
        blob1 = blob([50, 50], 25, 20)
        blob2 = blob([200, 200], 50, 100)
        blob3 = blob([300, 300], 50, 40)
        blob4 = blob([300, 100], 70, 60)
        blob5 = blob([100, 320], 60, 40)
        points = blob1+blob2+blob3+blob4+blob5

        k_means(points, 5, Canvas())
        # k_means(points, 5)

if __name__ == '__main__':
    unittest.main()

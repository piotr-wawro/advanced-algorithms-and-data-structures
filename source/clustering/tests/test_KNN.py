import unittest
from clustering.algorithms.KNN import KNN
from clustering.utilities.blob import blob
from clustering.utilities.metric import euclidean_distance

class TestKMeans2(unittest.TestCase):

    def test_case_1(self):
        blob1 = blob([50, 50], 25, 20)
        blob2 = blob([200, 200], 50, 100)
        blob3 = blob([300, 300], 50, 40)
        blob4 = blob([300, 100], 70, 60)
        blob5 = blob([100, 320], 60, 40)
        points = blob1+blob2+blob3+blob4+blob5

        label1 = [1 for _ in range(20)]
        label2 = [2 for _ in range(100)]
        label3 = [3 for _ in range(40)]
        label4 = [4 for _ in range(60)]
        label5 = [5 for _ in range(40)]
        labels = label1+label2+label3+label4+label5

        solution = KNN(points, labels, 5, [230, 180], euclidean_distance)
        self.assertEqual(solution, 2)

if __name__ == '__main__':
    unittest.main()

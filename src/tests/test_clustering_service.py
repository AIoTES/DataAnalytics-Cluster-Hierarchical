import unittest
import numpy as np

from src.services.clustering_impl import ClusteringImpl


# TODO añadir un test con un juego de datos más amplio
class TestClusteringService(unittest.TestCase):

    def setUp(self):
        self.clustering_service = ClusteringImpl()

    def test_agglomerativeClustering(self):
        x = np.array([[1, 2], [1, 4], [1, 0],
                      [4, 2], [4, 4], [4, 0]])
        result = self.clustering_service.agglomerativeClustering(data=x)
        self.assertEqual("[1 1 1 0 0 0]", str(result))

    def test_agglomerativeClustering2(self):
        x = np.array(
            [
                [5.1, 3.5, 1.4, 0.2],
                [5.8, 4.0, 1.2, 0.2],
                [5.7, 4.4, 1.5, 0.4],
                [5.4, 3.9, 1.3, 0.4],
                [5.1, 3.5, 1.4, 0.3],
                [5.7, 3.8, 1.7, 0.3],
                [5.1, 3.8, 1.5, 0.3],
                [5.4, 3.4, 1.7, 0.2],
                [5.1, 3.7, 1.5, 0.4]
            ]
        )
        x = np.concatenate((x, [[4.6, 3.6, 1.0, 0.2]]))

        result = self.clustering_service.agglomerativeClustering(data=x)
        self.assertEqual("[0 1 1 1 0 0 0 0 0 0]", str(result))

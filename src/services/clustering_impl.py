from sklearn.cluster import AgglomerativeClustering

from src.services.clustering_service import Clustering


class ClusteringImpl(Clustering):

    def agglomerativeClustering(self, n_clusters=2, affinity='euclidean', linkage='ward', data=None):
        return AgglomerativeClustering(n_clusters=n_clusters, affinity=affinity, linkage=linkage).fit_predict(data)


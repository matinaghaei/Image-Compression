from clusters import Clusters
from data import Data
import matplotlib.pyplot as plt


class KMeans:

    def __init__(self, coordinates, number_of_clusters):
        self.clusters = Clusters(number_of_clusters, coordinates.shape[1])
        self.data = Data(coordinates, self.clusters)
        self.clusters.set_data(self.data)

    def start(self, termination_condition_threshold):
        self.data.update_memberships()
        while self.clusters.update_centers() >= termination_condition_threshold:
            self.data.update_memberships()
        return self.clusters.total_error()

    def plot_data(self):
        self.data.plot()
        self.clusters.plot()
        plt.show()

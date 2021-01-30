import random
import numpy as np
import matplotlib.pyplot as plt
from data import Data


class Clusters:

    def __init__(self, number_of_clusters, dims):
        self.number_of_clusters = number_of_clusters
        self.dims = dims
        self.centers = None
        self.data = None

    def set_data(self, data):
        self.data = data
        self.centers = random.sample(list(data.coordinates), self.number_of_clusters)

    def size(self):
        return self.number_of_clusters

    def get_center(self, index):
        return self.centers[index]

    def update_centers(self):
        max_change = 0
        for j in range(self.number_of_clusters):
            s1 = np.zeros(self.dims)
            s2 = 0
            for i in range(self.data.size()):
                if self.data.get_membership(i) == j:
                    s1 += self.data.get_data(i)
                    s2 += 1
            max_change = max(max_change, Data.cal_distance(self.centers[j], s1 / s2))
            self.centers[j] = s1 / s2
        return max_change

    def error(self, c):
        n = 0
        s = 0
        for i in range(self.data.size()):
            if self.data.get_membership(i) == c:
                s += Data.cal_distance(self.centers[c], self.data.get_data(i))
                n += 1
        return s / n

    def total_error(self):
        s = 0
        for c in range(self.number_of_clusters):
            s += self.error(c)
        return s / self.number_of_clusters

    def plot(self):
        for center in self.centers:
            plt.scatter(center[0], center[1], s=100, c='k')

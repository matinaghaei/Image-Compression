import math
import matplotlib.pyplot as plt


class Data:
    colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan']

    @staticmethod
    def cal_distance(coordinate1, coordinate2):
        s = 0
        for d in range(len(coordinate1)):
            s += (coordinate1[d] - coordinate2[d]) ** 2
        return math.sqrt(s)

    def __init__(self, coordinates, clusters):
        self.coordinates = coordinates
        self.clusters = clusters
        self.memberships = [0] * len(coordinates)

    def size(self):
        return len(self.coordinates)

    def get_membership(self, data_index):
        return self.memberships[data_index]

    def get_data(self, data_index):
        return self.coordinates[data_index]

    def update_memberships(self):
        for i in range(len(self.coordinates)):
            for j in range(self.clusters.size()):
                k = self.memberships[i]
                d1 = self.cal_distance(self.coordinates[i], self.clusters.get_center(j))
                d2 = self.cal_distance(self.coordinates[i], self.clusters.get_center(k))
                if d1 < d2:
                    self.memberships[i] = j

    def plot(self):
        for i in range(len(self.coordinates)):
            plt.scatter(self.coordinates[i, 0], self.coordinates[i, 1], c=self.colors[self.memberships[i] % 10])

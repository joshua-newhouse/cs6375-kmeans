import numpy
import sys

from data import DataSet
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

class Application:
    def __init__(self, fileName, nClusters, maxIterations):
        self.fileName = fileName
        self.nClusters = int(nClusters)
        self.maxIterations = int(maxIterations)
        self.model = KMeans(n_clusters=self.nClusters, init='k-means++', max_iter=self.maxIterations)

        data = numpy.genfromtxt(fileName, missing_values=('?'), usecols=(0, 1, 2, 3, 4, 5))
        self.dataSet = DataSet(data)
    # __init__

    def start(self):
        self.model.fit(self.dataSet.dataPoints)

        print(self.model.labels_)
        print(self.model.cluster_centers_)

        plt.subplots(1, sharey=True, figsize=(10,6))

        self.generatePlot("mpg vs cylinders", 1)
        self.generatePlot("mpg vs displacement", 2)
        self.generatePlot("mpg vs horsepower", 3)
        self.generatePlot("mpg vs weight", 4)
        self.generatePlot("mpg vs acceleration", 5)
    # start

    def generatePlot(self, title, y):
        plt.title(title)
        plt.scatter(self.dataSet.dataPoints[:,y], self.dataSet.dataPoints[:,0], c=self.model.labels_)
        plt.show()
# Application

# Main Entry
def main():
    app = Application(sys.argv[1], sys.argv[2], sys.argv[3])
    app.start()
# main

if __name__ == "__main__":
    main()
# fi

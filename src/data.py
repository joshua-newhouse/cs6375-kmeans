import numpy

class DataSet:
    def __init__(self, data):
        self.nPoints = 0
        self.dataPoints = data[~numpy.isnan(data).any(axis=1)]

        # for i in range(len(self.dataPoints)):
        #     if numpy.isnan(self.dataPoints[i]).any():
        #         self.dataPoints = numpy.delete(self.dataPoints, i, 0)

        self.nPoints = len(self.dataPoints)
    # __init__

    def printDataPoints(self):
        for dataPoint in self.dataPoints:
            print(dataPoint)
        # for
    # printDataPoints

    def printByIndex(self, index):
        print(self.getDataPoint(index))
    # printByIndex

    def getDataPoint(self, index):
        return self.dataPoints[index]
    # getDataPoint

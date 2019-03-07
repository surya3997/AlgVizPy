import numpy as np
import random


class MultipleRegression:
    def __init__(self, _x, _y):
        self.X = np.array(_x)
        self.Y = np.array(_y)

    def calculateCoeff(self):
        Xtranspose = self.X.transpose()
        A = np.dot(Xtranspose, self.X)
        B = np.dot(Xtranspose, self.Y)

        Ainverse = np.linalg.inv(A)
        self.coeff = np.dot(Ainverse, B)

    def predict(self, inpX):
        return sum(np.array(inpX) * self.coeff)


a = 400
nums = 10
dimension = 5
dataX = [[random.randint(1, a) for i in range(dimension)] for j in range(nums)]
dataY = [random.randint(1, a) for i in range(nums)]
lr = MultipleRegression(dataX, dataY)
lr.calculateCoeff()
test_y = lr.predict([random.randint(1, a) for i in range(dimension)])

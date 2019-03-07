import numpy as np
import random
from MultipleRegression import MultipleRegression


class PolynomialRegression(MultipleRegression):
    def __init__(self, _x, _y, _dim):
        self.dimension = _dim
        self.X = np.array([self.getPowers(j) for j in _x])
        self.Y = np.array(_y)

    def getPowers(self, x_val):
        return [x_val ** i for i in range(1, self.dimension + 1)]

    def predict(self, x_value):
        return super().predict(self.getPowers(x_value))


a = 400
nums = 10
dimension = 5

dataX = [random.randint(1, a) for i in range(nums)]
dataY = [random.randint(1, a) for i in range(nums)]
lr = PolynomialRegression(dataX, dataY, dimension)
lr.calculateCoeff()
test_y = lr.predict(random.randint(1, a))

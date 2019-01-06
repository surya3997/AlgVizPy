from MultipleRegression import MultipleRegression
from LinearRegression import LinearRegression
import math, random
import numpy as np

def sigmoid(value):
    return 1 / (1 + math.exp(-value))

class LogisticRegression:
    def __init__(self, _x, _y):
        self.X = np.array(_x)
        self.Y = np.array(_y)

    def predict(self, _x_val):
        mr = None
        if type(_x_val) is not list:
            mr = LinearRegression(self.X, self.Y)
        else:
            mr = MultipleRegression(self.X, self.Y)
        mr.calculateCoeff()
        y_val = mr.predict(_x_val)
        prob_val = sigmoid(y_val)
        if prob_val < 0.5:
            return 0
        else:
            return 1


dataX = [15, 17, 16, 18, 19, 14, 16, 17, 34, 25, 53, 32, 51]
dataY = [0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1]
lr = LogisticRegression(dataX, dataY)
label_predict = lr.predict(36)
print(label_predict)


a = 400
nums = 10
dimension = 5
# dataX = [random.randint(1, a) for i in range(nums)]
# dataY = [random.randint(1, a) for i in range(nums)]
dataX = [[random.randint(1, a) for i in range(dimension)] for j in range(nums)]
dataY = [random.randint(0, 1) for i in range(nums)]
lr = LogisticRegression(dataX, dataY)
label_predict = lr.predict([random.randint(1, a) for i in range(dimension)])
print(label_predict)
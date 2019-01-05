import numpy as np
from p5 import *
import random

class LinearRegression:
    def __init__(self, _x, _y):
        self.X = _x[:]
        self.Y = _y[:]
        self.n = len(self.X)

    def calculateCoeff(self):
        sumOfX = sum(self.X)
        sumOfY = sum(self.Y)
        sumOfXsquare = sum(map(lambda x: x*x, self.X))
        sumOfXY = sum(map(lambda l, m: l*m, self.X, self.Y))
        A = np.array([[sumOfXsquare, sumOfX], [sumOfX, self.n]])
        B = np.array([sumOfXY, sumOfY])

        Ainverse = np.linalg.inv(A)
        coeff = np.dot(Ainverse, B)
        #print(coeff)

        self.slope = coeff[0]
        self.intercept = coeff[1]

    def predict(self, inpX):
        return self.slope * inpX + self.intercept

# dataX = [15, 17, 16, 18, 19, 14, 16, 17, 34, 25, 53, 32, 51]
# dataY = [3, 66, 8, 23, 34, 43, 73, 31, 93, 53, 72, 71, 135]
a = 400
nums = 10
dataX = [random.randint(1, a) for i in range(nums)]
dataY = [random.randint(1, a) for i in range(nums)]
lr = LinearRegression(dataX, dataY)
lr.calculateCoeff()

def setup():
    size(a, a)
    no_stroke()
    background(204)
    

def draw():
    fill(255, 0, 0)
    stroke(0)
    for i, j in zip(dataX, dataY):
        circle((i, j), 20)

    line((0, lr.intercept), (a, a * lr.slope + lr.intercept))

        
def mouse_clicked():
    newVal = random.randint(1, a)
    prediction = lr.predict(newVal)

    fill(0, 0, 255)
    stroke(0)
    circle((newVal, prediction), 20)
    redraw()


def main():
    run()

if __name__ == "__main__":
    main()
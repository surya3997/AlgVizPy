import math
import matplotlib.pyplot as plt

"""

x2 =  x0 * f(x1) - x1 * f(x0)
     -------------------------
          f(x1) - f(x0)

"""


precision = 4


def y_fun(x):
    y = math.exp(x) - (4 * x)
    return y


def cal_x2(x0, x1):
    numerator = x0 * y_fun(x1) - x1 * y_fun(x0)
    denominator = y_fun(x1) - y_fun(x0)

    x2 = numerator / denominator
    return round(x2, precision)


x0 = 0
x1 = 1

stopper = 20

x2 = cal_x2(x0, x1)

cnt = 0

while y_fun(x2) != 0 and cnt < stopper:
    x2 = cal_x2(x0, x1)

    print((x0, y_fun(x0)), (x2, y_fun(x2)), (x1, y_fun(x1)))

    plt.scatter(x0, y_fun(x0))
    plt.scatter(x1, y_fun(x1), color='red')
    plt.show()

    if y_fun(x0) * y_fun(x2) < 0:
        x1 = x2
    else:
        x0 = x2

    cnt += 1

    if x2 == cal_x2(x0, x1):
        break

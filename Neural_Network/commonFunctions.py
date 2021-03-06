import numpy as np
import math


def getRandWeight(_):
    precision = 100
    return np.random.randint(1, precision) / precision


def matrixMap(function, array):
    return np.vectorize(function)(array)


def sigmoid(value):
    return 1 / (1 + math.exp(-value))


def dsigmoid(value):
    fun_val = sigmoid(value)
    return fun_val * (1 - fun_val)

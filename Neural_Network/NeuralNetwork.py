import random
import numpy as np
from commonFunctions import *


class NeuralNetwork:
    def __init__(self, _n_input, _n_hidden, _n_output, _lr):
        self.lrate = _lr
        self.num_inputs = _n_input
        self.num_hidden = _n_hidden
        self.num_output = _n_output

        self.wts_ih = np.zeros([self.num_hidden, self.num_inputs + 1])
        self.wts_ho = np.zeros([self.num_output, self.num_hidden])

        self.wts_ih = matrixMap(getRandWeight, self.wts_ih)
        self.wts_ho = matrixMap(getRandWeight, self.wts_ho)

    def predict(self, inp, target):
        self.inp_vector = np.append(inp, 1)
        self.hidden_nodes = matrixMap(sigmoid, np.dot(self.wts_ih, self.inp_vector))
        self.output = matrixMap(sigmoid, np.dot(self.wts_ho, self.hidden_nodes))
        print(target[0], np.argmax(self.output))
        return self.output
import random


class Perceptron:
    def __init__(self, n_input, _lr):
        self.lrate = _lr
        self.num_inputs = n_input
        self.weights = list()
        self.bias = 1
        self.randomize_wts()

    def randomize_wts(self, weight_precision=1000):
        self.weights = list()

        for i in range(self.num_inputs + 1):
            wt = random.randint(1, weight_precision) / weight_precision
            self.weights.append(wt)

    def activation_fn(self, wt_sum):
        if wt_sum >= 0.5:
            return 1
        else:
            return 0

    def guess(self, inputs):
        weighted_sum = 0
        for i in range(self.num_inputs):
            weighted_sum += inputs[i] * self.weights[i]
        weighted_sum += self.bias * self.weights[-1]
        return self.activation_fn(weighted_sum)

    def train(self, inputs, label):
        predicted = self.guess(inputs)
        actual = label
        error = actual - predicted

        for i in range(self.num_inputs):
            self.weights[i] += inputs[i] * error * self.lrate
        self.weights[-1] += self.bias * error * self.lrate

        return self.weights

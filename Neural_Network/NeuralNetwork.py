import random
import numpy as np
from commonFunctions import *
from time import gmtime, strftime
import json


class NeuralNetwork:
    '''
    Creates a Neural Network with input layer, hidden layer and output layer.
    Arguments : no.of input nodes, no.of hidden nodes, no.of output nodes, learning_rate
    Optional Arguments : Activation function {Default : Sigmoid}, Derivative of activation function
    Methods : train, predict
    '''

    def __init__(self, _n_input, _n_hidden, _n_output, _lr, _activation=sigmoid, _activ_deriv=dsigmoid, memory=None):
        self.activation = _activation
        self.activ_derivative = _activ_deriv

        if memory is None:
            self.lrate = _lr
            self.num_inputs = _n_input
            self.num_hidden = _n_hidden
            self.num_output = _n_output

            self.wts_ih = np.zeros([self.num_hidden, self.num_inputs + 1])
            self.wts_ho = np.zeros([self.num_output, self.num_hidden + 1])

            self.wts_ih = matrixMap(getRandWeight, self.wts_ih)
            self.wts_ho = matrixMap(getRandWeight, self.wts_ho)
        else:
            self.lrate = memory['lrate']
            self.num_inputs = memory['num_inputs']
            self.num_hidden = memory['num_hidden']
            self.num_output = memory['num_output']

            self.wts_ih = np.array(memory['wts_ih'])
            self.wts_ho = np.array(memory['wts_ho'])

    def getOneHotTarget(self, value):
        targets = np.zeros(self.num_output)
        targets[value] = 1
        return targets

    def predict(self, inputs):
        '''
        returns a predicted output class label for the given input
        '''
        inp_vector = np.append(inputs, 1)

        hidden_nodes_without_activation = np.dot(self.wts_ih, inp_vector)
        hidden_nodes_active_without_bias = matrixMap(
            self.activation, hidden_nodes_without_activation)
        hidden_nodes = np.append(hidden_nodes_active_without_bias, 1)

        output_without_activation = np.dot(self.wts_ho, hidden_nodes)
        outputs = matrixMap(self.activation, output_without_activation)
        predicted_label = np.argmax(outputs)
        return predicted_label

    def train(self, inputs, targ):
        '''
        train the Neural Network with inputs and the output class labels (numerical)
        '''
        inp_vector = np.append(inputs, 1)

        hidden_nodes_without_activation = np.dot(self.wts_ih, inp_vector)
        hidden_nodes_active_without_bias = matrixMap(
            self.activation, hidden_nodes_without_activation)
        hidden_nodes = np.append(hidden_nodes_active_without_bias, 1)

        output_without_activation = np.dot(self.wts_ho, hidden_nodes)
        outputs = matrixMap(self.activation, output_without_activation)

        targets = self.getOneHotTarget(targ)

        output_error = targets - outputs

        wts_ho_trans = self.wts_ho.transpose()
        hidden_errors = np.dot(wts_ho_trans, output_error)

        output_gradients = matrixMap(
            self.activ_derivative, output_without_activation)
        error_deriv = output_gradients * output_error
        hid_trans = hidden_nodes.transpose()
        wts_ho_deltas = self.lrate * np.outer(error_deriv, hid_trans)
        self.wts_ho += wts_ho_deltas

        hidden_gradients = matrixMap(
            self.activ_derivative, hidden_nodes_without_activation)
        inp_error_deriv = hidden_errors[:-1] * hidden_gradients
        inp_trans = inp_vector.transpose()
        wts_ih_deltas = self.lrate * np.outer(inp_error_deriv, inp_trans)
        self.wts_ih += wts_ih_deltas
        return outputs

    def serialze(self, file_path=None):
        if file_path is None:
            file_path = strftime("%Y-%m-%d_%H-%M-%S", gmtime()) + '.json'

        data = {
            'lrate': self.lrate,
            'num_inputs': self.num_inputs,
            'num_hidden': self.num_hidden,
            'num_output': self.num_output,
            'wts_ih': self.wts_ih.tolist(),
            'wts_ho': self.wts_ho.tolist()
        }

        with open(file_path, "w") as write_file:
            json.dump(data, write_file)

    def deserialize(file_path):
        with open(file_path) as read_file:
            data = json.loads(read_file.read())
        return data

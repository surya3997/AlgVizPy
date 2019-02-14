import NeuralNetwork
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

lr = 0.1
epoch = 10

def train_all_inputs(nn, inp_arr, tar_arr):
    for j in range(epoch):
        for ind in range(len(inp_arr)):
            inp_row, tar_row = inp_arr.iloc[ind], tar_arr.iloc[ind]
            output = nn.train(inp_row.values, tar_row.values)
            #print(output)
        # print()

def test_nn(nn, inputs, targets):
    for ind in range(len(inputs)):
        inp_row, tar_row = inputs.iloc[ind], targets.iloc[ind]
        output = nn.predict(inp_row.values)
        print(output, tar_row.values[0])


def main():
    data = pd.read_csv('./dataset/iris.csv', header=None)
    data = data.replace('Iris-setosa', 0)
    data = data.replace('Iris-versicolor', 1)
    data = data.replace('Iris-virginica', 2)

    train, test = train_test_split(data, test_size=0.2)

    inp_data = train[[0, 1, 2, 3]]
    target = train[[4]]

    nn = NeuralNetwork.NeuralNetwork(4, 5, 3, 0.1)
    train_all_inputs(nn, inp_data, target)
    test_nn(nn, test[[0, 1, 2, 3]], test[[4]])


if __name__ == "__main__":
    main()

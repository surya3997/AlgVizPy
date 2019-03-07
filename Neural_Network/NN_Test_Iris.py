import NeuralNetwork
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

epoch = 250


def train_all_inputs(nn, inp_arr, tar_arr):
    for j in range(epoch):
        for ind in range(len(inp_arr)):
            inp_row, tar_row = inp_arr.iloc[ind], tar_arr.iloc[ind]
            output = nn.train(inp_row.values, tar_row.values)
            # print(output)
        # print()


def test_nn(nn, inputs, targets):
    correct = 0
    for ind in range(len(inputs)):
        inp_row, tar_row = inputs.iloc[ind], targets.iloc[ind]
        output = nn.predict(inp_row.values)
        actual = tar_row.values[0]
        print(output, actual)
        if output == actual:
            correct += 1
    print(correct * 100 / len(inputs))


def preprocessing(data, output_label):
    data = data.replace('Iris-setosa', 0)
    data = data.replace('Iris-versicolor', 1)
    data = data.replace('Iris-virginica', 2)

    train, test = train_test_split(data, test_size=0.2)
    x_cols = list(train.columns)
    x_cols.remove(output_label)
    train_x = train[x_cols]
    train_y = train[[output_label]]
    test_x = test[x_cols]
    test_y = test[[output_label]]

    return train_x, train_y, test_x, test_y


def main():
    lr = 0.1
    data = pd.read_csv('./dataset/iris.csv', header=None)
    nn = NeuralNetwork.NeuralNetwork(4, 5, 3, lr)

    train_x, train_y, test_x, test_y = preprocessing(data, 4)
    train_all_inputs(nn, train_x, train_y)
    test_nn(nn, test_x, test_y)


if __name__ == "__main__":
    main()

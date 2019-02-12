import NeuralNetwork
import numpy as np
import pandas as pd

inp_array = np.array([
                        [2, 23, 6],
                        [3, 4, 1],
                        [2, 22, 4]                       
                    ])

target = np.array([[1], [0], [1]])

lr = 0.1
epoch = 10

def train_all_inputs(nn, inp_arr, tar_arr):
    for j in range(epoch):
        for ind in range(len(inp_arr)):
            inp_row, tar_row = inp_arr.iloc[ind], tar_arr.iloc[ind]
            output = nn.predict(inp_row.values, tar_row.values)
            #print(output)
        print()

def guess_all_inputs(nn):
    for inp, tar in zip(inp_array, target):
        print(nn.predict(inp, tar))
    print()


def main():
    data = pd.read_csv('./dataset/iris.csv', header=None)
    data = data.replace('Iris-setosa', 0)
    data = data.replace('Iris-versicolor', 1)
    data = data.replace('Iris-virginica', 2)
    inp_data = data[[0, 1, 2, 3]]
    target = data[[4]]
    #print(inp_data)
    nn = NeuralNetwork.NeuralNetwork(4, 4, 3, 0.1)
    train_all_inputs(nn, inp_data, target)


if __name__ == "__main__":
    main()

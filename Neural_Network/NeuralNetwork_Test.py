import NeuralNetwork
import numpy as np


inp_array = np.array([
                        [2, 23, 6],
                        [3, 4, 1],
                        [2, 22, 4]                       
                    ])

target = np.array([[1], [0], [1]])

lr = 0.1
epoch = 10

def train_all_inputs(nn):
    for j in range(epoch):
        for inp, tar in zip(inp_array, target):
            print(nn.predict(inp, tar))
        print()

def guess_all_inputs(nn):
    for inp, tar in zip(inp_array, target):
        print(nn.predict(inp, tar))
    print()


def main():
    nn = NeuralNetwork.NeuralNetwork(3, 4, 1, 0.1)
    train_all_inputs(nn)


if __name__ == "__main__":
    main()

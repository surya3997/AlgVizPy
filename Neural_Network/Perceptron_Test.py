from Perceptron import *

inp_data = [
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1]
    ]

target_data = [0, 0, 0, 1]  # AND Gate
target_data1 = [0, 1, 1, 1] # OR Gate
lr = 0.1

epoch = 10

def train_all_inputs(p):
    for j in range(epoch):
        for i in range(len(inp_data)):
            rand_index = random.randint(0, len(inp_data) - 1)
            wts = p.train(inp_data[rand_index], target_data[rand_index])
            guess_all_inputs(p)

def guess_all_inputs(p):
    for i in inp_data:
        print(p.guess(i), end=" ")
    print()

def main():
    n = len(inp_data[0])
    p = Perceptron(n, lr)
    train_all_inputs(p)


if __name__ == "__main__":
    main()

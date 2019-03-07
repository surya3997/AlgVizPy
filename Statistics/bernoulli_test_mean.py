import bernoulli_rand_var
import matplotlib.pyplot as plt
import numpy as np

sample_cnts = 60
epsilon = 0.1
head_cnt = 0
prob_list = list()

for sample_cnt in range(1, sample_cnts):
    for i in range(sample_cnt):
        head = bernoulli_rand_var.bernoulli_trail()
        head_cnt += head

    prob = head_cnt / sample_cnt
    # print(prob)

    greater_eps_cnt = 0
    if abs(prob - 0.5) > epsilon:
        greater_eps_cnt += 1

    epsilon_prob = greater_eps_cnt/sample_cnt
    print(epsilon_prob)
    prob_list.append(epsilon_prob)

prob_arr = np.array(prob_list)
plt.hist(prob_arr, bins=20)
plt.ylabel('No of times')
plt.show()

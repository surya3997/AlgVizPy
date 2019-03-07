import numpy as np
import operator


def clean(data):
    cleaned = []
    for row in data:
        if '?' in row:
            continue
        else:
            cleaned.append(row)
    return cleaned


def getCancerData():
    import os
    import sys
    prefix_path = os.path.split(sys.argv[0])[0] + '/'
    path = '../dataset/cancer_dataset.csv'
    correct_path = prefix_path + path
    with open(correct_path, 'r') as f:
        content_with_header = f.read().splitlines()
    unclean_content = content_with_header[1:]
    content = clean(unclean_content)
    result_x = list(map(lambda x: list(map(int, x.split(',')[1:-1])), content))
    result_y = list(map(lambda x: int(x.split(',')[-1]), content))
    return(result_x, result_y)


def leaveOneOut(x_data, y_data):
    training_x = x_data[:-1]
    training_y = y_data[:-1]
    testing_x = x_data[-1]
    testing_y = y_data[-1]
    return training_x, training_y, testing_x, testing_y


def eucleidian_distance(point1, point2):
    if len(point1) == len(point2):
        dist = 0
        for i, j in zip(point1, point2):
            dist += (i - j) ** 2
        return np.sqrt(dist)


def KNN(train_x, train_y, test_x, test_y, k, distance_func):
    dist_dict = {}
    for x in range(len(train_x)):
        distance = distance_func(train_x[x], test_x)
        dist_dict[x] = distance
    sorted_dist = sorted(dist_dict.items(), key=operator.itemgetter(1))

    freq_count = {}
    for i in range(k):
        result = train_y[sorted_dist[i][0]]
        if result in freq_count:
            freq_count[result] += 1
        else:
            freq_count[result] = 1

    sorted_count = sorted(freq_count.items(),
                          key=operator.itemgetter(1), reverse=True)
    return sorted_count[0][0]


data_x, data_y = getCancerData()
train_x, train_y, test_x, test_y = leaveOneOut(data_x, data_y)
k = 100
predicted_class = KNN(train_x, train_y, test_x, test_y, k, eucleidian_distance)
print(predicted_class)

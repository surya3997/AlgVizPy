import numpy as np

def getCancerData():
    import os, sys
    prefix_path = os.path.split(sys.argv[0])[0] + '/'
    path = '../dataset/cancer_dataset.csv'
    correct_path = prefix_path + path
    with open(correct_path, 'r') as f:
        content_with_header = f.read().splitlines()
    content = content_with_header[1:]
    result_x = list(map(lambda x: x.split(',')[1:-1], content))
    result_y = list(map(lambda x: x.split(',')[-1], content))
    return(result_x, result_y)


data_x, data_y = getCancerData()
print()
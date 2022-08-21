from random import shuffle
from p5 import *

def bubble_sort(arr):
    for j in range(len(arr)):
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]


def setup():
    size(300, 300)
    no_stroke()
    background(204)


def draw():
    # fill(255, 0, 0)
    # stroke(0)
    fill(0)
    for i in range(len(arr)):
            rect((0, i*10), x[i], 8)

if __name__ == "__main__":
    arr = [i for i in range(100)]
    globals()['arr'] = arr
    shuffle(arr)
    print("Before Sorting")
    print(arr)
    # bubble_sort(arr)
    # print("After Sorting")
    # print(arr)
    run()
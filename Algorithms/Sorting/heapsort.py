from typing import List
from random import shuffle

def heapify(arr: List[int], position: int, n: int):
    largest = position
    index = position * 2 + 1
    if index < n and arr[largest] < arr[index]:
        largest = index

    index = position * 2 + 2
    if index < n and arr[largest] < arr[index]:
        largest = index

    if position != largest:
        arr[largest], arr[position] = arr[position], arr[largest]
        heapify(arr, largest, n)


def heapsort(arr: List[int]):
    for i in range(len(arr) - 1 // 2, -1, -1):
        heapify(arr, i, len(arr))
    for i in range(len(arr) - 1, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, 0, i)


if __name__ == "__main__":
    arr = list(range(100))
    shuffle(arr)
    print(arr)
    print()
    heapsort(arr)
    print(arr)

from typing import List
from random import shuffle

def partition(arr: List[int], low: int, high: int) -> int:
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i

def quicksort(arr: List[int], low: int, high: int):
    if low < high:
        pivot = partition(arr, low, high)
        quicksort(arr, low, pivot - 1)
        quicksort(arr, pivot + 1, high)


if __name__ == "__main__":
    arr = list(range(100))
    shuffle(arr)
    print(arr)
    print()
    quicksort(arr, 0, len(arr)-1)
    print(arr)

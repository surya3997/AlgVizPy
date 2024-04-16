import random

def insertion(arr):
    for i in range(1, len(arr)):
        if arr[i] >= arr[i-1]:
            continue
        
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key

if __name__ == "__main__":
    arr = list(range(100))
    random.shuffle(arr)
    print(arr)
    print("Sorted:")
    insertion(arr)
    print(arr)
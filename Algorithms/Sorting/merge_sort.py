from random import shuffle

def merge(arr, l, m, r):
    left_arr = arr[l:m]
    right_arr = arr[m:r+1]

    left_index = 0
    right_index = 0
    actual_index = l

    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            arr[actual_index] = left_arr[left_index]
            left_index += 1
        else:
            arr[actual_index] = right_arr[right_index]
            right_index += 1
        actual_index += 1

    while left_index < len(left_arr):
        arr[actual_index] = left_arr[left_index]
        actual_index += 1
        left_index += 1

    while right_index < len(right_arr):
        arr[actual_index] = right_arr[right_index]
        right_index += 1
        actual_index += 1


def mergesort(arr, l, r):
    if l < r:
        mid = (l + r) // 2
        mergesort(arr, l, mid)
        mergesort(arr, mid+1, r)
        merge(arr, l, mid+1, r)

if __name__ == "__main__":
    arr = list(range(100))
    shuffle(arr)
    print(arr)
    print()
    mergesort(arr, 0, len(arr)-1)
    print(arr)
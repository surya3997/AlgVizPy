import random
from typing import List

def bin_search(arr: List[int], target: int, low:int, high:int) -> int:
    if low > high: return -1
    mid_index = (low + high) // 2
    # print(arr[mid_index])
    if arr[mid_index] == target: return mid_index
    elif arr[mid_index] > target: return bin_search(arr, target, low, mid_index-1)
    else: return bin_search(arr, target, mid_index+1, high)

def bin_search_iter(arr, target, low, high):
	while low <= high:
		mid_index = (low + high) // 2
		if arr[mid_index] == target:
			return mid_index
		elif arr[mid_index] > target:
			high = mid_index - 1
		else:
			low = mid_index + 1
	return -1

n = random.randint(0, 10)
arr = list(range(100, n+100))
target = -10
if arr:
    target = random.choice(arr)
answer = bin_search(arr, target, 0, len(arr)-1)
answer1 = bin_search_iter(arr, target, 0, len(arr)-1)
print(arr, target, answer, answer1 == answer)

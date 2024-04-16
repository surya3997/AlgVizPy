def constant_space(n: int) -> int:
	one, two = 0, 1

	for i in range(n):
		tmp = one
		one = two
		two = tmp + two
	return one

def recursive(n: int) -> int:
	if n == 0:
		return 0
	if n == 1:
		return 1
	return recursive(n-1) + recursive(n-2)

def linear_space(n: int) -> int:
	if n == 0:
		return 0
	cache = [1] * n
	for i in range(2, n):
		cache[i] = cache[i-1] + cache[i-2]
	return cache[-1]

mem_cache = {}
def memoization(n:int) -> int:
	global mem_cache
	if n == 0:
		return 0
	if n == 1:
		return 1
	if n in mem_cache:
		return mem_cache[n]
	value = memoization(n-1) + memoization(n-2)
	mem_cache[n] = value
	return value

if __name__ == "__main__":
	chosen = lambda x: print(memoization(x))
	chosen(0)
	chosen(1)
	chosen(2)
	chosen(3)
	chosen(5)
	chosen(8)

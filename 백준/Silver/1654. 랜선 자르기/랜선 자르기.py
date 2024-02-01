import sys
input = sys.stdin.readline
k, n = map(int, input().split())
length = [int(input()) for _ in range(k)]
start, end = 1, max(length)
result = 0
while start <= end: 
	mid = (start + end) // 2
	if sum(map(lambda x: x // mid, length)) >= n: # 너무 잘게 쪼갬 - 늘려야 함
		start = mid + 1
		result = mid
	else: # 너무 크게 쪼갬 - 줄여야 함 
		end = mid - 1
print(result) 
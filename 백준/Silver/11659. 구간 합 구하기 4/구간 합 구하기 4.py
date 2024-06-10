import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr_sum = [0] * (n+1)
for i in range(1, n+1):
	arr_sum[i] = arr_sum[i-1] + arr[i-1]
while m > 0:
	i, j = map(int, input().split())
	print(arr_sum[j] - arr_sum[i-1])
	m -= 1
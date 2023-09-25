import sys
input = sys.stdin.readline
n, k = map(int, input().split())
div = [i for i in range(1, n+1) if n % i == 0]
if len(div) < k:
	print(0)
else:
	print(div[k-1])
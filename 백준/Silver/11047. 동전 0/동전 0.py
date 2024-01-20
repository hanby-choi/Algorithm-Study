import sys
input = sys.stdin.readline
n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
index = cnt = 0
for i, coin in enumerate(coins):
	if coin <= k:
		index = i
	else:
		break
for i in range(index, -1, -1):
	cnt += k // coins[i]
	k %= coins[i]
	if k == 0:
		print(cnt)
		break
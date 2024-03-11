import sys
input = sys.stdin.readline
n, m = map(int, input().split())
mem = [0] + list(map(int, input().split()))
cost = [0] + list(map(int, input().split()))
total_cost = sum(cost)
dp = [[0] * (total_cost + 1) for _ in range(n+1)]
ans = total_cost
for i in range(1, n + 1):
	for c in range(total_cost + 1):
		if c < cost[i]:
			dp[i][c] = dp[i-1][c]
		else:
			dp[i][c] = max(dp[i-1][c-cost[i]] + mem[i], dp[i-1][c])
		if dp[i][c] >= m:
			ans = min(ans, c)
print(ans)
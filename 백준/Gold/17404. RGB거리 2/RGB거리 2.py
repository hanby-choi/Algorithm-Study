import sys 
input = sys.stdin.readline
n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]
INF = 1e5
ans = INF
for i in range(3): # 첫 집의 색 i 
	dp = [[INF, INF, INF] for _ in range(n)]
	dp[0][i] = cost[0][i]
	for j in range(1, n):
		dp[j][0] = min(dp[j-1][1], dp[j-1][2]) + cost[j][0]
		dp[j][1] = min(dp[j-1][0], dp[j-1][2]) + cost[j][1]
		dp[j][2] = min(dp[j-1][0], dp[j-1][1]) + cost[j][2]
	for j in range(3):
		if i != j: # 첫 집의 색과 마지막 집의 색이 다를 경우에만 
			ans = min(ans, dp[n-1][j]) # 최소 비용 갱신 
print(ans)
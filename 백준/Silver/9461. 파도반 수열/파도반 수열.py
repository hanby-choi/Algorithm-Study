import sys 
input = sys.stdin.readline

def calc(n):
	dp = [0, 1, 1, 1, 2, 2]
	for i in range(6, n+1):
		dp.append(dp[i-1] + dp[i-5])
	return dp[n]

t = int(input())
while t:
	n = int(input())
	print(calc(n))	
	t -= 1
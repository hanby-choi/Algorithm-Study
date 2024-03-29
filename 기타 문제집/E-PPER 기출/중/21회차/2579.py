# 계단 오르기: DP
import sys
input = sys.stdin.readline
n = int(input())
score = [int(input()) for _ in range(n)]
def solution(n, score):
    if n == 1:
        return score[0]
    elif n == 2:
        return score[0]+score[1]
    dp = [0] * n
    dp[0] = score[0]
    dp[1] = score[0] + score[1]
    dp[2] = max(score[0], score[1]) + score[2]
    for i in range(3, n):
        dp[i] = max(dp[i-2], dp[i-3] + score[i-1]) + score[i]
    return dp[n-1]
print(solution(n, score))

"""def solution(n, stair):
    if n == 1:
        return stair[0]
    elif n == 2:
        return stair[0] + stair[1]
    dp = [0] * (n+1)
    dp[1] = stair[0]
    dp[2] = stair[0] + stair[1]
    for i in range(3, n+1):
        dp[i] = max(dp[i-2], dp[i-3] + stair[i-1]) + stair[i-1]
    return dp[n]"""
# 다이나믹 프로그래밍: 실전 문제 1 1로 만들기
import sys
input = sys.stdin.readline
X = int(input())
dp = [0] * 30001
for i in range(2, X+1):
    dp[i] = dp[i-1] + 1 # 현재 수에서 1을 빼는 경우: 1 작은 수의 최소 연산 횟수 + 1
    if i % 2 == 0: # 2로 나뉘는 경우
        dp[i] = min(dp[i], dp[i//2] + 1)
    if i % 3 == 0: # 3으로 나뉘는 경우
        dp[i] = min(dp[i], dp[i//3] + 1)
    if i % 5 == 0: # 5로 나뉘는 경우
        dp[i] = min(dp[i], dp[i//5] + 1)
print(dp[X])
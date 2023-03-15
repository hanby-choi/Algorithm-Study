# 다이나믹 프로그래밍: 실전 문제 4 효율적인 화폐 구성
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
money = []
for i in range(N):
    money.append(int(input().rstrip()))
money.sort()
d = [10001] * 10001
for i in money:
    d[i] = 1
for i in range(1, M+1):
    for j in money:
        if (i - j) > 0:
            d[i] = min(d[i], d[i-j] + 1)
if d[M] == 10001:
    print(-1)
else:
    print(d[M])
"""
d[0] = 0
for i in range(N): # 모든 money에 대해
    for j in range(money[i], M+1): # money[i]부터 M까지의 j원을 만드는 방법
        if d[j-money[i]] != 10001: # i-k원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j], d[j - money[i] + 1])
"""
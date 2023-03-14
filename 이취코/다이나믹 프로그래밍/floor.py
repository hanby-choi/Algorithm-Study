# 다이나믹 프로그래밍: 실전 문제 3 바닥 공사
import sys
input = sys.stdin.readline
N = int(input())
d = [0] * (N+1)
d[1] = 1; d[2] = 3
for i in range(3, N+1):
    d[i] = d[i-2]*2 + d[i-1]
print(d[N] % 796796)
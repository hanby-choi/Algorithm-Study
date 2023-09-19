# 백트래킹: 15649 N과 M(1)
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
num = [0] * M
check = [False for _ in range(N+1)]
def backtracking(cnt):
    if cnt == M:
        print(*num)
        return
    for i in range(1, N+1):
        if not check[i]:
            num[cnt] = i
            check[i] = True
            backtracking(cnt+1)
            check[i] = False
backtracking(0)
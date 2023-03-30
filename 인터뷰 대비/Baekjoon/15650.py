# 백트래킹: 15650 N과 M(2)
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
num = [0] * M
def backtracking(cnt):
    if cnt == M:
        print(*num)
        return
    for i in range(num[cnt-1] + 1, N+1): # 직전 인덱스보다 큰 원소만 탐색 -> 방문 체크 배열 필요 없음 (범위가 중복되지 않기 때문)
        num[cnt] = i
        backtracking(cnt+1)
backtracking(0)
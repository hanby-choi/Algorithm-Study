# 다이나믹 프로그래밍: 실전 문제 4 효율적인 화폐 구성
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
money = []
for i in range(N):
    money.append(int(input().rstrip()))

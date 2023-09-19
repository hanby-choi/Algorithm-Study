# 그리디: 숫자 카드 게임
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
card = []; min_arr = []
for i in range(N):
    card.append(list(map(int, input().split())))
    min_arr.append(min(card[i]))
print(max(min_arr))
"""
result = 0
for i in range(N):
    data = list(map(int, input().split()))
    result = max(min(data), result)
print(result)
"""
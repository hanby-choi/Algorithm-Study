# 구현: 실전 문제 1 왕실의 나이트
import sys
input = sys.stdin.readline
knight = input().rstrip()
x = int(knight[1])
y = int(ord(knight[0] - int(ord('a')))) + 1
steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (1, -2), (-1, 2), (1, 2)]
cnt = 0
for s in steps:
    if 1 <= (x + s[0]) <= 8 and 1 <= (y + s[1]) <= 8:
        cnt += 1
print(cnt)
"""
dx = [-2, -2, 2, 2, -1, 1, -1, 1]
dy = [-1, 1, -1, 1, -2, -2, 2, 2]
for i in range(8):
    if 1 <= (x + dx[i]) <= 8 and 1 <= (y + dy[i]) <= 8:
        cnt += 1
"""
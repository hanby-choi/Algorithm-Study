# 바닥 장식: DFS
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
floor = []
for i in range(n):
    floor.append(list(input().rstrip()))
def dfs(x, y, last):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if floor[x][y] == '-' and last == '-':
        floor[x][y] = 0
        dfs(x, y+1, '-')
        return True
    elif floor[x][y] == '|' and last == '|':
        floor[x][y] = 0
        dfs(x+1, y, '|')
        return True
    return False
cnt = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j, floor[i][j]):
            cnt += 1
print(cnt)
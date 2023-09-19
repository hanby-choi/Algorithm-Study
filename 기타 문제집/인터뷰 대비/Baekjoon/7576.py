# DFS & BFS: 7576 토마토
import sys
from collections import deque
input = sys.stdin.readline
m, n = map(int, input().split())
tomato = []
for _ in range(n):
    tomato.append(list(map(int, input().split())))
dx = [0, 0, 1, -1] # 상 하 좌 우
dy = [1, -1, 0, 0]
# bfs를 써야할 것 같고 ... 모든 토마토를 방문한다는 소리니까 visit 대신 tomato max값 출력
# 모든 방문이 끝났는데도 0이 있으면 -1, 저장될 때부터 모든 토마토가 익어 있으면(0이 없으면) 1 출력
start = []
already = True
for i in range(n):
    if already and 0 in tomato[i]:
        already = False
    for j in range(m):
        if tomato[i][j] == 1:
            start.append((i, j))
def findMinDays(tomato):
    if already:
        return 0
    queue = deque(start)
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if (0 <= nx < n) and (0 <= ny < m) and tomato[nx][ny] == 0:
                tomato[nx][ny] = tomato[x][y] + 1
                queue.append((nx, ny))
    min_days = 0
    for i in range(n):
        if 0 in tomato[i]:
            return -1
        min_days = max(min_days, max(tomato[i]))
    return min_days - 1 # 처음 시작이 1이었으므로 1을 빼줌
print(findMinDays(tomato))  
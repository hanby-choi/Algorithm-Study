import sys
from collections import deque
input = sys.stdin.readline

def bfs(tomato):
	dx = [-1, 1, 0, 0]
	dy = [0, 0, -1, 1]
	q = deque()
	no_tomato = True
	for i in range(n):
		for j in range(m):
			if tomato[i][j] == 1:
				q.append((i, j))
			elif tomato[i][j] == 0:
				no_tomato = False
	if no_tomato:
		return 0
	while q:
		x, y = q.popleft()
		for i in range(4):
			nx, ny = dx[i] + x, dy[i] + y
			if 0 <= nx < n and 0 <= ny < m and tomato[nx][ny] == 0:
				tomato[nx][ny] = tomato[x][y] + 1
				q.append((nx, ny))
	res = 0
	for i in range(n):
		for j in range(m):
			if tomato[i][j] == 0:
				return -1
		res = max(res, max(tomato[i]))
	return res-1
m, n = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(n)]
print(bfs(tomato))

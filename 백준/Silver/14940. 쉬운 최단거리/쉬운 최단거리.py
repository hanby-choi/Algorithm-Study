import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1 for _ in range(m)] for _ in range(n)]

def BFS(i, j):
	dx = [0, 0, -1, 1] # 상하
	dy = [-1, 1, 0, 0] # 좌우 	
	queue = deque([(i, j)])
	visited[i][j] = 0
	while queue:
		x, y = queue.popleft()
		for i in range(4):
			nx = dx[i] + x
			ny = dy[i] + y
			if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1:
				if graph[nx][ny] == 0:
					visited[nx][ny] = 0
				elif graph[nx][ny] == 1:
					queue.append((nx, ny))
					visited[nx][ny] = visited[x][y] + 1

for i in range(n):
	for j in range(m):
		if graph[i][j] == 2:
			BFS(i, j)

for i in range(n):
	for j in range(m):
		if graph[i][j] == 0:
			print(0, end=' ')
		else:
			print(visited[i][j], end=' ')
	print()
import sys
input = sys.stdin.readline
from collections import deque

def bfs(graph, sx, sy, dist):
	dx = [-1, 1, 0, 0]
	dy = [0, 0, -1, 1]
	q = deque([(sx, sy)])
	dist[sx][sy] = 1
	while q:
		x, y = q.popleft()
		for i in range(4):
			nx, ny = dx[i] + x, dy[i] + y
			if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == '1' and dist[nx][ny] == -1:
				q.append((nx, ny))
				dist[nx][ny] = dist[x][y] + 1

n, m = map(int, input().split())
graph = [input().rstrip() for _ in range(n)]
dist = [[-1] * m for _ in range(n)]
bfs(graph, 0, 0, dist)
print(dist[n-1][m-1])
import sys
from collections import deque
input = sys.stdin.readline

def BFS(graph, v, visited):
	dx = [-1, 1, 0, 0]
	dy = [0, 0, -1, 1]
	q = deque([v])
	visited[v[1]][v[0]] = 0
	while q:
		x, y = q.popleft()
		for i in range(4):
			nx, ny = dx[i] + x, dy[i] + y
			if 0 <= nx < m and 0 <= ny < n and visited[ny][nx] > (visited[y][x] + int(graph[ny][nx])):
				q.append((nx, ny))
				visited[ny][nx] = min(visited[ny][nx], visited[y][x] + int(graph[ny][nx]))

m, n = map(int, input().split())
graph = [input().rstrip() for _ in range(n)]
visited = [[1e5 for _ in range(m)] for _ in range(n)]
BFS(graph, (0, 0), visited)
print(visited[n-1][m-1])
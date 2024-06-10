import sys
input = sys.stdin.readline
from collections import deque

def bfs(graph, visited, r, c, w, h):
	dx = [-1, 1, 0, 0, -1, -1, 1, 1]
	dy = [0, 0, -1, 1, -1, 1, -1, 1]
	q = deque([(r, c)])
	visited[r][c] = True
	while q:
		x, y = q.popleft()
		for i in range(8):
			nx, ny = x + dx[i], y + dy[i]
			if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1 and not visited[nx][ny]:
				visited[nx][ny] = True
				q.append((nx, ny))
	return 

while True:
	w, h = map(int, input().split())
	if w == 0 and h == 0:
		break
	graph = [list(map(int, input().split())) for _ in range(h)]
	visited = [[False] * w for _ in range(h)]
	cnt = 0
	for r in range(h):
		for c in range(w):
			if graph[r][c] == 1 and not visited[r][c]:
				bfs(graph, visited, r, c, w, h)
				cnt += 1
	print(cnt)
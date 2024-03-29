import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph, i, j):
	q = deque([(i, j)])
	graph[i][j] = 0
	cnt = 1
	while q:
		x, y = q.popleft()
		for i in range(4):
			nx, ny = dx[i] + x, dy[i] + y
			if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
				q.append((nx, ny))
				graph[nx][ny] = 0
				cnt += 1
	return cnt

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
total_cnt = max_cnt = 0
for i in range(n):
	for j in range(m):
		if graph[i][j] == 1:
			temp = bfs(graph, i, j)
			max_cnt = max(temp, max_cnt)
			total_cnt += 1
print(total_cnt)
print(max_cnt)
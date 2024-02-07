import sys
from collections import deque
input = sys.stdin.readline

def BFS(graph, sx, sy, visited):
	dx = [0, 0, -1, 1]
	dy = [-1, 1, 0, 0]
	queue = deque([(sx, sy)])
	visited[sy][sx] = True
	cnt = 0
	while queue:
		x, y = queue.popleft()
		for i in range(4):
			nx, ny = dx[i] + x, dy[i] + y
			if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx]: # 갈 수 있는 범위의 아직 방문하지 않은 블록일 때
				if graph[ny][nx] == 'O' or graph[ny][nx] == 'P': # 빈 공간 또는 사람이면
					queue.append((nx, ny))
				if graph[ny][nx] == 'P': # 사람이면 cnt 증가
					cnt += 1
				visited[ny][nx] = True 
	return cnt if cnt > 0 else 'TT'

n, m = map(int, input().split())
graph = [input().rstrip() for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
for i in range(n):
	for j in range(m):
		if graph[i][j] == 'I':
			print(BFS(graph, j, i, visited))
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def DFS(graph, x, y):
	graph[y][x] = 0
	for i in range(4):
		nx = dx[i] + x
		ny = dy[i] + y
		if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == 1:
			 DFS(graph, nx, ny)

t = int(input())
while t:
	m, n, k = map(int, input().split())
	graph = [[0 for _ in range(m)] for _ in range(n)]
	for _ in range(k):
		x, y = map(int, input().split())
		graph[y][x] = 1
	cnt = 0
	for i in range(n):
		for j in range(m):
			if graph[i][j] == 1:
				cnt += 1
				DFS(graph, j, i)
	print(cnt)
	t -= 1
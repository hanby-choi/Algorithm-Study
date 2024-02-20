import sys
from collections import deque
input = sys.stdin.readline

def find_tomato():
	no_tomato = True
	for z in range(h):
		for r in range(n):
			for c in range(m): 
				if tomato[z][r][c] == 1:
					q.append((z, r, c))
				elif tomato[z][r][c] == 0:
					no_tomato = False
	return no_tomato

def bfs():
	dx = [-1, 1, 0, 0, 0, 0]
	dy = [0, 0, -1, 1, 0, 0]
	dz = [0, 0, 0, 0, -1, 1]
	while q:
		z, x, y = q.popleft()
		for i in range(6):
			nz, nx, ny = dz[i] + z, dx[i] + x, dy[i] + y
			if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h and tomato[nz][nx][ny] == 0:
				tomato[nz][nx][ny] = tomato[z][x][y] + 1
				q.append((nz, nx, ny))
	ans = 0
	for z in range(h):
		for r in range(n):
			for c in range(m): 
				if tomato[z][r][c] == 0:
					return -1
				if ans < tomato[z][r][c]:
					ans = tomato[z][r][c]
	return ans - 1 

m, n, h = map(int, input().split())
tomato = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
q = deque()
if find_tomato():
	print(0)
else:
	print(bfs())
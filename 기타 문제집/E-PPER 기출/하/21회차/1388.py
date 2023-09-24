"""# 바닥 장식: DFS
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
floor = []
for i in range(n):
    floor.append(list(input().rstrip()))
def dfs(x, y, last):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if floor[x][y] == '-' and last == '-':
        floor[x][y] = 0
        dfs(x, y+1, '-')
        return True
    elif floor[x][y] == '|' and last == '|':
        floor[x][y] = 0
        dfs(x+1, y, '|')
        return True
    return False
cnt = 0
for i in range(n):
    for j in range(m):
        if floor[i][j] != 0:
            if dfs(i, j, floor[i][j]):
                cnt += 1
print(cnt)"""
"""
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
floor = []
for i in range(n):
    floor.append(list(input().rstrip()))
def dfs(x, y, n, m, floor, visited):
	visited[x][y] = True
	if floor[x][y] == '-':
		nx = x
		ny = y + 1
	elif floor[x][y] == '|':
		nx = x + 1
		ny = y
	if 0 <= nx < n and 0 <= ny < m and floor[x][y] == floor[nx][ny] and not visited[nx][ny]:
		dfs(nx, ny, n, m, floor, visited)

def solution(n, m, floor):
	visited = [[False for _ in range(m)] for _ in range(n)]
	ans = 0
	for i in range(n):
		for j in range(m):
			if not visited[i][j]:
				dfs(i, j, n, m, floor, visited)
				ans += 1
	return ans
print(solution(n, m, floor))
"""
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
floor = []
for i in range(n):
    floor.append(list(input().rstrip()))

"""def dfs(x, y, last, n, m, floor):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if floor[x][y] == '-' == last:
        floor[x][y] = 0
        dfs(x, y+1, '-', n, m, floor)
        return True
    elif floor[x][y] == '|' == last:
        floor[x][y] = 0
        dfs(x+1, y, '|', n, m, floor)
        return True
    return False

def solution(n, m, floor):
    ans = 0
    for i in range(n):
        for j in range(m):
            if floor[i][j] != 0:
                if dfs(i, j, floor[i][j], n, m, floor):
                    ans += 1
    return ans"""

def dfs(n, m, x, y, floor, visited):
    visited[x][y] = True
    nx, ny = x, y
    if floor[x][y] == '-':
        ny = y+1
    elif floor[x][y] == '|':
        nx = x+1
    if 0<=nx<n and 0<=ny<m and floor[x][y] == floor[nx][ny] and not visited[nx][ny]:
        dfs(n, m, nx, ny, floor, visited)

def solution(n, m, floor):
    visited = [[False]*(m) for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                dfs(n, m, i, j, floor, visited)
                ans += 1
    return ans

print(solution(n, m, floor))
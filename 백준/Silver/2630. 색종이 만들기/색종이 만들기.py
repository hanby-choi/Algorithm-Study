import sys
sys.setrecursionlimit(10 ** 7) 
input = sys.stdin.readline

def sol(r, c, n): 
	color = graph[r][c]
	half = n // 2
	for i in range(r, r+n):
		for j in range(c, c+n):
			if color != graph[i][j]:
				sol(r, c, half)
				sol(r, c + half, half)
				sol(r + half, c, half)
				sol(r + half, c + half, half)
				return
	if color == 0:
		cnt[0] += 1
	else:
		cnt[1] += 1
	
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
cnt = [0, 0]
sol(0, 0, n)
print(cnt[0])
print(cnt[1])
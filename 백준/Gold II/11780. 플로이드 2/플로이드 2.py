import sys
input = sys.stdin.readline

def floyd_warshall(n, graph, nxt):
	for k in range(1, n+1):
		for a in range(1, n+1):
			for b in range(1, n+1):
				if graph[a][b] > graph[a][k] + graph[k][b]:
					graph[a][b] = graph[a][k] + graph[k][b]
					nxt[a][b] = nxt[a][k]

n = int(input())
m = int(input())
graph = [[1e7] * (n+1) for _ in range(n+1)]
nxt = [[0] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
	graph[i][i] = 0
for _ in range(m):
	a, b, c = map(int, input().split())
	graph[a][b] = min(graph[a][b], c)
	nxt[a][b] = b
floyd_warshall(n, graph, nxt)

for i in range(1, n+1):
	for j in range(1, n+1):
		print(0, end=' ') if graph[i][j] == 1e7 else print(graph[i][j], end=' ')
	print()

for i in range(1, n+1):
	for j in range(1, n+1):
		if graph[i][j] == 0 or graph[i][j] == 1e7:
			print(0)
			continue
		path = []
		start = i
		while start != j:
			path.append(start)
			start = nxt[start][j]
		path.append(j)
		print(len(path), *path)
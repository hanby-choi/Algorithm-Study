import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

def DFS(graph, v, visited):
	visited[v] = True
	for i in graph[v]:
		if not visited[i]:
			DFS(graph, i, visited)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)] 
visited = [False] * (n+1) 
for _ in range(m):
	u, v = map(int, input().split())
	graph[u].append(v)
	graph[v].append(u)

cnt = 0
for i in range(1, n+1):
	if not visited[i]:
		DFS(graph, i, visited)
		cnt += 1
print(cnt)
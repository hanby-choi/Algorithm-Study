import sys
from collections import deque
input = sys.stdin.readline

def BFS(graph, start, visited):
	queue = deque([start])
	while queue:
		v = queue.popleft()
		for i in graph[v]:
			if not visited[i]:
				queue.append(i)
				visited[i] = True

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
		BFS(graph, i, visited)
		cnt += 1
print(cnt)
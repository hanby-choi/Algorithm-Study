import sys
from collections import deque
input = sys.stdin.readline

def BFS(start):
	queue = deque([start])
	distance[start] = 0
	while queue:
		v = queue.popleft()
		for i in graph[v]:
			cost = distance[v] + 1
			if distance[i] > cost:
				distance[i] = cost
				queue.append(i)

INF = 1e5
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
	a, b = map(int, input().split())
	graph[a].append(b)
distance = [INF] * (n+1)
BFS(x)

is_answer = False
for i in range(1, n+1):
	if distance[i] == k:
		print(i)
		is_answer = True
if not is_answer:
	print(-1)
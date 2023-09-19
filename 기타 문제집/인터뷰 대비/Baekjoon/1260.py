# DFS & BFS: 1260 DFS와 BFS
import sys
from collections import deque
input = sys.stdin.readline
n, m, v = map(int, input().split())
graph = [[False] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

def DFS(graph, v, visited):
    visited[v] = True
    print(v, end = ' ')
    for i in range(1, n+1):
        if not visited[i] and graph[v][i]:
            DFS(graph, i, visited)

def BFS(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        for i in range(1, n+1):
            if not visited[i] and graph[v][i]:
                queue.append(i)
                visited[i] = True

visited = [False] * (n+1)
DFS(graph, v, visited)
print()
visited = [False] * (n+1)
BFS(graph, v, visited)
# DFS & BFS: 2606 바이러스
import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
m = int(input())
visited = [False] * (n+1)
""" 인접 리스트
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def DFS(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            DFS(graph, i, visited)

def BFS(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True """
# 인접 행렬
graph = [[False] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

def DFS(graph, v, visited):
    visited[v] = True
    for i in range(1, n+1):
        if not visited[i] and graph[v][i]:
            DFS(graph, i, visited)

DFS(graph, 1, visited)
#BFS(graph, 1, visited)
print(visited.count(True) - 1) # remove computer 1 from cnt
# DFS & BFS: 실전 문제 2 미로 탈출
import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().rstrip())))
dx = [-1, 1, 0, 0] # 상 하 좌 우
dy = [0, 0, -1, 1]
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1: # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    print(graph)
    return graph[n-1][m-1]
print(bfs(0, 0))
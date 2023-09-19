# 최단 경로: 실전 문제 2 전보
import sys, heapq
input = sys.stdin.readline
INF = 1e9
n, m, c = map(int, input().split())
graph = [[] for i in range(n+1)] # 각 노드에 연결된 노드에 대한 정보
distance = [INF] * (n+1)
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[c] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
dijkstra(c)
count = 0; max_distance = 0
for dist in distance:
    if dist != INF:
        count += 1
        max_distance = max(max_distance, dist)
print(count-1, max_distance) # 시작 노드는 제외
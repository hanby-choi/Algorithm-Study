import sys, heapq
input = sys.stdin.readline

def dijkstra(start):
	q = []
	heapq.heappush(q, (0, start))
	distance[start] = 0
	while q:
		dist, now = heapq.heappop(q)
		if distance[now] >= dist:
			for i in graph[now]:
				cost = dist + i[1] # k에서 now를 경유해서 i로 가는 cost
				if cost < distance[i[0]]: # cost가 현재 저장된 i로 가는 distance보다 작다면
					distance[i[0]] = cost # 값 갱신
					heapq.heappush(q, (cost, i[0])) 

INF = int(1e6)
V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V+1)]
for _ in range(E):
	u, v, w = map(int, input().split())
	graph[u].append((v, w)) # (도착 노드, 가중치)
distance = [INF] * (V+1)
dijkstra(K)
for i in range(1, V+1):
	print(distance[i]) if distance[i] != INF else print('INF')
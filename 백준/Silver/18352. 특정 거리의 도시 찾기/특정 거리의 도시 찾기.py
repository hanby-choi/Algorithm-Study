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
				cost = dist + i[1]
				if cost < distance[i[0]]:
					distance[i[0]] = cost
					heapq.heappush(q, (cost, i[0]))

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
	a, b = map(int, input().split())
	graph[a].append((b, 1))
distance = [1e5] * (n+1)
dijkstra(x)

is_answer = False
for i in range(1, n+1):
	if distance[i] == k:
		print(i)
		is_answer = True
if not is_answer:
	print(-1)
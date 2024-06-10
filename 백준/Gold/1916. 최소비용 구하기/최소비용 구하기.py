import sys, heapq
input = sys.stdin.readline

def djikstra(start):
	q = []
	heapq.heappush(q, (0, start))
	cost[start] = 0
	while q:
		c, v = heapq.heappop(q)
		if c <= cost[v]:
			for i in graph[v]:
				new_cost = c + i[1] # A에서 v를 경유해서 i로 가는 cost
				if new_cost < cost[i[0]]: # 기존에 i로 가는 cost보다 새로 구한 비용이 작으면
					cost[i[0]] = new_cost # 갱신 
					heapq.heappush(q, (new_cost, i[0]))

n = int(input())
m = int(input())
graph = [[] for i in range(n+1)]
cost = [1e9] * (n+1)
for _ in range(m):
	a, b, c = map(int, input().split())
	graph[a].append((b, c)) # 도착 도시, 비용
A, B = map(int, input().split())
djikstra(A)
print(cost[B])
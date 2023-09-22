import sys
from collections import deque
input = sys.stdin.readline

def bfs(n, k, visited):
	queue = deque([n])
	while queue:
		v = queue.popleft()
		if v == k:
			return visited[v]
		for next_v in (v-1, v+1, 2*v):
			if 0 <= next_v <= MAX-1 and not visited[next_v]:
				visited[next_v] = visited[v] + 1
				queue.append(next_v)				
			
MAX = 100001
n, k = map(int, input().split())
visited = [0] * MAX
print(bfs(n, k, visited))
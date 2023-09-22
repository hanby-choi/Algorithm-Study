import sys, heapq
input = sys.stdin.readline
n = int(input())
heap = []
for _ in range(n):
	cmd = int(input())
	if cmd != 0:
		heapq.heappush(heap, (abs(cmd), cmd))
	elif heap:
		print(heapq.heappop(heap)[1])
	else:
		print(0)
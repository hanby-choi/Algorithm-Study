import sys, heapq
input = sys.stdin.readline
heap = []
n = int(input())
for _ in range(n):
	cmd = int(input())
	if cmd != 0:
		heapq.heappush(heap, -cmd)
	elif heap:
		print(-1 * heapq.heappop(heap))
	else:
		print(0)
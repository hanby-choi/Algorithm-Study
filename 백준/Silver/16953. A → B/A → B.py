import sys, math
from collections import deque 
input = sys.stdin.readline

def BFS(a, b):
	queue = deque([a])
	cnt = length = 1
	while True:
		new_queue = deque([])
		while queue:
			v = queue.popleft()
			v1, v2 = v * 2, v * 10 + 1
			if v1 == b or v2 == b:
				return cnt + 1
			if (length - 1) == len(queue) and v1 > b:
				return -1
			if v1 < b:
				new_queue.append(v1)
			if v2 < b:	 
				new_queue.append(v2)
		queue = new_queue
		length = len(queue)
		cnt += 1

a, b = map(int, input().split())
print(BFS(a, b))
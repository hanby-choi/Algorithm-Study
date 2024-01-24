import sys
input = sys.stdin.readline
from collections import deque
t = int(input())
deq = deque()
while t > 0:
	cmd = input().split()
	if len(cmd) == 1:
		if cmd[0] == 'size':
			print(len(deq))
		elif cmd[0] == 'empty':
			print(1) if len(deq) == 0 else print(0)
		elif len(deq) == 0:
			print(-1)
		else:
			if cmd[0] == 'front':
				print(deq[0])
			elif cmd[0] == 'back':
				print(deq[-1])
			elif cmd[0] == 'pop_front':
				print(deq.popleft())
			elif cmd[0] == 'pop_back':
				print(deq.pop())
	else:
		if cmd[0] == 'push_back':
			deq.append(cmd[1])
		else:
			deq.appendleft(cmd[1])
	t -= 1
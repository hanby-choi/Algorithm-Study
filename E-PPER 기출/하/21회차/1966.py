# 프린터 큐: 구현, 큐
import sys
from collections import deque 
input = sys.stdin.readline
T = int(input())
for _ in range(T):
	n, m = map(int, input().split())
	priority = list(map(int, input().split()))
	q = deque(priority)
	cnt = 0
	priority.sort()
	while True: 
		if q[0] == priority[-1]: # 큐의 가장 앞에 있는 원소가 중요도가 가장 높은 문서일 때
			cnt += 1
			q.popleft()
			priority.pop()
			if m == 0:
				break
		else:
			q.append(q.popleft())
		m = len(q) - 1 if m == 0 else m - 1
	print(cnt)
"""for _ in range(T):
	n, m = map(int, input().split())
	priority = list(map(int, input().split()))
	q = deque([(priority[i], i) for i in range(n)])
	cnt = 0
	while q:
		flag = False
		for i in range(len(q)):
			if q[0][0] < q[i][0]:
				q.append(q.popleft())
				flag = True
				break
		if not flag:
			res = q.popleft()
			cnt += 1
			if res[1] == m:
				print(cnt)
				break	"""
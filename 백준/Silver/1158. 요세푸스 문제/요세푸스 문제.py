import sys
from collections import deque 
input = sys.stdin.readline
n, k = map(int, input().split())
arr = deque([i + 1 for i in range(n)])
ans = []
while arr:
	for i in range(k-1):
		arr.append(arr.popleft())
	ans.append(str(arr.popleft()))
print('<', end='')
print(', '.join(ans), end ='')
print('>')	
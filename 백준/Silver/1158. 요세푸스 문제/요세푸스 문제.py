import sys
input = sys.stdin.readline
n, k = map(int, input().split())
arr = [i + 1 for i in range(n)]
index = 0
ans = []
while arr: # for i in range(n)로도 가능
	index = (index + k-1) % len(arr) 
	ans.append(str(arr.pop(index)))
print('<', ', '.join(ans), '>', sep='')
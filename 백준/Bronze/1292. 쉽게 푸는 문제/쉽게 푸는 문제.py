import sys
input = sys.stdin.readline
arr = [0]
for i in range(1, 150):
	arr += [i] * i
a, b = map(int, input().split())
print(sum(arr[a:b+1]))
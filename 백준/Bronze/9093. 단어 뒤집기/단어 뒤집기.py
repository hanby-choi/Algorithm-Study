import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
	line = list(input().split())
	for word in line:
		print(word[::-1], end=' ')
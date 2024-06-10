import sys
input = sys.stdin.readline
n = int(input())
info = [tuple(map(int, input().split())) for _ in range(n)]
rank = [1] * n
for i in range(n-1):
	for j in range(i+1, n):
		if info[i][0] > info[j][0] and info[i][1] > info[j][1]:
			rank[j] += 1
		elif info[i][0] < info[j][0] and info[i][1] < info[j][1]:
			rank[i] += 1
print(*rank)
import sys
input = sys.stdin.readline
s1, s2 = input().rstrip(), input().rstrip()
l1, l2 = len(s1), len(s2)
cache = [[0] * (l2 + 1) for _ in range(l1 + 1)]
for i in range(1, l1 + 1):
	for j in range(1, l2 + 1):
			if s1[i-1] == s2[j-1]:
				cache[i][j] = cache[i-1][j-1] + 1
			else:
				cache[i][j] = max(cache[i][j-1], cache[i-1][j])
print(cache[-1][-1])
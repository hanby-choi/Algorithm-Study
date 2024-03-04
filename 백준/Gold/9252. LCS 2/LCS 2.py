import sys
input = sys.stdin.readline
s1, s2 = input().rstrip(), input().rstrip()
l1, l2 = len(s1), len(s2)
cache = [[""] * (l2 + 1) for _ in range(l1 + 1)]
for i in range(1, l1 + 1):
	for j in range(1, l2 + 1):
			if s1[i-1] == s2[j-1]:
				cache[i][j] = cache[i-1][j-1] + s1[i-1]
			else:
				if len(cache[i-1][j]) >= len(cache[i][j-1]):
					cache[i][j] = cache[i-1][j]
				else:
					cache[i][j] = cache[i][j-1]
result = cache[-1][-1]
print(len(result), result, sep='\n')
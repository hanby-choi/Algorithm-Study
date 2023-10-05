import sys
input = sys.stdin.readline
m = int(input())
n = int(input())
def sieve(n):
	decimal = [True] * (n+1)
	decimal[0] = decimal[1] = False
	for i in range(2, int(n ** 0.5) + 1):
		if decimal[i]:
			for j in range(i*2, n+1, i):
				decimal[j] = False
	return decimal
dec = sieve(n)
ans = []
for i in range(m, n+1):
	if dec[i]:
		ans.append(i)
if ans:
	print(sum(ans))
	print(min(ans))
else:
	print(-1)
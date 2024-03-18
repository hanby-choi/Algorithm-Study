import sys
input = sys.stdin.readline

def calc(cur, food, n):
	sour, bitter = 1, 0
	for i in range(n):
		if cur & (1 << i):
			sour *= food[i][0]
			bitter += food[i][1]
	return abs(sour - bitter)

n = int(input())
food = [tuple(map(int, input().split())) for _ in range(n)]
ans = 1e12
for c in range(1, 1 << n):
	ans = min(ans, calc(c, food, n))
print(ans)
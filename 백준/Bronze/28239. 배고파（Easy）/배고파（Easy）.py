import sys
input = sys.stdin.readline
MAX = 60
def find(m):
	# 제곱수인 경우 (1이 하나) 
	for i in range(1, MAX):
		if m == (1 << i):
			return (i-1, i-1)
	# 제곱수가 아닌 경우
	for x in range(0, MAX):
		if m & (1 << x):
			m -= (1 << x)
			break
	for y in range(x+1, MAX):
		if m & (1 << y):
			break
	return (x, y)

n = int(input())
while n:
	m = int(input())
	print(*find(m))
	n -= 1
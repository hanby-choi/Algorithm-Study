import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7) 

def find(n, r, c):
	if n == 0:
		return 0
	half = 2 ** (n-1)
	if 0 <= r < half and 0 <= c < half:
		return find(n-1, r, c)
	elif 0 <= r < half and half <= c < half * 2:
		return half * half + find(n-1, r, c-half)
	elif half <= r < half * 2 and 0 <= c < half:
		return 2 * half * half + find(n-1, r-half, c)
	else:
		return 3 * half * half + find(n-1, r-half, c-half)

n, r, c = map(int, input().split())
print(find(n, r, c))
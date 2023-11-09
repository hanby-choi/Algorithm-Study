import sys
input = sys.stdin.readline

def convert(n, b):
	arr = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	ans = ''
	while n:
		ans += arr[n % b]
		n //= b
	return ans[::-1]

n, b = map(int, input().split())
print(convert(n, b))
import sys
input = sys.stdin.readline
s = int(input())
now = 0
for i in range(1, s+1):
	now += i
	if now > s:
		print(i-1)
		break
	elif now == s:
		print(i)
		break
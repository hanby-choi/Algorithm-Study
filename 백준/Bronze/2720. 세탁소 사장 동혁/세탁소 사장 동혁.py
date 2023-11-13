import sys
input = sys.stdin.readline
t = int(input())
coin = [25, 10, 5, 1]
for i in range(t):
	change = int(input())
	cnt = []
	for c in coin:
		cnt.append(change // c)
		change %= c
	print(*cnt)
import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
	n = int(input())
	binary = str(bin(n))[::-1]
	for i, b in enumerate(binary):
		if b == '1':
			print(i, end=" ")
	print()
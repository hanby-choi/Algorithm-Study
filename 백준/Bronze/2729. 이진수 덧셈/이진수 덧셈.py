import sys
input = sys.stdin.readline
n = int(input())
for i in range(n):
	a, b = input().split()
	print(bin(int(a, 2) + int(b, 2))[2:])
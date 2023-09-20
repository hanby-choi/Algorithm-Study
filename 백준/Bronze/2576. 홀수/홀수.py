import sys
input = sys.stdin.readline
arr = [int(input()) for _ in range(7)]
odd = [a for a in arr if a % 2 == 1 ]
if not odd:
	print(-1)
else:
	print(sum(odd))
	print(min(odd))
import sys
input = sys.stdin.readline

def count(n):
	five = n // 5
	three = 0
	while five >= 0 and three >= 0:
		three = (n - five * 5) // 3
		if (five * 5 + three * 3) == n:
			return five + three
		five -= 1
	return -1

n = int(input())
print(count(n))
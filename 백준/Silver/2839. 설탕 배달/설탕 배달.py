import sys
input = sys.stdin.readline

def count(n):
	five = n // 5
	rest = n % 5
	three = 0
	while five >= 0 and three >= 0:
		three = rest // 3
		if rest % 3 == 0:
			return five + three
		five -= 1
		rest += 5
	return -1

n = int(input())
print(count(n))
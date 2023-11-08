import sys
input = sys.stdin.readline

def getDecimal(n, b):
	ans = 0
	length = len(n)
	for i in range(length):
		target = n[length-i-1]
		if target.isdigit():
			ans += int(target) * (b ** i)   
		else:
			ans += (ord(target) - ord('A') + 10) * (b ** i)
	return ans

n, b = input().split()
b = int(b)
print(getDecimal(n, b))
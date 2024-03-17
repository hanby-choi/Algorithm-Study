import sys
input = sys.stdin.readline
n = bin(int(input()))[2:]
ans = 0
for i in range(len(n)):
	if int(n[-i-1]):	
		ans += 3 ** i
print(ans)
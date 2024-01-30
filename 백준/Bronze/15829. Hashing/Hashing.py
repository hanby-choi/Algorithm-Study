import sys
input = sys.stdin.readline
L = int(input())
s = input().rstrip()
ans = 0
for i in range(L):
	ans += (ord(s[i]) - ord('a') + 1) * (31 ** i)
print(ans)
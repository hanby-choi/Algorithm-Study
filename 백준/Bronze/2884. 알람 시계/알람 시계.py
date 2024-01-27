import sys
input = sys.stdin.readline
h, m = map(int, input().split())
if (m - 45) >= 0:
	m -= 45
else:
	if h == 0:
		h = 23
	else:
		h -= 1
	m = m - 45 + 60 
print(h, m)
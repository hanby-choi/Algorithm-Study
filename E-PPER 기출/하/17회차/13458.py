# 시험 감독: 수학
import sys, math
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())
ans = 0
for i in a:
	if b >= i:
		ans += 1
	else:
		ans += math.ceil((i - b)/c) + 1
print(ans)
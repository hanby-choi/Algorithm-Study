# 스캐너 - 동적 배열
import sys
input = sys.stdin.readline
r, c, zr, zc = map(int, input().split())
arr = [input().rstrip() for _ in range(r)]
for i in range(r):
	ans = ['' for _ in range(r)]
	for j in range(c):
		ans[i] += arr[i][j] * zc
	for j in range(zr):
		print(ans[i])
import sys
input = sys.stdin.readline

def calc(visited, arr):
	start, link = 0, 0
	for i in range(n):
		for j in range(n):
			if visited & (1 << i) and visited & (1 << j):
				start += arr[i][j]
			elif not (visited & (1 << i)) and not (visited & (1 << j)):
				link += arr[i][j]
	return abs(start - link)			

def backtracking(visited, start, cur, cnt):
	global ans
	if cur == cnt:
		ans = min(ans, calc(visited, arr))
		return
	for i in range(start, n):
		if visited ^ (1 << i): # i번째 자리가 0일 때 - not visited
			visited |= (1 << i)
			backtracking(visited, i + 1, cur + 1, cnt)
			visited &= ~(1 << i)
	
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = 1e9
for i in range(1, n // 2 + 1):
	backtracking(0, 0, 0, i)
print(ans)
import sys
input = sys.stdin.readline

def findP(n, nums):
	is_p = [[0] * n for _ in range(n)]
	for i in range(n): # 길이가 1인 팰린드롬
		is_p[i][i] = 1
	for i in range(1, n): # 길이가 2인 팰린드롬 - 같은 수가 연속해서 나오는 경우
		if nums[i-1] == nums[i]:
			is_p[i-1][i] = 1
	for l in range(3, n+1): # 길이가 3부터 n인 팰린드롬
		for start in range(n - l + 1):
			end = start + l - 1
			if nums[start] == nums[end] and is_p[start + 1][end - 1]:
				is_p[start][end] = 1
	return is_p

n = int(input())
nums = list(map(int, input().split()))
is_p = findP(n, nums)
m = int(input())
for _ in range(m):
	s, e = map(int, input().split())
	print(is_p[s-1][e-1])
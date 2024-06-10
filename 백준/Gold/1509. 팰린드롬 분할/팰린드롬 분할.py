import sys
input = sys.stdin.readline
s = input().rstrip()
L = len(s)
is_p = [[0] * L for _ in range(L)]
dp = [2500] * (L + 1)
dp[-1] = 0
for i in range(L): # 길이가 1
	is_p[i][i] = 1
for i in range(1, L): # 길이가 2 -> aa, bb, ...
	if s[i-1] == s[i]:
		is_p[i-1][i] = 1
for l in range(3, L+1): # 길이가 3 ~ L
	for start in range(L - l + 1):
		end = start + l - 1
		if s[start] == s[end] and is_p[start + 1][end - 1] == 1:
			is_p[start][end] = 1
for end in range(L):
	for start in range(end + 1): # start는 end보다 작거나 같아야 함
		if is_p[start][end]:
			dp[end] = min(dp[end], dp[start - 1] + 1)
		else:
			dp[end] = min(dp[end], dp[end - 1] + 1)
print(dp[L-1])		
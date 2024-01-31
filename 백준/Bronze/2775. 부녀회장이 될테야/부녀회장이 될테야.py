import sys
input = sys.stdin.readline
arr = [[0 for _ in range(15)] for _ in range(15)]
for i in range(15):
	arr[0][i] = i
for i in range(1, 15): # 층수
	for j in range(1, 15): # 호수
		arr[i][j] += arr[i][j-1] + arr[i-1][j]
t = int(input())
while t:
	k = int(input())
	n = int(input())
	print(arr[k][n])
	t -= 1
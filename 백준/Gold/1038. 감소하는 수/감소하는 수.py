import sys
input = sys.stdin.readline

def backtracking(n, length, temp):
	global count
	if len(temp) == length:
		count += 1
		if count == n:
			for num in temp:
				print(num, end='')
			exit()
		return
	for i in range(0, 10):
		if len(temp) == 0 or temp[-1] > i:
			temp.append(i)
			backtracking(n, length, temp)
			temp.pop()

n = int(input())
count = -1
if n <= 9:
	print(n)
else:
	for i in range(1, 11): # 길이가 1~10인 수열 
		temp = []
		backtracking(n, i, temp)
	print(-1)
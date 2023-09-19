# OX 퀴즈: 단순 계산
import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
	string = input().rstrip()
	cnt = total = 0
	for i in string:
		if i == 'O':
			cnt += 1
			total += cnt
		else:
			cnt = 0
	print(total)
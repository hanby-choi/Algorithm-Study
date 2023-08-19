# 팰린드롬수 - 구현, 문자열
import sys
input = sys.stdin.readline
while True:
	num = input().rstrip()
	if num == '0':
		break
	reversed_num = num[::-1]
	print("yes") if reversed_num == num else print("no")
"""import sys
input = sys.stdin.readline
while True:
	num = input().rstrip()
	if num == '0':
		break
	flag = True
	n = len(num)
	for i in range(0, n//2):
		if num[i] != num[n-1-i]:
			flag = False
			break
	print("yes") if flag else print("no")"""
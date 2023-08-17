# 괄호: 스택, 문자열
import sys
input = sys.stdin.readline
T = int(input())
for i in range(T):
	string = input().rstrip()
	stack = []
	valid = True
	for j in string:
		if j == '(':
			stack.append(j)
		else:
			if stack:
				stack.pop()
			else:
				valid = False
				break
	if stack:
		valid = False
	print('YES') if valid else print('NO')
# 쇠막대기 - 스택, 문자열
import sys
input = sys.stdin.readline
stick = input().rstrip()
stack = []
cnt = 0
for i in range(len(stick)):
	if stick[i] == '(':
		stack.append(stick[i])
	else: # stick[i] == ')'
		stack.pop()
		if stick[i-1] == '(':
			cnt += len(stack)
		else: # stick[i-1] == ')'
			cnt += 1
print(cnt) 
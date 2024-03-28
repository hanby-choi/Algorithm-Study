import sys
input = sys.stdin.readline

def solution(brackets):
	temp, ans = 1, 0
	stack = []
	for i, b in enumerate(brackets):
		if b == '(':
			stack.append(b)
			temp *= 2
		elif b == '[':
			stack.append(b)
			temp *= 3
		elif b == ')':
			if not stack or stack[-1] == '[':
				return 0
			if brackets[i-1] == '(':
				ans += temp
			stack.pop()
			temp //= 2
		else:
			if not stack or stack[-1] == '(':
				return 0
			if brackets[i-1] == '[':
				ans += temp
			stack.pop()
			temp //= 3
	if stack:
		return 0
	return ans

brackets = input().rstrip()
print(solution(brackets))
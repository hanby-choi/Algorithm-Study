# 문자열 압축: 구현, 문자열
import sys
def solution(src):
	ans = ''
	if src[0] == '1':
		ans += '1'
	flag = src[0]
	cnt = 0
	for c in src:
		if c == flag:
			cnt += 1
		else:
			flag = c
			ans += chr(ord('A') + cnt - 1)
			cnt = 1
	ans += chr(ord('A') + cnt - 1)
	return ans
src = sys.stdin.readline().rstrip()
print(solution(src))

def solution(src):
	ans = ''
	if src[0] == '1':
		ans += '1'
	cnt = 0
	for i in range(len(src)-1):
		if src[i] != src[i+1]:
			ans += chr(ord('A') + cnt)
			cnt = 0
		else:
			cnt += 1
	ans += chr(ord('A') + cnt)
	return ans 
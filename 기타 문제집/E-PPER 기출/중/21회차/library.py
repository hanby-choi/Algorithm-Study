# 도서관 예약: 그리디
import sys
input = sys.stdin.readline
n = int(input())
s = list(map(int, input().split()))
e = list(map(int, input().split()))
def solution(n, s, e):
	student = [(s[i], e[i]) for i in range(n)]
	student.sort(key = lambda x: (x[1], x[0]))
	e1 = e2 = -1
	ans = 0
	for st in student:
		if e1 <= st[0]:
			e1 = st[1]
			ans += 1
		elif e2 <= st[0]:
			e2 = e1
			e1 = st[1]
			ans += 1
	return ans
print(solution(n, s, e))

"""def solution(n, s, e):
	student = [(s[i], e[i]) for i in range(n)]
	student.sort(key=lambda x: x[1])
	e1 = e2 = ans = 0
	for st in student:
		if e1 <= st[0]:
			e1 = st[1]
			ans += 1
		elif e2 <= st[0]:
			e2 = e1
			e1 = st[1]
			ans += 1
	return ans"""
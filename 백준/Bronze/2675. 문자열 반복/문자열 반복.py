import sys
input = sys.stdin.readline
t = int(input())
while t > 0:
	r, sentence = input().split()
	r = int(r)
	ans = ''
	for s in sentence:
		ans += s * r
	print(ans)
	t -= 1
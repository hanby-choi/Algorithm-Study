import sys
input = sys.stdin.readline

def calcFloor(h, w, n):
	ans = ''
	# 층수 계산
	remain = n % h
	if remain == 0:
		ans += str(h)
		num = n // h
	else:
		ans += str(remain)
		num = n // h + 1
	# 호수 계산
	if num <= 9:
		ans += '0' + str(num)
	else:
		ans += str(num)
	return ans

t = int(input())
while t > 0:
	h, w, n = map(int, input().split())
	print(calcFloor(h, w, n))
	t -= 1
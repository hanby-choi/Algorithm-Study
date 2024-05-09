import sys
input = sys.stdin.readline

def countNum(length, stick):
	cnt = 0
	for s in stick:
		cnt += s // length
	return cnt
	
def binarySearch(m, stick):
	left, right = 1, max(stick)
	while left <= right:
		mid = (left + right) // 2
		cnt = countNum(mid, stick)
		if cnt >= m:
			left = mid + 1
		else:
			right = mid - 1
	return left - 1

m, n = map(int, input().split())
stick = list(map(int, input().split()))
print(binarySearch(m, stick))
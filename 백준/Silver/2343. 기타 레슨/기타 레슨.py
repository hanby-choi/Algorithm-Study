import sys
input = sys.stdin.readline

def countBluray(l, video):
	cnt, cur = 1, 0
	for v in video:
		if (cur + v) > l: # 현재 강의부터는 다음 블루레이에 넣어야 할 때 
			cnt += 1
			cur = 0
		cur += v
	return cnt

def binarySearch(m, video):
	left, right = max(video), sum(video)
	while left <= right:
		mid = (left + right) // 2
		required = countBluray(mid, video)
		if required <= m:
			right = mid - 1
		else: 
			left = mid + 1
	return left 

n, m = map(int, input().split()) 
video = list(map(int, input().split()))
print(binarySearch(m, video))
import sys
input = sys.stdin.readline

def countRouter(dist, house):
	cnt = 1
	cur = house[0]
	for h in house:
		if (h - cur) >= dist:
			cur = h
			cnt += 1
	return cnt

def binarySearch(start, end, target, house):
	while start <= end:
		mid = (start + end) // 2
		cnt = countRouter(mid, house)
		if cnt >= target:
			start = mid + 1
		else:
			end = mid - 1
	return start - 1

n, c = map(int, input().split())
house = [int(input()) for _ in range(n)]
house.sort()
print(binarySearch(1, house[-1] - house[0], c, house))
import sys
input = sys.stdin.readline

def countPeople(limit, time):
	cnt = 0
	for t in time:
		cnt += limit // t # 전체 시간 // 각 심사대의 처리 시간 
	return cnt

def binarySearch(n, m, time):
	left, right = min(time), m * max(time)
	while left <= right:
		mid = (left + right) // 2
		cnt = countPeople(mid, time)
		if cnt >= m:
			right = mid - 1
		else:
			left = mid + 1
	return left

n, m = map(int, input().split())
time = [int(input()) for _ in range(n)]
print(binarySearch(n, m, time))
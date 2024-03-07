import sys
input = sys.stdin.readline

def lower_bound(arr, left, right, target):
	while left < right:
		mid = (left + right) // 2
		if arr[mid] >= target:
			right = mid
		else:
			left = mid + 1
	return right

n = int(input())
nums = list(map(int, input().split()))
l = [0]
for n in nums:
	if l[-1] < n:
		l.append(n)
	else:
		idx = lower_bound(l, 0, len(l), n)
		l[idx] = n
print(len(l) - 1)
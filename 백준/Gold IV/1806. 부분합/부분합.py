import sys
input = sys.stdin.readline

def two_pointer(n, s, arr):
	start = end = 0
	temp = arr[0]
	ans = 1e6
	while True:
		if temp < s:
			end += 1
			if end == n:
				break
			temp += arr[end]
		else:
			ans = min(ans, end - start + 1)
			temp -= arr[start]
			start += 1
	return 0 if ans == 1e6 else ans 

n, s = map(int, input().split())
arr = list(map(int, input().split()))
print(two_pointer(n, s, arr))
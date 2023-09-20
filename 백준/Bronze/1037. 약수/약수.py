import sys
input = sys.stdin.readline
cnt = int(input())
arr = list(map(int, input().split()))
def findN(cnt, arr):
	return max(arr) * min(arr)
print(findN(cnt, arr))
import sys
input = sys.stdin.readline
cnt = int(input())
arr = list(map(int, input().split()))
def findN(cnt, arr):
	arr.sort()
	return arr[0] * arr[-1]
print(findN(cnt, arr))
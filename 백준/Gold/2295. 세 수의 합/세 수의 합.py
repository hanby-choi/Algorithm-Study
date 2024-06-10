import sys 
input = sys.stdin.readline
n = int(input())
arr = [int(input()) for _ in range(n)]
twoSum = set()
maxSum = 0
for i in range(n):
	for j in range(n):
		twoSum.add(arr[i] + arr[j])
for k in range(n):
	for l in range(n):
		if (arr[l] - arr[k]) in twoSum:
			maxSum = max(maxSum, arr[l])
print(maxSum)
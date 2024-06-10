import sys
input = sys.stdin.readline

def check(arr):
	is_ascending = True
	is_descending = True
	for i in range(len(arr)-1):
		if arr[i] >= arr[i+1]:
			is_ascending = False
		else:
			is_descending = False
	if is_ascending:
		return 'ascending'
	elif is_descending:
		return 'descending'
	else:
		return 'mixed'

num = list(map(int, input().split()))
print(check(num))
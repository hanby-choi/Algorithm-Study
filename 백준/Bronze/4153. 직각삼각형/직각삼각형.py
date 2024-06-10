import sys
input = sys.stdin.readline
while True:
	arr = list(map(int, input().split()))
	if arr.count(0) == 3:
		break
	max_num = max(arr)
	arr.remove(max_num)
	if (arr[0]**2 + arr[1]**2) == max_num**2:
		print('right')
	else:
		print('wrong')
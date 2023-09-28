import sys
input = sys.stdin.readline
info = [list(map(int, input().split())) for _ in range(10)]
nums = [info[0][1]] * 10 # 첫번째 역에서 탄 사람 수로 초기화 
for i in range(1, 10):
	nums[i] = nums[i-1] - info[i][0] + info[i][1]
print(max(nums))
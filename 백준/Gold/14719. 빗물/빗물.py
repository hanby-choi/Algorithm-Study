import sys
input = sys.stdin.readline

def calcWater(c, height):
	left_max = max(height[:c])
	right_max = max(height[c+1:])
	return max(0, min(left_max, right_max) - height[c])

h, w = map(int, input().split())
height = list(map(int, input().split()))
ans = 0
for i in range(1, w-1):
	ans += calcWater(i, height)
print(ans)
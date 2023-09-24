# 빗물: 구현, 시뮬레이션
import sys
input = sys.stdin.readline

def calcWater(i, height):
    left_max = height[:i]
    right_max = height[i+1:]
    return max(0, min(left_max, right_max) - height[i])

def solution(h, w, height):
    ans = 0
    for i in range(1, w-1):
        ans += calcWater(i, height)
    return ans

h, w = map(int, input().split())
height = list(map(int, input().split()))
print(solution(h, w, height))
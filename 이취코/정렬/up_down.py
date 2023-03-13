# 정렬: 실전 문제 1 위에서 아래로
import sys
input = sys.stdin.readline
N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))
arr.sort(reverse = True) # arr = sorted(arr, reverse = True)
print(*arr)
"""
for i in arr:
    print(i, end = ' ')
"""
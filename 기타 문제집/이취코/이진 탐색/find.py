# 이진 탐색: 실전 문제 1 부품 찾기
import sys
input = sys.stdin.readline
n = int(input())
have = list(map(int, input().split()))
m = int(input())
want = list(map(int, input().split()))
have.sort() # 정렬 - 시간 복잡도 O(NlogN)
def binary_search(array, target, start, end): # 이진 탐색 - 시간 복잡도 O(logN)
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None
for i in want:
    if binary_search(have, i, 0, n-1) != None:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')
"""
# 계수 정렬로 풀기 O(N)
array = [0] * 1000001
for i in input().split():
    array[int(i)] = 1
for i in want:
    if array[i] == 1:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')
"""
"""
# 집합으로 풀기: M * O(N)
have = set(map(int, input().split()))
for i in want:
    if i in have:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')
"""
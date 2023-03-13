# 이진 탐색: 실전 문제 2 떡볶이 떡 만들기
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
length = list(map(int, input().split()))
start = 0; end = max(length)
ans = 0
while (start <= end):
    total = 0
    mid = (start + end) // 2
    for i in length:
        if i > mid:
            total += (i - mid)
    if total < m: # 떡의 양이 부족한 경우 더 많이 자르기 (H 감소)
        end = mid - 1
    else: # 떡의 양이 충분한 경우 덜 자르기 (H 증가)
        ans = mid
        start = mid + 1
print(ans)
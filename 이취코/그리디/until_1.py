# 그리디: 1이 될 때까지
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
cnt = 0
while N != 1:
    if N % K == 0:
        N /= K
    else:
        N -= 1
    cnt += 1
print(cnt)
"""
# 효율적인 연산을 위해 1씩 빼지 않고 N이 K의 배수가 될 때까지 한 번에 빼는 코드
while True:
    left = N % K
    cnt += left
    N -= left
    if N < K: # 더 이상 나눌 수 없을 때
        break
    cnt += 1
    N //= K
cnt += (N-1)
print(cnt)
"""
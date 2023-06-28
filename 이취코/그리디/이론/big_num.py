# 그리디: 큰 수의 법칙
import sys
input = sys.stdin.readline
N, M, K = map(int, input().split())
arr = list(map(int, input().split()))
max_index = arr.index(max(arr))
max_first = arr.pop(max_index)
max_second = max(arr)
second_cnt = M // (K+1) # 두번째로 큰 수가 더해질 횟수
ans = 0
ans = (second_cnt * max_second) + ((M-second_cnt) * max_first)
print(ans)
'''
arr.sort()
first = arr[-1]
second = arr[-2]
count = (m // (k+1)) * k
count += m % (k+1)
# count는 가장 큰 수가 더해질 횟수
'''
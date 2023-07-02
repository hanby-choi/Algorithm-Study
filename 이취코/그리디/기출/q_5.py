# 그리디 - 5. 볼링공 고르기
import sys, collections
input = sys.stdin.readline
def nC2(n):
    return int(n*(n-1)/2)
n, m = map(int, input().split())
weight = list(map(int, input().split()))
cnt = collections.Counter(weight)
total = nC2(n)
for key, value in cnt.items():
    if value > 1:
        total -= nC2(value)
print(total)
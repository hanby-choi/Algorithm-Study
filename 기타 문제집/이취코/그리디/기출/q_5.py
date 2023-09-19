# 그리디 - 5. 볼링공 고르기
"""import sys, collections
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
print(total)"""
n, m = map(int, input().split())
weight = list(map(int, input().split()))
cnt = [0] * (m+1) # 무게별 공의 개수 저장할 배열
for x in weight:
	cnt[x] += 1
result = 0
for i in range(1, m):
	n -= cnt[i] # B가 선택할 수 있는 공의 수 (전체에서 무게가 1~i인 공의 수 제외)
	result += cnt[i] * n # A가 선택할 수 있는 공의 수(무게가 i인 공의 수) * B가 선택할 수 있는 공의 수
print(result)
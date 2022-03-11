# 6092~6098 [기초-종합]

# 6092 : [기초-리스트] 이상한 출석 번호 부르기1(설명)(py)
n = int(input())
a = list(map(int, input().split()))
d = [0]*24 # 0~23
for i in range(0, n):
    d[a[i]] += 1
for i in range(1, 24):
    print(d[i], end=' ')

# 6093 : [기초-리스트] 이상한 출석 번호 부르기2(py)
n = int(input())
a = list(map(int, input().split()))
for i in range(n-1, -1, -1):
    print(a[i], end=' ')

# 6094 : [기초-리스트] 이상한 출석 번호 부르기3(py)
n = int(input())
a = list(map(int, input().split()))
min = a[0]
for i in range(1, n):
    if min > a[i]:
        min = a[i]
print(min)

# 6095 : [기초-리스트] 바둑판에 흰 돌 놓기(설명)(py)

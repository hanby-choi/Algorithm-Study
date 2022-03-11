# 6092~6098 [기초-종합]
'''
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
d = [[0]*20 for i in range(20)]
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    d[x][y] = 1
for i in range(1, 20):
    for j in range(1, 20):
        print(d[i][j], end=' ')
    print() # 줄바꿈
'''
# 6096 : [기초-리스트] 바둑알 십자 뒤집기(py)
a=[]
for i in range(19):
    a.append(list(map(int, input().split())))

n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    for j in range(19):
        if a[x-1][j] == 0:
            a[x-1][j] = 1
        else:
            a[x-1][j] = 0
        if a[j][y-1] == 0:
            a[j][y-1] = 1
        else:
            a[j][y-1] = 0
for i in range(19):
    for j in range(19):
        print(a[i][j], end=' ')
    print() # 줄바꿈
# 6077~6091 [기초-종합]

# 6077 : [기초-종합] 짝수 합 구하기(설명)(py)
n = int(input())
sum = 0
for i in range(1, n+1):
    if i % 2 == 0:
        sum += i
    else:
        continue
print(sum)

# 6078 : [기초-종합] 원하는 문자가 입력될 때까지 반복 출력하기(py)
c = ''
while c != 'q':
    c = input()
    print(c)

# 6079 : [기초-종합] 언제까지 더해야 할까?(py)
sum = 0
n = int(input())
for i in range(1, n+1):
    sum += i
    if sum >= n:
        print(i)
        break

# 6080 : [기초-종합] 주사위 2개 던지기(설명)(py)
n, m = map(int, input().split())
for i in range(1, n+1):
    for j in range(1, m+1):
        print(i, j)

# 6081 : [기초-종합] 16진수 구구단 출력하기(py)
n = int(input(), 16) # 16진수로 입력 받음
for i in range(0X01, 0X10): # i도 16진수
    print('%X'%n, '*%X'%i, '=%X'%(n*i), sep='')

# 6082 : [기초-종합] 3 6 9 게임의 왕이 되자(설명)(py)
n = int(input())
for i in range(1, n+1):
    if (str(i).find('3') != -1) or (str(i).find('6') != -1) or (str(i).find('9') != -1): # 3 또는 6 또는 9가 있으면
        print('X', sep=' ')
    else:
        print(i, sep=' ')

# 6083 : [기초-종합] 빛 섞어 색 만들기(설명)(py)
r, g, b = map(int, input().split())
for i in range(r):
    for j in range(g):
        for k in range(b):
            print(i, j, k)
print(r*g*b)

# 6084 : [기초-종합] 소리 파일 저장용량 계산하기(py)
h, b, c, s = map(int, input().split())
memory = h*b*c*s/8/1024/1024
print(format(memory, ".1f"), 'MB')

# 6085 : [기초-종합] 그림 파일 저장용량 계산하기(py)
w, h, b = map(int, input().split())
memory = w*h*b/8/1024/1024
print(format(memory, ".2f"), 'MB')

# 6086 : [기초-종합] 거기까지! 이제 그만~(설명)(py)
sum = 0
n = int(input())
for i in range(1, n+1):
    sum += i
    if sum >= n:
        print(sum)
        break

# 6087 : [기초-종합] 3의 배수는 통과(설명)(py)
n = int(input())
for i in range(1, n+1):
    if i%3!=0:
        print(i, sep=' ')

# 6088 : [기초-종합] 수 나열하기1(py)
a, d, n = map(int, input().split())
print(a+d*(n-1))

# 6089 : [기초-종합] 수 나열하기2(py)
a, r, n = map(int, input().split())
print(a*(r**(n-1)))

# 6090 : [기초-종합] 수 나열하기3(py)
a, m, d, n = map(int, input().split())
result = a
for i in range(n-1):
    a = a*m+d
print(a)

# 6091 : [기초-종합] 함께 문제 푸는 날(설명)(py)
a, b, c = map(int, input().split())
d = 1
while d%a!=0 or d%b!=0 or d%c!=0: # d가 a, b, c 모두의 배수인 경우 멈춤
    d += 1
print(d)
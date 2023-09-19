# 6065~6076 [기초-조건/선택실행구조, 반복실행구조]

# 6065 : [기초-조건/선택실행구조] 정수 3개 입력받아 짝수만 출력하기(설명)(py)
a, b, c = map(int, input().split())
if a % 2 == 0:
    print(a)
if b % 2 == 0:
    print(b)
if c % 2 == 0:
    print(c)

# 6066 : [기초-조건/선택실행구조] 정수 3개 입력받아 짝/홀 출력하기(설명)(py)
a, b, c = map(int, input().split())
if a % 2 == 0:
    print("even")
else: 
    print("odd")
if b % 2 == 0:
    print("even")
else: 
    print("odd")
if c % 2 == 0:
   print("even")
else: 
    print("odd")

# 6067 : [기초-조건/선택실행구조] 정수 1개 입력받아 분류하기(설명)(py)
a = int(input())
if a<0:
    if a%2==0:
        print('A')
    else:
        print('B')
elif a>0:
    if a%2==0:
        print('C')
    else:
        print('D')
else:
    print('입력 오류')

# 6068 : [기초-조건/선택실행구조] 점수 입력받아 평가 출력하기(설명)(py)
a = int(input())
if 90 <= a <= 100:
    print('A')
elif a >= 70:
    print('B')
elif a >= 40:
    print('C')
else:
    print('D')

# 6069 : [기초-조건/선택실행구조] 평가 입력받아 다르게 출력하기(py)
a = input()
if a == 'A':
    print('best!!!')
elif a == 'B':
    print('good!!')
elif a == 'C':
    print('run!')
elif a == 'D':
    print('slowly~')
else:
    print('what?')

# 6070 : [기초-조건/선택실행구조] 월 입력받아 계절 출력하기(설명)(py)
month = int(input())
if month//3 == 1:
    print("spring")
elif month//3 == 2:
    print("summer")
elif month//3 == 3:
    print("fall")
else:
    print("winter")

# 6071 : [기초-반복실행구조] 0 입력될 때까지 무한 출력하기(설명)(py)
n = 1
while n != 0:
    n = int(input())
    if n != 0:
        print(n)

# 6072 : [기초-반복실행구조] 정수 1개 입력받아 카운트다운 출력하기1(설명)(py)
n = int(input())
while n > 0:
    print(n)
    n -= 1

# 6073 : [기초-반복실행구조] 정수 1개 입력받아 카운트다운 출력하기2(py)
n = int(input())
while n > 0:
    n -= 1
    print(n)
    
# 6074 : [기초-반복실행구조] 문자 1개 입력받아 알파벳 출력하기(설명)(py)
c = ord(input())
t = ord('a')
while (t <= c):
    print(chr(t), end=' ')
    t += 1

# 6075 : [기초-반복실행구조] 정수 1개 입력받아 그 수까지 출력하기1(py)
n = int(input())
a = 0
while (a <= n):
    print(a)
    a += 1

# 6076 : [기초-반복실행구조] 정수 1개 입력받아 그 수까지 출력하기2(설명)(py)
n = int(input())
for i in range(n+1):
    print(i)
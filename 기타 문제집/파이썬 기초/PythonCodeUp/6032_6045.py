# 6032~6045 [기초-산술연산]

# 6032 : [기초-산술연산] 정수 1개 입력받아 부호 바꾸기(설명)(py)
n = int(input())
print(-n)

# 6033 : [기초-산술연산] 문자 1개 입력받아 다음 문자 출력하기(설명)(py)
n = ord(input())
print(chr(n+1))

# 6034 : [기초-산술연산] 정수 2개 입력받아 차 계산하기(설명)(py)
a, b = input().split()
print(int(a)-int(b))

# 6035 : [기초-산술연산] 실수 2개 입력받아 곱 계산하기(설명)(py)
a, b = input().split()
print(float(a) * float(b))

# 6036 : [기초-산술연산] 단어 여러 번 출력하기(설명)(py)
w, n = input().split()
print(w*int(n))

# 6037 : [기초-산술연산] 문장 여러 번 출력하기(설명)(py)
n = input()
s = input()
print(int(n)*s)

# 6038 : [기초-산술연산] 정수 2개 입력받아 거듭제곱 계산하기(설명)(py)
a, b = map(int, input().split())
print(a**b)

# 6039 : [기초-산술연산] 실수 2개 입력받아 거듭제곱 계산하기(py)
a, b = map(float, input().split())
print(a**b)

# 6040 : [기초-산술연산] 정수 2개 입력받아 나눈 몫 계산하기(설명)(py)
a, b = map(int, input().split())
print(a//b)

# 6041 : [기초-산술연산] 정수 2개 입력받아 나눈 나머지 계산하기(설명)(py)
a, b = map(int, input().split())
print(a%b)

# 6042 : [기초-값변환] 실수 1개 입력받아 소숫점이하 자리 변환하기(설명)(py)
a = float(input())
print(format(a, ".2f"))
print('{0:0.2f}'.format(a))

# 6043 : [기초-산술연산] 실수 2개 입력받아 나눈 결과 계산하기(py)
a, b = map(float, input().split())
print(format(a/b, ".3f"))

# 6044 : [기초-산술연산] 정수 2개 입력받아 자동 계산하기(py)
a, b =  map(int, input().split())
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print(format(a/b, '.2f'))

# 6045 : [기초-산술연산] 정수 3개 입력받아 합과 평균 출력하기(설명)(py)
a, b, c = map(int, input().split())
sum = a+b+c
print(sum, format(sum/3.0, '.2f'))

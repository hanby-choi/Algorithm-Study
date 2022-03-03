# 6009~6024 [기초-입출력]

# 6009 [기초-입출력] 문자 1개 입력받아 그대로 출력하기(설명)(py)
c = input()
print(c)

# 6010 [기초-입출력] 정수 1개 입력받아 int로 변환하여 출력하기(설명)(py)
n = input()
print(int(n))

# 6011 [기초-입출력] 실수 1개 입력받아 변환하여 출력하기(설명)(py)
f = input()
print(float(f))

# 6012 [기초-입출력] 정수 2개 입력받아 그대로 출력하기1(설명)(py)
a = input() 
b = input()
print(a)
print(b)

# 6013 [기초-입출력] 문자 2개 입력받아 순서 바꿔 출력하기1(py)
a = input() 
b = input()
print(b)
print(a)

# 6014 [기초-입출력] 실수 1개 입력받아 3번 출력하기(py)
f=input()
print(f)
print(f)
print(f)

# 6015 [기초-입출력] 정수 2개 입력받아 그대로 출력하기2(설명)(py)
a, b = input().split()
print(a)
print(b)

# 6016 [기초-입출력] 문자 2개 입력받아 순서 바꿔 출력하기2(설명)(py)
a, b = input().split()
print(b, a)

# 6017 [기초-입출력] 문장 1개 입력받아 3번 출력하기(설명)(py)
s = input()
print(s, s, s)

# 6018 [기초-입출력] 시간 입력받아 그대로 출력하기(설명)(py)
a, b = input().split(':')
print(a, b, sep=':')

# 6019 [기초-입출력] 연월일 입력받아 순서 바꿔 출력하기(py)
y, m, d = input().split('.')
print(d, m, y, sep = '-')

# 6020 [기초-입출력] 주민번호 입력받아 형태 바꿔 출력하기(py)
a, b = input().split('-')
print(a, b, sep = "")

# 6021 [기초-입출력] 단어 1개 입력받아 나누어 출력하기(설명)(py)
s = input()
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])

# 6022 [기초-입출력] 연월일 입력받아 나누어 출력하기(설명)(py)
s = input()
print(s[0:2], s[2:4], s[4:6])

# 6023 [기초-입출력] 시분초 입력받아 분만 출력하기(py)
a, b, c = input().split(":")
print(b)

# 6024 [기초-입출력] 단어 2개 입력받아 이어 붙이기(설명)(py)
w1, w2 = input().split()
s = w1 + w2
print(s)





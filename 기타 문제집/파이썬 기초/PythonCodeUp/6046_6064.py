# 6046~6064 [기초-비트시프트연산, 비교연산, 논리연산, 비트단위논리연산, 3항연산]

# 6046 : [기초-비트시프트연산] 정수 1개 입력받아 2배 곱해 출력하기(설명)(py)
n = int(input())
print(n<<1)

# 6047 : [기초-비트시프트연산] 2의 거듭제곱 배로 곱해 출력하기(설명)(py)
a, b = map(int, input().split())
print(a<<b)


# 6048 : [기초-비교연산] 정수 2개 입력받아 비교하기1(설명)(py)
a, b = map(int, input().split())
if a < b:
    print(True)
else:
    print(False)

# 6049 : [기초-비교연산] 정수 2개 입력받아 비교하기2(설명)(py)
a, b = map(int, input().split())
if a == b:
    print(True)
else:
    print(False)

# 6050 : [기초-비교연산] 정수 2개 입력받아 비교하기3(설명)(py)
a, b = map(int, input().split())
if a <= b:
    print(True)
else:
    print(False)

# 6051 : [기초-비교연산] 정수 2개 입력받아 비교하기4(설명)(py)
a, b = map(int, input().split())
if a != b:
    print(True)
else:
    print(False)

# 6052 : [기초-논리연산] 정수 입력받아 참 거짓 평가하기(설명)(py)
n = int(input())
print(bool(n))

# 6053 : [기초-논리연산] 참 거짓 바꾸기(설명)(py)
a = bool(int(input()))
print(not a)

# 6054 : [기초-논리연산] 둘 다 참일 경우만 참 출력하기(설명)(py)
a, b = map(int, input().split())
print(bool(a) and bool(b))

# 6055 : [기초-논리연산] 하나라도 참이면 참 출력하기(설명)(py)
a, b = map(int, input().split())
print(bool(a) or bool(b))

# 6056 : [기초-논리연산] 참/거짓이 서로 다를 때에만 참 출력하기(설명)(py)
a, b = map(int, input().split())
print(bool(a) ^ bool(b))

# 6057 : [기초-논리연산] 참/거짓이 서로 같을 때에만 참 출력하기(설명)(py)
a, b = map(int, input().split())
print(not (bool(a) ^ bool(b)))

# 6058 : [기초-논리연산] 둘 다 거짓일 경우만 참 출력하기(py)
a, b = map(int, input().split())
print(not (bool(a) or bool(b)))

# 6059 : [기초-비트단위논리연산] 비트단위로 NOT 하여 출력하기(설명)(py)
a = int(input())
print(~a)

# 6060 : [기초-비트단위논리연산] 비트단위로 AND 하여 출력하기(설명)(py)
a, b = map(int, input().split())
print(a & b)

# 6061 : [기초-비트단위논리연산] 비트단위로 OR 하여 출력하기(설명)(py)
a, b = map(int, input().split())
print(a | b)

# 6062 : [기초-비트단위논리연산] 비트단위로 XOR 하여 출력하기(설명)(py)
a, b = map(int, input().split())
print(a ^ b)

# 6063 : [기초-3항연산] 정수 2개 입력받아 큰 값 출력하기(설명)(py)
a, b = map(int, input().split())
print(a if a>=b else b)


# 6064 : [기초-3항연산] 정수 3개 입력받아 가장 작은 값 출력하기(설명)(py)
a, b, c = map(int, input().split())
print((a if a<=b else b) if (a if a<=b else b)<=c else c)
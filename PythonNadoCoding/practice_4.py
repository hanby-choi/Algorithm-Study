#4 문자열 처리

#4-1 문자열
sentence = "파이썬은 쉬워요"
print(sentence) 

sentence3 = """
나는 소년이고, 
파이썬은 쉬워요
"""
print(sentence3)

#4-2 슬라이싱
jumin = "990120-1234567"
print("성별 : " + jumin[7]) # 1
print("연 : " + jumin[0:2]) # 0부터 2 직전까지 (99)
print("월 : " + jumin[2:4]) # 01
print("일 : " + jumin[4:6]) # 20
print("생년월일 : " + jumin[:6]) # 처음부터 6 직전까지 (990120)
print("뒤 7자리 : " + jumin[7:]) # 7부터 끝까지 (1234567)
print("뒤 7자리 (뒤에부터) : " + jumin[-7:]) # 맨 뒤에서 7번째부터 끝까지 (1234567)

#4-3 문자열 처리 함수
python = "Python is Amazing"
print(python.lower()) # 소문자 변환, python is amazing
print(python.upper()) # 대문자 변환, PYTHON IS AMAZING
print(python[0].isupper()) # 대문자 검사, True
print(len(python)) # 길이 계산, 17
print(python.replace("Python", "Java")) # 문자열 대체, Java is Amazing

index = python.index("n") # 가장 처음에 나오는 위치
print(index) # 5
index = python.index("n", index + 1) # index + 1 번째부터 인덱스 찾기 (두번째로 n이 나오는 위치)
print(index) # 15

print(python.find("Java")) # 찾는 값이 없으면 -1 반환, -1
print(python.index("Java")) # 찾는 값이 없으면 에러 발생

print(python.count("n")) # 해당 문자열의 개수 반환, 2

#4-4 문자열 포맷
print("a" + "b") # ab
print("a", "b") # a b

# 방법 1: % 이용
print("나는 %d살입니다." % 20) # 정수 대입, 나는 20살입니다.
print("나는 %s을 좋아해요." % "파이썬") # 문자열 대입, 나는 파이썬을 좋아해요.
print("Apple은 %c로 시작해요." % "A") # 문자 대입, Apple은 A로 시작해요.
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간")) # 여러 개 문자열 대입, 나는 파란색과 빨간색을 좋아해요.

# 방법 2: {} 이용
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간")) # 나는 파란색과 빨간색을 좋아해요.
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간")) # 나는 빨간색과 파란색을 좋아해요.

# 방법 3: {변수} 이용
print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color="빨간"))
print("나는 {age}살이며, {color}색을 좋아해요.".format(color="빨간", age = 20))

# 방법 4 (v3.6 이상~)
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.") # f: 실제 변수의 값을 가져다 사용

#4-5 탈출 문자
# \n : 줄바꿈

# \" \' : 문장 내에서 따옴표
# 저는 "나도코딩" 입니다.
# print("저는 '나도코딩'입니다.")
# print('저는 "나도코딩"입니다.')
print("저는 \"나도코딩\"입니다.")
print("저는 \'나도코딩\'입니다.")

# \\ : 문장 내에서 하나의 \
print("C:\\Users\\Nadocoding");

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine") # PineApple - Red 자리로 커서가 이동해서 그 위치에 Pine 작성

# \b : 백스페이스 (한 글자 삭제)
print("Redd\bApple") # Red Apple

# \t : 탭
print("Red\tApple") # Red    Apple

#4-6 퀴즈 3
url = "http://naver.com"
my_str = url.replace("http://", "") # 규칙 1
print(my_str) # naver.com
my_str = my_str[:my_str.index(".")] # 처음 만나는 . 의 위치 직전까지 슬라이싱 - 규칙 2
print(my_str) # naver
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0}의 비밀번호는 {1} 입니다.".format(url, password))
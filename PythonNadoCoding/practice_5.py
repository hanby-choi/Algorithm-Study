#5 자료구조
#5-1 리스트
subway = [10, 20, 30]
print(subway) # [10, 20, 30]

subway = ["유재석", "조세호", "박명수"]
print(subway.index("조세호")) # 1

subway.append("하하") # append는 리스트 맨 뒤에 추가
print(subway) # ["유재석", "조세호", "박명수", "하하"]

subway.insert(1, "정형돈") # 리스트의 지정한 위치에 추가
print(subway) # ["유재석", "정형돈", "조세호", "박명수", "하하"]

print(subway.pop()) # 맨 뒤의 사람 제거, 하하
print(subway) # ["유재석", "정형돈", "조세호", "박명수" ]

print(subway.count("유재석")) # 같은 사람의 이름이 몇 명 있는지 확인

# 정렬
num_list = [5, 2, 4, 3, 1]
num_list.sort() # 정렬
print(num_list)  # [1, 2, 3, 4, 5]

num_list.reverse() # 순서 뒤집기
print(num_list) # [5, 4, 3, 2, 1]

num_list.clear() # 모두 지우기
print(num_list) # []

# 다양한 자료형 함께 사용 가능
mix_list = ["조세호", 20, True]

# 리스트 확장
num_list.extend(mix_list)
print(num_list) # [5, 2, 4, 3, 1, "조세호", 20, True]

#5-2 사전
cabinet = {3:"유재석", 100:"김태호"}

# 사전 자료형에서 값을 가져오는 방법 - [], .get()
print(cabinet[3]) # key에 해당하는 value 출력, 유재석
print(cabinet[5]) # 5에 해당하는 value가 없으므로 에러 발생

print(cabinet.get(3)) # 유재석
print(cabinet.get(5)) # 5에 해당하는 value가 없으므로 None 출력 후 다음 코드 실행
print(cabinet.get(5, "사용 가능")) # 5에 해당하는 값이 없는 경우 기본값인 "사용 가능" 출력

# 특정 키가 있는지 검색
print(3 in cabinet) # True
print(5 in cabinet) # False

# key가 문자 자료형인 경우도 가능
cabinet = {"A-3":"유재석", "B-100":"김태호"}

# 새로운 key, value 추가
cabinet["A-3"] = "김종국" # 값을 업데이트
cabinet["C-20"] = "조세호" # 값을 추가
print(cabinet) # {'A-3': '김종국', 'B-100': '김태호', 'C-20': '조세호'}

# 값 삭제
del cabinet["A-3"]
print(cabinet) # {'B-100': '김태호', 'C-20': '조세호'}

# key들만 출력
print(cabinet.keys())

# value들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 사전 비우기
cabinet.clear()
print(cabinet) # {}

#5-3 튜플
menu = ("돈가스", "치즈가스")
print(menu[0]) # 돈가스
print(menu[1]) # 치즈가스

name = "김종국"
age = 20
hobby = "코딩"

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby) # 김종국 20 코딩

#5-4 세트(집합)
my_set = {1, 2, 3, 3, 3}
print(my_set) # {1, 2, 3}

# 집합을 정의하는 두 가지 방법
java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"]) # 리스트 만든 후 set()으로 변환

# 교집합 
print(java & python) # {'유재석'}
print(java.intersection(python))

# 합집합
print(java | python) # {'김태호', '박명수', '유재석', '양세형') - 순서 없음
print(java.union(python))

# 차집합 (java는 할 수 있지만 python은 할 수 없는 사람들)
print(java - python)
print(java.difference(python))

# 집합 원소 추가
python.add("김태호")

# 집합 원소 삭제
java.remove("김태호")

#5-5 자료구조의 변경
menu = {"커피", "우유", "주스"} # 집합
print(menu, type(menu)) # {"커피", "우유", "주스"} <class 'set'>

menu = list(menu) # 리스트로 변환
print(menu, type(menu)) # ['주스', '우유', '커피'] <class 'list'>

menu = tuple(menu) # 튜플로 변환
print(menu, type(menu)) # ('주스', '우유', '커피') <class 'tuple'>

menu = set(menu) # 집합으로 변환
print(menu, type(menu)) # {'우유', '커피', '주스'} <class 'set'>

#5-6 퀴즈 4
from random import *
lst = [1, 2, 3, 4, 5]
print(lst) # [1, 2, 3, 4, 5]
shuffle(lst) # 리스트 안의 원소 순서를 무작위로 바꿈
print(lst) # [5, 4, 1, 3, 2]
print(sample(lst, 1)) # 리스트 안의 원소 중 한 개를 무작위로 뽑기, [4]

users = range(1, 21) # 1부터 20까지의 숫자를 생성
print(type(users)) # <class 'range'>
users = list(users) # 리스트로 변환
print(type(users)) # <class 'list'>

shuffle(users)
winners = sample(users, 4)

print(" -- 당첨자 발표 -- ")
print("치킨 당첨자 : {0}".format(winners[0]))
print("치킨 당첨자 : {0}".format(winners[1:])) # winners의 1, 2, 3
print(" -- 축하합니다 -- ")
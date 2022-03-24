# 브루트 포스 - 2231: 분해합
# 내 풀이
n = int(input())
max = 1000000
arr = [0] * (max+1) # 굳이 배열로 저장할 필요 없이 바로바로 값을 비교해 출력하면 됨
ans = 0
for i in range(1, max+1):
    arr[i] = i 
    num_list = list(map(int, str(i)))
    for j in range(len(num_list)): # sum 함수로 간단하게 해결 가능
        arr[i] += num_list[j]
    if arr[i] == n:
        ans = i
        break
    num_list.clear() # 리스트 생성 시 append가 아니고 list로 새 리스트를 매핑해주는 것이므로 생략 가능함
print(ans)

# 모범 답안(https://yongku.tistory.com/787) -  짧고 메모리를 덜 사용하는 코드
n = int(input())
result = 0
for i in range(1, n+1):
    num_list = list(map(int, str(i)))
    result = i + sum(num_list)
    if result == n: # 생성자 발견하면 출력 후 종료 - 가장 작은 생성자
        print(i) 
        break
    if i == n: # 생성자가 없는 경우 0 출력
        print(0) 
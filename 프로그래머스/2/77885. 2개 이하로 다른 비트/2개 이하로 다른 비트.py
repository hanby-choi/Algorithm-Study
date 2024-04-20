def findMin(num):
    b_num = bin(num)[2:][::-1]
    cnt = 0
    for b in b_num:
        if b == '0':
            break
        else:
            cnt += 1
    if cnt < 2:
        return num + 1
    else:
        return num + 2 ** (cnt-1)
    
def solution(numbers):
    answer = []
    for num in numbers: 
        answer.append(findMin(num))
    return answer
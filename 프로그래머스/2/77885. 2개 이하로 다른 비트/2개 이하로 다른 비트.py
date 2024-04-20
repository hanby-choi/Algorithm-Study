def findMin(num):
    if num % 2 == 0:
        return num + 1
    b_num = '0' + bin(num)[2:]
    idx = b_num.rfind('0')
    b_num = list(b_num)
    b_num[idx] = '1'
    b_num[idx + 1] = '0'
    return int(''.join(b_num), 2)
    
def solution(numbers):
    answer = []
    for num in numbers: 
        answer.append(findMin(num))
    return answer
from itertools import combinations
def solution(nums):
    answer = 0
    is_prime = [True] * 3001
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(3000**(1/2))+1):
        if (is_prime[i]):
            for j in range(i*i, 3001, i):
                is_prime[j] = False
    com = combinations(nums, 3)
    for c in com:
        if is_prime[sum(c)]:
            answer += 1
    return answer
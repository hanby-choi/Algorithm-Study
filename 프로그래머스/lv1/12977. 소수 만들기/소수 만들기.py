from itertools import combinations
def solution(nums):
    answer = 0
    is_prime = [False] * 2 + [True] * 2999
    for i in range(2, int(3000 ** 0.5) + 1):
        if (is_prime[i]):
            for j in range(i*i, 3001, i):
                is_prime[j] = False
    for c in combinations(nums, 3):
        if is_prime[sum(c)]:
            answer += 1
    return answer
import sys
input = sys.stdin.readline

def divisor(number): 
    result = []
    for i in range(1, int(number ** 0.5) + 1):
        if number % i == 0:
            result.append(i)
            if i < number // i: 
                result.append(number // i)
    return result 

n = int(input())
dict = {num: i for i, num in enumerate(list(map(int, input().split())))}
ans = [0] * n
for num, index in dict.items():
    div = divisor(num)
    for d in div:
        if d in dict:
            ans[index] -= 1
            ans[dict[d]] += 1
print(*ans)
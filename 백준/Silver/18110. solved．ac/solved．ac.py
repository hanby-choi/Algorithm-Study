import sys
input = sys.stdin.readline

def my_round(num):
    if num - int(num) >= 0.5:
        return int(num) + 1
    else:
        return int(num)

def score(n, rate):
    if n == 0:
        return 0 
    else:
        cut = my_round(n * 0.15)
        rate.sort()
        avg = my_round(sum(rate[cut:n-cut]) / (n - 2 * cut))
    return avg
        
n = int(input())
rate = [int(input()) for _ in range(n)]
print(score(n, rate))
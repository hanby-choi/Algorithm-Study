# 그리디: 5585 거스름돈
import sys
input = sys.stdin.readline
N = int(input())
num = 1000 - N
coin = [500, 100, 50, 10, 5, 1]
count = 0
for i in coin:
    count += num // i
    num %= i
print(count)
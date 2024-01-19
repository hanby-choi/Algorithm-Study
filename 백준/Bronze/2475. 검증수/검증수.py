import sys
input = sys.stdin.readline
arr = list(map(int, input().split()))
total = 0
for a in arr:
    total += a*a
print(total % 10)
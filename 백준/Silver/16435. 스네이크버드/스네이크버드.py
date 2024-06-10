import sys
input = sys.stdin.readline
n, l = map(int, input().split())
height = list(map(int, input().split()))
height.sort()
for h in height:
    if h <= l:
        l += 1
print(l)
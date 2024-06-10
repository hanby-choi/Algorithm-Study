import sys
input = sys.stdin.readline
l, p = map(int, input().split())
news = list(map(int, input().split()))
total = l * p
for n in news:
    print(n - total, end=' ')
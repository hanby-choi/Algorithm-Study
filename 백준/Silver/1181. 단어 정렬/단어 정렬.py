import sys 
input = sys.stdin.readline
from functools import cmp_to_key

n = int(input())
arr = list(set(input().strip() for _ in range(n)))
arr.sort()
arr.sort(key = len)
for a in arr:
    print(a)
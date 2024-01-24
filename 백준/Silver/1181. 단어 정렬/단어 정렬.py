import sys 
input = sys.stdin.readline
from functools import cmp_to_key

def comparator(a,b):
    if len(a) < len(b) or (len(a) == len(b) and a < b):
        return 1
    else:
        return -1

n = int(input())
arr = list(set(input().strip() for _ in range(n)))
sorted_arr = sorted(arr, key=cmp_to_key(comparator), reverse=True)
for s in sorted_arr:
	print(s)
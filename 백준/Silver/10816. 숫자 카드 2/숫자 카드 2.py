from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
query = list(map(int, input().split()))
cnt = Counter(arr) 
for q in query:
	print(cnt[q], end=' ')
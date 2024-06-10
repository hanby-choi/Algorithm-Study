import sys
input = sys.stdin.readline
n = int(input())
words = list(input().split())
cnt = 0
banned = {'she', 'he', 'her', 'him'}
for w in words:
	if w in banned:
		cnt += 1
print(cnt) 
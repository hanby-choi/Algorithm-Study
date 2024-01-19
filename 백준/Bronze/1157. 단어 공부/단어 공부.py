import sys
input = sys.stdin.readline
from collections import Counter

word = input().strip().upper()
cnt = Counter(word).most_common()
if len(cnt) != 1 and cnt[0][1] == cnt[1][1]:
	print('?')
else:
	print(cnt[0][0])
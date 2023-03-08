# 구현: 예제 4-2 시각
import sys
input = sys.stdin.readline
N = int(input())
cnt = 0
"""
for h in range(N+1):
    if h == 3 or h == 13 or h == 23:
        cnt += 3600
    else:
        cnt += 15*60*2 - 15*15
"""
for h in range(N+1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h)+str(m)+str(s):
                cnt += 1
print(cnt)
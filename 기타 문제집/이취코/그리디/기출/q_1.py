# 그리디 - 1. 모험가 길드 
n = int(input())
fears = list(map(int, input().split()))
fears.sort() # 오름차순 정렬
current = require = 1
ans = 0
for fear in fears:
	require = fear
	if require > current:
		current += 1
	else:
		ans += 1
		current = 1
print(ans)
'''
n = int(input())
fear = list(map(int, input().split()))
fear.sort() # 오름차순 정렬
ans = crnt = 0
for i in fear:
	crnt += 1
	if crnt >= i:
		ans += 1
		crnt = 0
print(ans)
'''
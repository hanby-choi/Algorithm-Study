import sys
input = sys.stdin.readline
x = int(input())
cnt = 0
for i in range(7): # 64는 2의 6승이므로 1000000 - 7자리 중 1이 몇 개인지 
	if x & (1 << i):
		cnt += 1
print(cnt)
import sys
input = sys.stdin.readline
n = int(input())
liquid = sorted(list(map(int, input().split())))
ans = [0, 0, 0]
l_sum = 1e10
for i in range(n-2):
	start, end = i+1, n-1
	while start < end:
		temp = liquid[i] + liquid[start] + liquid[end]
		if abs(temp) < abs(l_sum): # 현재까지 저장된 값보다 작으면 
			l_sum = temp
			ans = liquid[i], liquid[start], liquid[end] # 정답 갱신 
		if temp < 0: # 합이 음수면
			start += 1 # 더 큰 수 추가
		elif temp > 0: # 합이 양수면
			end -= 1 # 더 작은 수 추가
		else: # 합이 0이면 
			print(*ans) # 정답 출력 
			exit()
print(*ans)
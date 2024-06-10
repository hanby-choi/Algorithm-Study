import sys
input = sys.stdin.readline
def find(n, liquid):
	start, end = 0, n-1
	l_sum = 1e10 # 탐색 중 가장 0에 가까운 값을 저장할 변수
	ans = [0, 0] # 가장 0에 가까운 값을 만드는 두 용액의 값을 저장할 배열
	while start < end:
		temp = liquid[start] + liquid[end]
		if abs(temp) <= l_sum:
			l_sum = abs(temp)
			ans[0], ans[1] = liquid[start], liquid[end]
		if temp < 0:
			start += 1
		elif temp == 0:
			break
		else:
			end -= 1
	return ans 
					
n = int(input())
liquid = list(map(int, input().split()))
print(*find(n, liquid))
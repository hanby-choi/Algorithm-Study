# ATM: 그리디, 정렬 / 18회차 기출
import sys
input = sys.stdin.readline
def solution(n, time):
	time.sort()
	total = 0
	temp = 0
	"""
	for i in range(n):
		total += time[i] * (n-i) 
	"""
	for i in range(n):
		temp += time[i]
		total += temp 
	return total
n = int(input())
time = list(map(int, input().split()))
print(solution(n, time))
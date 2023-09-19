# 국영수: 정렬
import sys 
input = sys.stdin.readline
n = int(input())
info = []
print(input().split(' ', 1))
print(map(int, input().split()))
"""import sys
input = sys.stdin.readline
n = int(input())
info = []
for _ in range(n):
	info.append(input().split())
print(info)
info.sort(key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for student in info:
	print(student[0])"""
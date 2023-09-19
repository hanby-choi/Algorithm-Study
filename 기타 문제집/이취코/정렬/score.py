# 정렬: 실전 문제 2 성적이 낮은 순서로 학생 출력하기
import sys
input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
    temp = input().split()
    arr.append((temp[0], int(temp[1])))
arr.sort(key = lambda x: x[1])
for i in arr:
    print(i[0], end = ' ')
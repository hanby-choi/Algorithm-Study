import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

def dfs(n):
	global cnt
	visited[n] = True # 해당 학생 방문
	cycle.append(n) # 사이클에 방문한 학생 추가
	if visited[students[n]] == True:
		if students[n] in cycle:
			cnt -= len(cycle[cycle.index(students[n]):])
			return
	else:
		dfs(students[n]) # n이 가리키는 학생 방문 
		
t = int(input())
while t:
	n = int(input())
	students = [0] 
	students.extend(list(map(int, input().split())))
	visited = [False] * (n+1)
	cnt = n
	for i in range(1, n+1):
		if not visited[i]:
			cycle = []
			dfs(i)
	print(cnt)
	t -= 1
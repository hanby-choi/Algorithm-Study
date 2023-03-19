# 그래프 이론: 실전 문제 3 커리큘럼
import sys, copy
from collections import deque
input = sys.stdin.readline
n = int(input())
indegree = [0] * (n+1)
graph = [[] for i in range(n+1)]
time = [0]
for i in range(1, n+1):
    tmp = list(map(int, input().split()))
    time.append(tmp[0])
    for j in tmp[1:-1]:
        graph[j].append(i)
        indegree[i] += 1
def topology_sort():
    result = copy.deepcopy(time)
    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i]) # 지금까지 저장된 값과 방금 방문한 선수강 강의를 듣기까지의 시간 + 그 강의 시간 더한 값
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    for i in range(1, n+1):
        print(result[i])
topology_sort()
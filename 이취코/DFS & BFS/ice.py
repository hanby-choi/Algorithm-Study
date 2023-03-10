# DFS & BFS: 실전 문제 1 음료수 얼려 먹기
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input().rstrip()))) 

def DFS(x, y):
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    if graph[x][y] == 0: # 현재 노드를 방문하지 않았다면
        graph[x][y] = 1 # 해당 노드 방문 처리
        DFS(x-1, y) # 상
        DFS(x, y-1) # 좌
        DFS(x+1, y) # 하
        DFS(x, y+1) # 우
        return True
    return False

result = 0
for i in range(N):
    for j in range(M):
        if DFS(i, j) == True:
            result += 1 # 처음 노드를 방문할 때 그 노드와 인접된 노드는 다 방문처리가 되므로 최초 1번만 true가 반환됨
print(result)
# 그래프 이론: 실전 문제 2 도시 분할 계획
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
parent = [i for i in range(n+1)]
edges = []
result = 0; cnt = 0
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
edges.sort()
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        cnt += 1
        # 혹은 last = cost 해서 마지막에 추가되는 간선의 비용을 저장한 후 result - last 출력
    if cnt == (n-2):
        break
print(result)
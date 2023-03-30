# 백트래킹: 10971 외판원 순회 2
import sys
input = sys.stdin.readline
n = int(input())
w = []
for _ in range(n):
    w.append(list(map(int, input().split())))
min_cost = 1e7 + 1
def TSP(start, next, visited, cost):
    global min_cost
    if len(visited) == n and w[next][start] != 0:
        min_cost = min(cost + w[next][start], min_cost)
        return
    for dest in range(n):
        if dest not in visited and w[next][dest] != 0 and cost < min_cost:
            visited.append(dest)
            TSP(start, dest, visited, cost + w[next][dest])
            visited.pop()
for i in range(n):
    TSP(i, i, [i], 0)
print(min_cost)
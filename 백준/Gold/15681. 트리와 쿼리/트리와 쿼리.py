import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def countPoint(x, count):
	count[x] = 1 # 방문 체크 겸 노드 수에 본인 세기
	for i in tree[x]: # 현재 정점과 연결된 정점(자식 노드) 탐색
		if not count[i]: # 아직 방문하지 않았다면 
			countPoint(i, count) # 방문
			count[x] += count[i] # 해당 노드의 서브 트리 정점 수 더해주기
	
n, r, q = map(int, input().split())
tree = [[] for _ in range(n+1)]
for i in range(n-1): # 간선 정보로 트리 구성
	a, b = map(int, input().split())
	tree[a].append(b)
	tree[b].append(a)

count = [0] * (n+1)
countPoint(r, count)

for _ in range(q):
	u = int(input())
	print(count[u])
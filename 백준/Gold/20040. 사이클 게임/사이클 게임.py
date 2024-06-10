import sys
input = sys.stdin.readline
def find_parent(parent, x):
	if parent[x] != x:
		parent[x] = find_parent(parent, parent[x])
	return parent[x]

def union_parent(parent, a, b):
	a = find_parent(parent, a)
	b = find_parent(parent, b)
	if a < b: # 번호가 더 작은 쪽을 부모 노드로 설정
		parent[b] = a
	else:
		parent[a] = b

n, m = map(int, input().split())
game = [tuple(map(int, input().split())) for _ in range(m)]
parent = [i for i in range(n+1)]
for i in range(m):
	a, b = game[i]
	if find_parent(parent, a) != find_parent(parent, b):
		union_parent(parent, a, b)
	else:
		print(i+1)
		exit()
print(0)
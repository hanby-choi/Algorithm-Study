def dfs(n, graph, v, visited):
	visited[v] = True
	for i in range(n):
		if not visited[i] and graph[v][i]:
			dfs(n, graph, i, visited)

def solution(n, computers):
	visited = [False] * n
	ans = 0
	for i in range(n):
		if not visited[i]:
			dfs(n, computers, i, visited)
			ans += 1
	return ans
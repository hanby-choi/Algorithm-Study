import sys
input = sys.stdin.readline
from itertools import combinations 

def calc(team, power):
	score = 0
	team_combi = combinations(team, 2)
	for t in team_combi:
		a, b = t[0], t[1]
		score += power[a][b] + power[b][a]
	return score
	
def solution(n, power):
	combi = combinations(range(n), n // 2)
	total = set(range(n))
	ans = 1e9
	for c in combi:
		start = c
		link = tuple(total - set(start))
		ans = min(ans, abs(calc(start, power) - calc(link, power)))
	return ans 
	
n = int(input())
power = [list(map(int, input().split())) for _ in range(n)] 
print(solution(n, power))
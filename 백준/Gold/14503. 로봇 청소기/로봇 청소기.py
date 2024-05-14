import sys
input = sys.stdin.readline

def solution(n, m, arr, r, c, d):
	cnt = 0
	dr = [-1, 0, 1, 0] # 북 동 남 서
	dc = [0, 1, 0, -1]
	while True:
		if arr[r][c] == 0: # 현재 칸이 아직 청소되지 않은 경우 
			arr[r][c] = 2 # 청소 
			cnt += 1
			
		allCleaned = True
		for i in range(4):
			nd = (d-i+3) % 4
			nr, nc = r + dr[nd], c + dc[nd]
			if 0 <= nr < n and 0 <= nc < m and arr[nr][nc] == 0: # 인접한 칸 중 청소되지 않은 칸이 있는 경우 
				allCleaned = False
				r, c, d = nr, nc, nd # 한 칸 전진 
				break
			
		if allCleaned: # 인접한 칸이 모두 청소된 경우 
			bd = (d+2) % 4
			br, bc = r + dr[bd], c + dc[bd]
			if arr[br][bc] == 1: 
				break
			r, c = br, bc # 후진할 수 있으면 후진
	return cnt

n, m = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _  in range(n)]
print(solution(n, m, arr, r, c, d))
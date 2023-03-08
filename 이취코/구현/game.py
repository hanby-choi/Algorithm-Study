# 구현: 실전 문제 2 게임 개발
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
A, B, d = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
visit = [[False for i in range(M)] for i in range(N)]
visit[A][B] = True
dx = [-1, 0, 1, 0] # 북 동 남 서
dy = [0, 1, 0, -1]
def turn_left(): # 3->2->1->0->3
    global d
    d -= 1
    if d == -1:
        d = 3
while True:
    moved = False
    for _ in range(4):
        turn_left() # 왼쪽으로 회전
        nA = A + dx[d]
        nB = B + dy[d]
        if visit[nA][nB] == False and arr[nA][nB] == 0: # 왼쪽 방향에 안 가본 칸 있고 그 칸이 육지면
            A, B = nA, nB # 전진
            visit[nA][nB] = True
            moved = True
            break
        # else면 회전만 진행하고 다음 방향 탐색
    if not moved: # 네 방향 모두 가본 칸이거나 바다로 된 칸이면
        nA = A - dx[d]
        nB = B - dy[d]
        if arr[nA][nB] == 1: # 뒤쪽 칸이 바다면
            break # 종료
        else:
            A, B = nA, nB # 바라보는 방향을 유지한 채로 한 칸 뒤로 감
cnt = 0
for i in range(N):
    for j in range(M):
        if visit[i][j] == True:
            cnt += 1
print(cnt)
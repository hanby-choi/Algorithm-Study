# 브루트 포스 - 1018: 체스판 다시 칠하기
n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(input())
mini = []
b_count = 0
for i in range(n-7):
    for j in range(m-7):
        for l in range(i, i+8):
            for o in range(j, j+8):
                if (l+o) % 2 == 0: # B여야 하는 영역
                    if arr[l][o] != 'B':
                        b_count += 1
                else:
                    if arr[l][o] != 'W':
                        b_count += 1
        b_count = min(b_count, 64-b_count)
        mini.append(b_count)
        b_count = 0
print(min(mini))
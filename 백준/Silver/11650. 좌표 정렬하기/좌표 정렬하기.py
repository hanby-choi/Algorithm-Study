n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x:(x[0], x[1]))
for a in arr:
	print(a[0], a[1])
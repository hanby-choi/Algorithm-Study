arr = [list(map(int, input().split())) for _ in range(3)]
for a in arr:
	cnt = a.count(0)
	if cnt == 0:
		print('E')
	else:
		print(chr(ord('A') - 1 + a.count(0)))
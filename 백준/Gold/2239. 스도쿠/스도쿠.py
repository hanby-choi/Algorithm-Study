import sys
input = sys.stdin.readline

def backtracking(idx):
	if idx == len(blank):
		for i in range(9):
			for j in range(9):
				print(sudoku[i][j], end='')
			print()
		exit()
	for num in range(1, 10):
		r, c = blank[idx][0], blank[idx][1]
		if checkRow(r, num) and checkColumn(c, num) and checkBox(r, c, num):
			sudoku[r][c] = num
			backtracking(idx + 1)
			sudoku[r][c] = 0

def checkRow(r, num):
	for j in range(9):
		if sudoku[r][j] == num:
			return False
	return True

def checkColumn(c, num):
	for j in range(9):
		if sudoku[j][c] == num:
			return False
	return True

def checkBox(i, j, num):
	r, c = i // 3, j // 3
	for row in range(3*r, 3*(r+1)):
		for column in range(3*c, 3*(c+1)):
			if sudoku[row][column] == num:
				return False
	return True

sudoku = [list(map(int, input().rstrip())) for _ in range(9)]
blank = []
for i in range(9):
	for j in range(9):
		if sudoku[i][j] == 0:
			blank.append((i, j))
backtracking(0)

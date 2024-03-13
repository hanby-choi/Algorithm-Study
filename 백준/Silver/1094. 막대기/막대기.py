import sys
input = sys.stdin.readline
x = int(input())
sticks = [64]
total = 64
while x < total:
	part = int(sticks.pop() / 2)
	sticks.append(part)
	if (total - part) >= x:
		total -= part
	else:
		sticks.append(part) 
print(len(sticks))
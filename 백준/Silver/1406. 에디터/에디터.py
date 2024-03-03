import sys
input = sys.stdin.readline
left = list(input().rstrip())
right = []
t = int(input())
while t:
	cmd = input().rstrip()
	if cmd == 'L' and left:
		right.append(left.pop())
	elif cmd == 'D' and right:
		left.append(right.pop())
	elif cmd == 'B' and left:
		left.pop()
	elif cmd[0] == 'P':
		left.append(cmd[2])
	t -= 1
print(''.join(left), end='')
print(''.join(right[::-1]))
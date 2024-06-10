import sys
input = sys.stdin.readline

def calcFloor(h, n):
    floor = n % h
    room_line = (n // h) + 1
    if floor == 0:
        floor = h
        room_line -= 1
    return floor * 100 + room_line

t = int(input())
while t > 0:
	h, w, n = map(int, input().split())
	print(calcFloor(h, n))
	t -= 1
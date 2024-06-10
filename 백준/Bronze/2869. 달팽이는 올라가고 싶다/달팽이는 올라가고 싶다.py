import sys, math
input = sys.stdin.readline

def cal(a, b, v):
	return math.ceil((v-a) / (a-b)) + 1

a, b, v = map(int, input().split())
print(cal(a, b, v))
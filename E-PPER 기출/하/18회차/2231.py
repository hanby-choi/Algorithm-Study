# 분해합: 브루트포스
import sys
input = sys.stdin.readline
def getNum(n):
    num = str(n)
    ans = n
    ans += sum(map(int, num))
    return ans
n = int(input())
found = False
for i in range(1, n+1):
    if getNum(i) == n:
        print(i)
        found = True
        break
if not found:
    print(0)
"""n = int(input())
found = False
for i in range(1, n+1):
	str_i = str(i)
	temp_sum = i + sum([int(str_i[j]) for j in range(len(str_i))])
	if temp_sum == n:
		print(i)
		found = True
		break
if not found:
	print(0) """
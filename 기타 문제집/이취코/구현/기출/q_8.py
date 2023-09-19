# 구현 - 8. 문자열 재정렬
import sys
input = sys.stdin.readline
S = input().rstrip()
alphabet = ''
num_sum = 0
for i in S:
    if '0' <= i <= '9':
        num_sum += int(i)
    else:
        alphabet += i
alphabet = sorted(alphabet)
print(''.join(list(alphabet)) + str(num_sum))
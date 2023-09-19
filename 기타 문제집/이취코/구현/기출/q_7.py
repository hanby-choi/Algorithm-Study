# 구현 - 7. 럭키 스트레이트
import sys
input = sys.stdin.readline
N = input().rstrip()
half_len = int(len(N)/2)
sum1 = sum([int(i) for i in N[:half_len]])
sum2 = sum([int(i) for i in N[half_len:]])
if sum1 == sum2:
    print("LUCKY")
else:
    print("READY")
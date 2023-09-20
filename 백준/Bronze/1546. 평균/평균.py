import sys
input = sys.stdin.readline
n = int(input())
score = list(map(int, input().split()))
max_score = max(score)
new_score = [s / max_score * 100 for s in score]
print(sum(new_score)/n)
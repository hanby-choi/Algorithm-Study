import sys
input = sys.stdin.readline
n, m = map(int, input().split())
not_hear = set(input().strip() for _ in range(n))
not_see = set(input().strip() for _ in range(m))
ans = sorted(list(not_hear & not_see))
print(len(ans))
for a in ans:
    print(a)

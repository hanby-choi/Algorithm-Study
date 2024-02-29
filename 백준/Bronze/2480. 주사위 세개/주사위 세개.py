import sys
input = sys.stdin.readline
dices = list(map(int, input().split()))
dic = {}
for d in dices:
    if d in dic:
        dic[d] += 1
    else:
        dic[d] = 1
if len(dic) == 1:
    print(10000 + dices[0] * 1000)
elif len(dic) == 2:
    for k, v in dic.items():
        if v == 2:
            print(1000 + k * 100)
else:
    m = max(dices)
    print(m * 100)
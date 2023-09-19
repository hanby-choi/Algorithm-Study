# 브루트 포스 - 1436: 영화감독 숌
n = int(input())
count = 1
for i in range(666, 6669999):
    if str(i).find("666") == -1:
        continue
    else:
        count += 1
    if count > n:
        print(i)
        break
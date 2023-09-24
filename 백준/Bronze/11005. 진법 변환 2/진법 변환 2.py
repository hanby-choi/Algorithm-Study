N, B = map(int, input().split())
ans = ''
arr = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
while N:
    ans += arr[N%B]
    N //= B
print(ans[::-1])
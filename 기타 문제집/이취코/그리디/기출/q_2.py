# 그리디 - 2. 곱하기 혹은 더하기
S = input()
ans = int(S[0])
for num in S[1:]:
	num = int(num)
	if num <= 1 or ans <= 1:
		ans += num
	else:
		ans *= num
print(ans)
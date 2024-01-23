n, k = map(int, input().split())
num1 = num2 = 1
for i in range(1, k+1):
	num1 *= n - i + 1
	num2 *= i
print(int(num1/num2))
import sys
input = sys.stdin.readline
def find_prime(n):
	is_prime = [True] * (MAX + 1)
	is_prime[0] = is_prime[1] = False
	for i in range(2, int(n ** 0.5) + 1):
		if is_prime[i]:
			for j in range(i*i, n+1, i):
				is_prime[j] = False
	return is_prime

def check(prime, is_prime, num):
	for p in prime:
		if is_prime[num-p]:
			return (str(num) + ' = ' + str(p) + ' + ' + str(num-p))
	return "Goldbach's conjecture is wrong."
	
MAX = 1000000
is_prime = find_prime(MAX)
prime = [i for i in range(MAX+1) if is_prime[i]]
while True:
	num = int(input())
	if num == 0:
		break
	print(check(prime, is_prime, num))
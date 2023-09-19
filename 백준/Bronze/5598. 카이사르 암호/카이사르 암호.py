import sys
input = sys.stdin.readline
word = input().rstrip()
def convert(word):
	ans = ''
	for c in word:
		uni = ord(c)
		if ord('A') <= uni <= ord('C'):
			ans += chr(uni + 23)
		else:
			ans += chr(uni - 3)
	return ans
print(convert(word))
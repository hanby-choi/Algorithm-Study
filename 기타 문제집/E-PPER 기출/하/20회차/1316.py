# 그룹 단어 체커: 문자열, 구현
import sys
input = sys.stdin.readline
n = int(input())
cnt = n
for _ in range(n):
	word = input().rstrip()
	alphabet = [False] * 26
	alphabet[ord(word[0])-ord('a')] = True
	for i in range(1, len(word)): 
		if word[i] != word[i-1] and alphabet[ord(word[i])-ord('a')]:
			cnt -= 1
			break
		alphabet[ord(word[i])-ord('a')] = True
print(cnt)
"""
import sys
input = sys.stdin.readline
n = int(input())
cnt = n
for _ in range(n):
	word = input().rstrip()
	alphabet = {word[0]: 1}
	for i in range(1, len(word)): # 해당 문자가 처음 등장
		if word[i] not in alphabet:
			alphabet[word[i]] = 1
		else:
			if word[i] == word[i-1]: # 같은 문자가 연속해서 등장
				alphabet[word[i]] += 1
			else: # 이전에 등장했던 문자가 연속하지 않게 다시 등장 - 그룹 단어 아님 
				cnt -= 1
				break
		before = i
print(cnt)
"""
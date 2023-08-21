# 비슷한 단어: 문자열, 구현, 파싱, 덱
import sys
input = sys.stdin.readline

def counting(ar, word):
    for w in word:
        i = ord(w) - ord('A')
        ar[i] += 1

def solution(n, words): # 단어의 총 개수와 단어의 배열
    ans = 0
    diff = 0
    freq_firstword = [0] * 26
    length = len(words[0])

    counting(freq_firstword, words[0])

    for i in range(1, n):
        diff = 0
        freq_other = [0] * 26
        counting(freq_other, words[i]) # 현재 조회하는 단어의 구성 세기

        for freq1, freq2 in zip(freq_other, freq_firstword):
            diff += abs(freq1-freq2) # 두 단어의 알파벳 차이 계산        

        if (diff == 0 or diff == 1 or (diff == 2 and (len(words[i]) == length))):
            ans += 1
    return ans

n = int(input())
words = [input().rstrip() for _ in range(n)]
ans = solution(n, words)
print(ans)

"""
import sys
input = sys.stdin.readline
n = int(input())
words = [input().rstrip() for _ in range(n)]
alphabet = [[0 for _ in range(26)] for _ in range(n)]
for i in range(n):
	for j in words[i]:
	    alphabet[i][ord(j) - ord('A')] += 1
cnt = 0
for i in range(1, n):
	if abs(len(words[0]) -len(words[i])) > 1: # 단어 길이가 2 이상 차이나면
		continue # 비슷한 구성 아님
	diff = 0
	for j in range(26):
		diff += abs(alphabet[0][j] - alphabet[i][j])
	if diff > 2: # 차이가 3개 이상이면
		continue # 비슷한 구성 아님
	if diff == 2 and abs(len(words[0]) -len(words[i])) != 0: # 차이가 2개 나는데 길이가 다르면 
		continue # 비슷한 구성 아님
	cnt += 1
print(cnt)

import sys
input = sys.stdin.readline
N = int(input())
target = list(input()) # 비교 대상 단어(첫 단어)
answer = 0

for _ in range(N-1):
    compare = target[:] 
    word = input() # 새로운 단어
    cnt = 0

    for w in word:
        if w in compare:
            compare.remove(w)
        else:
            cnt += 1

    if cnt < 2 and len(compare) < 2:
        answer += 1

print(answer)
"""
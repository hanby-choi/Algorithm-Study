# 그리디 - 3. 문자열 뒤집기
S = input()
parse = S[0]
for crnt in S[1:]:
    if crnt != parse[-1]:
        parse += crnt
print(int(len(parse)/2))
'''
S = input()
count0 = count1 = 0
if data[0] == '1':
	count0 += 1
else:
	count1 += 1
for i in range(len(data)-1):
	if data[i] != data[i+1]:
		if data[i+1] == '1': # 0 -> 1
			count0 += 1
		else: # 1 -> 0
			count1 += 1 
print(min(count0, count1))
'''
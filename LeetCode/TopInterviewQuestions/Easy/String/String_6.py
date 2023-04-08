# String to Integer (atoi)
class Solution(object):
    def myAtoi(self, s):
        MIN, MAX = -2**31, 2**31-1
        result, empty, sign = 0, True, 1 
        for ch in s:
            if empty:
                if ch == ' ': continue
                elif ch.isdigit(): result = int(ch)
                elif ch == '-': sign = -1
                elif ch != '+': return 0
                empty = False
            else:
                if ch.isdigit():
                    result = result * 10 + int(ch)
                else:
                    break
        result *= sign
        if result > MAX: result = MAX
        elif result < MIN: result = MIN
        return result
    def myAtoi2(self, s):
        ls = list(s.strip())
        if len(ls) == 0 : return 0
        sign = -1 if ls[0] == '-' else 1
        if ls[0] in ['-','+'] : del ls[0]
        ret, i = 0, 0
        while i < len(ls) and ls[i].isdigit() :
            ret = ret*10 + ord(ls[i]) - ord('0')
            i += 1
        return max(-2**31, min(sign * ret,2**31-1))
    
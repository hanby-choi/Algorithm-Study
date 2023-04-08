# Roman to Integer
class Solution(object):
    def romanToInt(self, s):
        ans = index = 0
        length = len(s)
        convert = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        while index < length:
            ch = s[index]
            special = False
            if ch == 'C' and (index+1) < length:
                if s[index+1] == 'D':
                    ans += 400
                    special = True
                elif s[index+1] == 'M':
                    ans += 900
                    special = True
            elif ch == 'X' and (index+1) < length:
                if s[index+1] == 'L':
                    ans += 40
                    special = True
                elif s[index+1] == 'C':
                    ans += 90
                    special = True
            if ch == 'I' and (index+1) < length:
                if s[index+1] == 'V':
                    ans += 4
                    special = True
                elif s[index+1] == 'X':
                    ans += 9
                    special = True
            if special:
                index += 2
            else:
                ans += convert[ch]
                index += 1
        return ans
    def romanToInt2(self, s):
        ans = 0
        convert = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        s = s.replace('CD', 'CCCC').replace('CM', 'DCCCC')
        s = s.replace('XL', 'XXXX').replace('XC', 'LXXXX')
        s = s.replace('IV', 'IIII').replace('IX', 'VIIII')
        for ch in s:
            ans += convert[ch]
        return ans
    def romanToInt(self, s):
        roman = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        z = 0
        for i in range(0, len(s) - 1):
            if roman[s[i]] < roman[s[i+1]]:
                z -= roman[s[i]]
            else:
                z += roman[s[i]]
        return z + roman[s[-1]]
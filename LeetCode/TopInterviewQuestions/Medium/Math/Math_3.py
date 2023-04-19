# Excel Sheet Column Number
class Solution(object):
    def titleToNumber(self, columnTitle):
        return 0 if not columnTitle else 26 ** (len(columnTitle)-1) * (ord(columnTitle[0]) - ord('A') + 1) + self.titleToNumber(columnTitle[1:])
    def titleToNumber(self, columnTitle):
        ans = 0
        n = len(columnTitle)
        for i, ch in enumerate(columnTitle):
            ans += 26 ** (n-i-1) * (ord(ch) - 64)
        return ans
    def titleToNumber(self, columnTitle):
        col_num = 0
        for char in columnTitle:
            col_num = col_num * 26 + (ord(char) - 64)
        return col_num
# Longest Common Prefix
class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) == 1:
            return strs[0]
        length = list(map(len, strs))
        result = ''
        for i in range(min(length)):
            flag = True
            for j in range(len(strs)-1):
                if strs[j][i] != strs[j+1][i]:
                    flag = False
            if flag:
                result += strs[0][i]
            else:
                break
        return result
    def longestCommonPrefix2(self, strs):
        common = strs[0]
        for i in range(1, len(strs)):
            tmp = ''
            for j in range(min(len(common), len(strs[i]))):
                if common[j] == strs[i][j]:
                    tmp += common[j]
                else:
                    break
            common = tmp
        return common
    def longestCommonPrefix3(self, strs):
        shortest = min(strs, key = len)
        for i in range(len(shortest)):
            if sum(1 for s in strs if shortest[i] != s[i]) > 0:
                return shortest[:i]
            """
            tmp = 0
            for s in strs:
                if shortest[i] != s[i]:
                    tmp += 1
                    break
            if tmp == 1:
                return shortest[:i]
            """
        return shortest
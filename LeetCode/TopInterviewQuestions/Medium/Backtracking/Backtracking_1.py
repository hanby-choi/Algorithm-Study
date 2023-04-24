# Letter Combinations of a Phone Number
class Solution(object):
    def letterCombinations(self, digits):
        n = len(digits)
        if n == 0:
            return []
        dic = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        ans = []
        def dfs(tmp, idx):
            if idx == n:
                ans.append(tmp)
                return
            for letter in dic[digits[idx]]:
                dfs(tmp + letter, idx + 1)
        dfs("", 0)
        return ans
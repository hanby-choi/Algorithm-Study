# Generate Parentheses
class Solution(object):
    def generateParenthesis(self, n):
        ans = []
        temp = ''
        def backtracking(op, cl, tmp):
            if op < cl:
                return
            if op == n:
                tmp += ')' * (n - cl)
                ans.append(tmp)
                return
            tmp += '('
            backtracking(op+1, cl, tmp)
            tmp[:] = tmp[:-1]
            tmp += ')'
            backtracking(op, cl+1, tmp)
            tmp = tmp[:-1]
        backtracking(0, 0, temp)
        return ans
    def generateParenthesis(self, n):
        def dfs(left, right, s):
            if len(s) == n * 2:
                res.append(s)
                return 

            if left < n:
                dfs(left + 1, right, s + '(')

            if right < left:
                dfs(left, right + 1, s + ')')

        res = []
        dfs(0, 0, '')
        return res
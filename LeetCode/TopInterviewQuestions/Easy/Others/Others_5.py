# Valid Parentheses
class Solution(object):
    def isValid(self, s):
        if len(s) % 2 != 0:
            return False
        dic = {'(':')', '{':'}', '[':']'}
        stack = []
        for ch in s:
            if ch in dic: # key로 여는 괄호인지 검사
                stack.append(ch)
            elif stack and dic[stack[-1]] == ch:
                stack.pop()
            else: # 닫는 괄호고 스택이 비어있거나 스택 top이 상응하는 짝이 아닌 경우
                return False
        return not stack # 모든 연산이 끝난 후에도 스택에 여는 괄호가 남아있다면 false
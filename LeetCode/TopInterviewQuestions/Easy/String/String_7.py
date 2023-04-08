# Implement strStr()
class Solution(object):
    def strStr(haystack, needle):
        if len(haystack) < len(needle):
            return -1
        ans = -1
        pnt1 = pnt2 = 0
        while pnt1 < len(needle) and pnt2 < len(haystack):
            print(pnt1, pnt2, ans)
            if needle[pnt1] == haystack[pnt2]:
                if ans == -1:
                    ans = pnt2
                pnt1 += 1
                pnt2 += 1
            else:
                if ans == -1:
                    pnt2 += 1
                else:
                    pnt2 = ans + 1
                    pnt1 = 0
                    ans = -1
            print(pnt1, pnt2, ans)
        if pnt2 == len(haystack) and pnt1 < len(needle):
            return -1
        return ans
Solution.strStr("mississippi", "pi")
# Valid Anagram
import collections
class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        cnt_s = collections.Counter(s)
        cnt_t = collections.Counter(t)
        if cnt_s == cnt_t:
            return True
        else:
            return False
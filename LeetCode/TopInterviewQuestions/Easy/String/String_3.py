# First Unique Character in a String
from collections import Counter
class Solution(object):
    def firstUniqChar(self, s):
        cnt = Counter(s) # cnt = collections.Counter(s)
        candidate = []
        for key, value in cnt.items():
            if value == 1:
                candidate.append(key)
        if not candidate:
            return -1
        min_index = 1e6
        for c in candidate:
            min_index = min(min_index, s.index(c))
        return min_index
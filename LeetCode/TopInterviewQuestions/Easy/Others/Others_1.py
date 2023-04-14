# Number of 1 Bits
class Solution(object):
    def hammingWeight(self, n):
        return bin(n).count('1')
    def using_inbuilt_counter(self, n):
        counter = collections.Counter(bin(n)[2:]) # 0b 무시하기 위해 2번째부터 탐
        return counter.get("1", 0)
    def hammingWeight2(self, n):
        cnt = 0
        while n:
            cnt += n & 1
            n = n >> 1
        return cnt
    def hammingWeight3(self, n):
        cnt = 0
        while n:
            n &= (n-1)
            cnt += 1
        return cnt
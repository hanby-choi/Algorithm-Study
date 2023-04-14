# Hamming Distance
class Solution(object):
    def hammingDistance(self, x, y):
        x = bin(x)[2:]
        y = bin(y)[2:]
        len_x = len(x)
        len_y = len(y)
        if len_x < len_y:
            x = '0'*(len_y-len_x) + x
        else:
            y = '0'*(len_x-len_y) + y
        cnt = 0
        for i in range(len(x)):
            if x[i] != y[i]:
                cnt += 1
        return cnt

    def hammingDistance2(self, x, y):
        return bin(x ^ y).count('1')

    def hammingDistance3(self, x, y):
        xor = x ^ y
        distance = 0
        while xor:
            xor &= xor - 1
            distance += 1
        return distance
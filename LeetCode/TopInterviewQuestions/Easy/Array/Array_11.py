# Rotate Image
class Solution(object):
    def rotate(self, matrix):
        a = matrix[:]
        i = 0
        for col in zip(*a):
            tmp = reversed(list(col))
            matrix[i][:] = tmp
            i += 1
        return
    def rotate2(self, matrix):
        # reverse
        matrix[:] = matrix[::-1]
        # transpose 
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
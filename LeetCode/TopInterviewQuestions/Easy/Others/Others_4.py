# Pascal's Triangle
class Solution(object):
    def generate(self, numRows):
        pascal = []
        for i in range(1, numRows + 1):
            pascal.append([1] * i) # pascal[i][0] = pascal[i][-1] = 1
            for j in range(1, i-1):
                pascal[i-1][j] = pascal[i-2][j-1] + pascal[i-2][j]
        return pascal
    def generate2(self, numRows):
        num = [[1], [1, 1]]
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return num
        elif numRows == 0:
            return []
        row = []
        for i in range(2, numRows):
            for j in range(i - 1):
                row.append(sum(num[-1][j:j + 2]))
            num.append([1] + row + [1])
            row = []
        return num
    def generate3(self, numRows):
        res = [[1]]
        for i in range(1, numRows):
            res += [list(map(lambda x, y: x+y, res[-1] + [0], [0] + res[-1]))]
        return res[:numRows]
        """
            1 3 3 1 0 
        +  0 1 3 3 1
        =  1 4 6 4 1
        """
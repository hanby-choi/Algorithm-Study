# Unique Paths
class Solution(object):
    def uniquePaths(self, m, n):
        d = [[1 for i in range(n)] for j in range(m)]
        for i in range(1, n):
            for j in range(1, m):
                d[j][i] = d[j-1][i] + d[j][i-1]
        return d[m-1][n-1]
    def uniquePaths2(self, m, n):
        if m == 1 or n == 1:
            return 1
        result = j = 1
        m -= 1
        n -= 1
        if m < n:
            m, n = n, m
        for i in range(m+1, m+n+1):
            result *= i
            result /= j
            j += 1
        return result
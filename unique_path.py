class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        f = {}
        for i in xrange(m):
            for j in xrange(n):
                if (i == 0 or j == 0):
                    f[(i, j)] = 1
                else:
                    f[(i, j)] = f[(i - 1, j)] + f[(i, j - 1)]
        return f[(m - 1, n - 1)]

if __name__ == '__main__':
    m, n = 3, 7
    unique_path = Solution().uniquePaths(m,n)
    print unique_path

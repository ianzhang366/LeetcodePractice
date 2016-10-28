class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        print grid
        return 0
        sum_of_position = {}

        for i in xrange(1, m):
            sum_of_position[(i,0)] = grid[i-1, 0]
        for j in xrange(1, n):
            sum_of_position[(0, j)] = grid[0, j-1]

        for i in xrange(1,m):
            for j in xrange(1,n):
                sum_of_position[(i, j)] = min(sum_of_position[i-1, j], sum_of_position[i, j-1]) + grid[i,j]
        return sum_of_position[(m-1, n-1)]

if __name__ == '__main__':
    grid = [[]]
    print Solution().minPathSum(grid)
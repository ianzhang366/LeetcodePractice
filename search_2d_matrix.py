class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row = len(matrix)
        col = len(matrix[0])
        if col == 0:
            return False
        total_length = row*col
        left, right = 0, total_length-1
        while left < right:
            mid = left + (right - left) / 2
            i, j = mid / col, mid % col
            value = matrix[i][j]
            if value == target:
                return True
            elif value < target:
                left = mid + 1
            else:
                right = mid
        return False

if __name__ == '__main__':
    # matrix, target = [[1,   3,  5,  7],[10, 11, 16, 20],[23, 30, 34, 50]], 3
    matrix, target = [[1, 1]], 2
    print Solution().searchMatrix(matrix, target)
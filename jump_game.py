class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length = len(nums)
        if length < 2:
            return True
        max_setp_left = 0
        for position in xrange(length):
            if nums[position] == 0:
                return False
            if max_setp_left < 0:
                return False
            max_setp_left = max(max_setp_left, nums[position]) - 1

        if max_setp_left > 0:
            return True

if __name__ == '__main__':
    A = [2, 3, 1, 0, 4]
    can_jump = Solution().canJump(A)
    print can_jump
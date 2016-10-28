class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        jumped_to, cur_posible_jump, result = 0, 0, 0
        for position in xrange(len(nums)):
            if position > jumped_to:
                jumped_to = cur_posible_jump
                result += 1
            cur_posible_jump = max(cur_posible_jump, position + nums[position])

        return result

if __name__ == '__main__':
    A = [2,3,1,1,4]
    test = Solution().jump(A)
    print test

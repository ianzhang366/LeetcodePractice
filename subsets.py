class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        length = len(nums)
        num = [''.join(str(i)) for i in nums]
        num = ''.join(num)


        possible = 2**length
        for item in range(possible):
            positions = bin(item)[2:]
            if len(positions) != length:
                diff = length - len(positions)
                while diff:
                    positions = '0' + positions
                    diff -= 1
            temp = []
            print positions
            for i in range(length):
                if positions[i] == '1':
                    temp.append(nums[i])
            result.append(temp)
        return result


if __name__ == '__main__':
    nums = [1, 2, 3]
    print Solution().subsets(nums)
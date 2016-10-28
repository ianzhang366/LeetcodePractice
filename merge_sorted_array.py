class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[i+m] = nums2[i]
        nums1.sort()
if __name__ == '__main__':
    s = Solution()
    nums2 = [ 2, 5, 7]
    m = 2
    nums1 = [1, 4, 6]
    n = 1
    s.merge(nums1, m, nums2, n)

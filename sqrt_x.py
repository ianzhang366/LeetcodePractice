class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x
        left, right = 1, x/2
        while left <= right:
            mid = left + (right-left)/2
            if (x / mid) > mid:
                left = mid + 1
                last_mid = mid
            elif (x / mid) < mid:
                right = mid - 1
            else:
                return mid
        return last_mid


if __name__ == '__main__':
    x = 5
    print Solution().mySqrt(x)
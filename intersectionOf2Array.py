class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        def inter(nums1, nums2):
            s1 = set(nums1)
            s2 = set(nums2)
            return list(s1 & s2)

        def listToDic(lis):
            dic = {}
            for item in lis:
                try:
                    dic[item] += 1
                except:
                    dic[item] = 1
            return dic
        if inter(nums1, nums2):
            d_1 = listToDic(nums1)
            d_2 = listToDic(nums2)
            re = []
            for item in inter(nums1, nums2):
                if d_1[item] >= d_2[item]:
                    for i in range(d_2[item]):
                        re.append(item)
                else:
                    for i in range(d_1[item]):
                        re.append(item)
            return re
        else:
            return []

if __name__ == '__main__':
    s = Solution()
    nums1 = [1]
    nums2 = [1,1]
    print s.intersection(nums1, nums2)

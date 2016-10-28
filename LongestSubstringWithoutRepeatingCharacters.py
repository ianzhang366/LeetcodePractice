# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         w_size = len(s)
#         if w_size != 1:
#             while w_size <= len(s):
#                 for i in range (len(s)- w_size):
#                     # s[i:i+w_size+1]
#                     sub = list(set(s[i:i+w_size+1]))
#                     l = len(s[i:i+w_size+1])
#                     if l == len(sub):
#                         return l
#                 w_size -= 1
#         else:
#             return 1

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_len = len(s)
        re = []
        ans = 0
        i, j = 0, 0 #start and end pointer
        while (i<s_len) and (j < s_len):
            if not(s[j] in re):
                re.append(s[j])
                j += 1
                ans = max(ans, j-i)
            else:
                re.pop(0)
                i += 1
        return ans

if __name__ == '__main__':
    s = Solution()
    in_string = "ylfzmeipzgwsdzgrebwvshaelhsndxydifdxllmltifwkooqpmohtqngygudfshqzknlvbyrmfnwt"
    # in_string = "abcabcbb"
    print s.lengthOfLongestSubstring(in_string)

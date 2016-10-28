import string

class Solution(object):
    def isPalindrome(self, in_string):
        """
        :type s: str
        :rtype: bool
        """
        if in_string:
            exclude = set(string.punctuation)
            s = ''.join(ch for ch in in_string.lower() if ch not in exclude)
            s = [d for d in s if d != ' ']
            s_o = ''.join(s)
            s.reverse()
            s_r = ''.join(s)
            if s_r == s_o:
                return True
            else:
                return False
        else:
            return True


if __name__ == '__main__':
    s = Solution()
    in_string = "race a car"
    print s.isPalindrome(in_string)



class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        BRACES = { '(': ')', '[': ']', '{': '}' }
        stack = [] #only store the right brackets
        for b in s:
            c = BRACES.get(b)
            if c:
                stack.append(c)
            elif not stack or stack.pop() != b: # if input is left brackets then pop stack, else return false
                return False
        return not stack # if stack is empty, it is macthed sequence


if __name__ == '__main__':
    s = Solution()
    in_string = '('
    # in_string = "abcabcbb"
    print s.isValid(in_string)

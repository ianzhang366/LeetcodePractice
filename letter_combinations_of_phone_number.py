import itertools
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        key_panel = {'1': '',
                     '2': ['a', 'b', 'c'],
                     '3': ['d', 'e', 'f'],
                     '4': ['g', 'h', 'i'],
                     '5': ['j', 'k', 'l'],
                     '6': ['m', 'n', 'o'],
                     '7': ['p', 'q', 'r', 's'],
                     '8': ['t', 'u', 'v'],
                     '9': ['w', 'x', 'y', 'z']}
        digits = list(digits)
        print digits
        candidate_letters = []
        length = len(digits)
        result = []
        for item in digits:
            for i in key_panel[item]:
                candidate_letters.append(i)

        for comb in list(itertools.combinations(candidate_letters, length)):
            flag = False
            for digit in digits:
                if comb[0] in key_panel[digit] and comb[1] in key_panel[digit]:
                    flag = True
            if not flag:
                result.append(''.join(comb))
        return result
if __name__ == '__main__':
    digits = "13"
    print Solution().letterCombinations(digits)
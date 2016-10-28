# # from sets import Set
# class Solution(object):
#     def minWindow(self, s, t):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         s, t = list(s), list(t)
#         s_len, w_len = len(s), len(t)
#
#         def listToDic(lis):
#             dic = {}
#             for item in lis:
#                 try:
#                     dic[item] += 1
#                 except:
#                     dic[item] = 1
#             return dic
#         def campareCnt(t, s):
#             dic_t = listToDic(t)
#             dic_s = listToDic(s)
#             for j in set(t):
#                 if dic_s[j] < dic_t[j]:
#                     return False
#             return True
#
#         while w_len <= s_len:
#             for i in range(s_len-w_len+1):
#                 if set(t) <= set(s[i:i+w_len]):
#                     # print s[i:i+w_len]
#                     if len(set(t)) == len(t):
#                         return ''.join(s[i:i+w_len])
#                     else:
#                         if campareCnt(t, s[i:i+w_len]):
#                             return ''.join(s[i:i+w_len])
#             w_len += 1
#         return ""

# from sets import Set

class  Solution:
  #  @return a string

    def minWindow(self, source, target):
        if (target == ""):
            return ""
        S , T = source, target
        d, dt = {}, dict.fromkeys(T, 0)
        for c in T: d[c] = d.get(c, 0) + 1
        pi, pj, cont = 0, 0, 0 # set up start, end pointer and a counter to check candidate window size
        if (source =="" or target ==""):
            return ""
        ans = ""
        for pj in range(len(S)): # move end pointer
            if S[pj] in dt: # if pointing element is in T then, add counter
                if dt[S[pj]] < d[S[pj]]:
                    cont += 1
                dt[S[pj]] += 1;
            if cont == len(T):
                while pi < pj: # move start pointer, if remains cover T
                    if S[pi] in dt:
                        if dt[S[pi]] == d[S[pi]]:
                            break;
                        dt[S[pi]] -= 1;
                    pi+= 1
                if ans == '' or pj - pi < len(ans):
                    ans = S[pi:pj+1]
                dt[S[pi]] -= 1 
                pi += 1
                cont -= 1
        return ans


if __name__ == '__main__':
    s = Solution()
    # S = "bbaa"
    # T = "aba"
    S = "ADOBECODEBANC"
    T = "ABC"
    print s.minWindow(S, T)

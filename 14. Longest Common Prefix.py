# Question: https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for s in strs[1:]:
            i = 0   
            min_len = lambda x, y: x if x < y else y
            loop = min(len(s), len(prefix))
            while i < loop and prefix != '':
                if s[i] != prefix[i]:
                    break
                i += 1
            prefix = prefix[:i]
        return prefix
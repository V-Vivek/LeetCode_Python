# Question: https://leetcode.com/problems/longest-palindromic-substring/description/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        if l == 1:
            return s
        max = s[0]
        for i, ch in enumerate(s):
            ct = s.count(ch, i+1, l)
            j = i + 1
            while ct:
                ind = s.find(ch, j, l)
                if s[i : ind+1] == s[ind : i : -1] + ch and len(s[i : ind+1]) > len(max):
                    max = s[i : ind+1]
                j = ind + 1
                ct -= 1

        return max
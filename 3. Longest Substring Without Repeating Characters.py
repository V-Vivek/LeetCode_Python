# Question: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1
        else:
            maximum = 1
            substring = ''
            for ch in s:
                if ch in substring:
                    substring = substring[substring.index(ch) + 1 :] + ch
                    continue
                substring += ch
                maximum = max(maximum, len(substring))
            maximum = max(maximum, len(substring))
            return maximum      
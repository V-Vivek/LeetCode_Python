# Question: https://leetcode.com/problems/valid-palindrome/description/

# Solution #1
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        for _ in s:
            if not _.isalnum():
                s = s.replace(_, '')

        return (s[: len(s)//2] == s[::-1][: len(s)//2])

# Solution #2
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        result = []
        print(s)
        for _ in s:
            if _.isalnum():
                result.append(_)
        result = ''.join(result)

        return (result[: len(result)//2] == result[::-1][: len(result)//2])
# Question: https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        if x < 0:
            return False
        elif s == s[::-1]:
            return True
        else:
            return False
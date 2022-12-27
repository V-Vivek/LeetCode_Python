# Question: https://leetcode.com/problems/plus-one/

# Solution #1
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        result = ''
        oneplus = []
        for i in digits:
            result += str(i)
        result = str(int(result) + 1)

        for n in result:
            oneplus.append(int(n))
        return oneplus


# Solution #2
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        was9 = False
        i = -1
        while i > (len(digits) * -1) - 1:
            if digits[i] == 9:
                digits[i] = 0
                was9 = True
            else:
                digits[i] += 1
                was9 = False
                break
            i -= 1
        if was9:
            digits = [1] + digits
        return digits
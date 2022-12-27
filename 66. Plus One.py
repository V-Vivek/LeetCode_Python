# Question: https://leetcode.com/problems/plus-one/

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

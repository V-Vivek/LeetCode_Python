# Question: https://leetcode.com/problems/single-number/description/

# Solution #1
from collections import Counter
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        count = Counter(nums)
        for k, v in count.items():
            if v == 1:
                return k


# Solution #2
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        d = dict()
        for n in nums:
            if d.get(n) != None:
                d[n] += 1
            else:
                d[n] = 1
        for k, v in d.items():
            if v == 1:
                return k
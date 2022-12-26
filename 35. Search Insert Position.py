# Question: https://leetcode.com/problems/search-insert-position/

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        for i, n in enumerate(nums):
            if n >= target:
                return i
                break
        else:
            return i + 1
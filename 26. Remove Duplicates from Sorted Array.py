# Question link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i=0
        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                nums.remove(nums[i])
                i-=1
            i+=1
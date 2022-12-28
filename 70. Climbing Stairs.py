class Solution:
    def climbStairs(self, n: int) -> int:
        if n > 2:
            start = 1
            next = 2
            for i in range(2,n):
                temp = start + next
                start, next = next, temp
        else:
            temp = n
        return temp
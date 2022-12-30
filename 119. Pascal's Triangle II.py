# Question: https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        temp = [1]
        if rowIndex == 0:
            return temp
        else:
            previous = [1]
            i = 2
            while i <= rowIndex + 1:
                temp = [1]
                for j in range(0, i-2):
                    temp.append(previous[j] + previous[j+1])
                temp += [1]
                previous = temp
                i += 1
            return temp
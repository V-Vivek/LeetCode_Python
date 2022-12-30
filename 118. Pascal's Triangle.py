# Question: https://leetcode.com/problems/pascals-triangle/description/

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        result = [[1]]
        if numRows == 1:
            return result
        else:
            previous = [1]
            i = 2
            while i <= numRows:
                temp = [1]
                for j in range(0, i-2):
                    temp.append(previous[j] + previous[j+1])
                temp += [1]
                result.append(temp)
                previous = temp
                i += 1
            return result
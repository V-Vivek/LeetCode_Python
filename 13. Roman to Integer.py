class Solution:
    def romanToInt(self, s: str) -> int:
        s = s + "_" #To eliminate string index out of range problem
        romanDict = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000, "_":0}
        sum = 0
        for i in range(len(s)-1):
            if (romanDict.get(s[i])>=romanDict.get(s[i+1])):
                sum = sum + romanDict.get(s[i])
            else:
                sum = sum - (romanDict.get(s[i]))
        return sum

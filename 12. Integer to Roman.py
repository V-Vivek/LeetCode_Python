class Solution:
    def intToRoman(self, num: int) -> str:
        romanList = [1, 5, 10, 50, 100, 500, 1000, 4, 9, 40, 90, 400, 900]
        romanDict = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M', 4:'IV', 9:'IX', 40:'XL', 90:'XC', 400:'CD', 900:'CM'}
        roman = ''
        tempRoman = []

        while num != 0:
            # Check if num is a standard value from romanList
            if (num in romanList):
                tempRoman.append(num)
                num = num - num
            # Check if temp is 0 & incerement the number of digits until we get non-zero value else set temp as num
            else:
                if num % 10:
                    temp = num % 10
                elif num % 100:
                    temp = num % 100
                elif num % 1000:
                    temp = num % 1000
                else:
                    temp = num
                # Check if temp is a standard value from romanList
                if (temp in romanList):
                    tempRoman.append(temp)
                    num = num - temp
                # Get the closest & valid roman digit for the temp
                else:
                    approxRomanList = [x for x in romanList if x > temp]
                    if approxRomanList:   # If value less than 1000
                        actualRoman = romanList[romanList.index(approxRomanList[0])-1]
                    else:
                        actualRoman = 1000   # If value greater than 1000
                    tempRoman.append(actualRoman)
                    num = num - actualRoman

        # Sort the list & generate the roman numbers using the romanDict dictionary
     
        tempRoman.sort(reverse=True)
       
        for num in tempRoman:
            roman = roman + romanDict.get(num)

        return roman

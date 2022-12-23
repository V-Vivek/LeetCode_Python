# Question: https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        check = []
        result = False

        for _ in s:
            if _ == '{':
                check.append(_)
            elif _ == '}' and len(check) > 0:
                if check[-1] != '{':
                    return result
                check.pop()
            elif _ == '[':
                check.append(_)
            elif _ == ']' and len(check) > 0:
                if check[-1] != '[':
                    return result
                check.pop()
            elif _ == '(':
                check.append(_)
            elif _ == ')' and len(check) > 0:
                if check[-1] != '(':
                    return result
                check.pop()
            else:
                return result

        if check == []:
            result = True
        return result
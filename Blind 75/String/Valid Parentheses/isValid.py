class Solution:
    def isValid(self, s: str) -> bool:
        """
        Determines if the input string contains a valid sequence of parentheses.

        Parameters:
        - s (str): Input string.

        Returns:
        - bool: True if the string has a valid sequence of parentheses, otherwise False.

        Examples:
        (), ([{}]) are valid
        (]), }{)()} are invalid
        
        """
        
        lst = []

        for i in s:
            if i == '(' or i == '[' or i == '{':
                lst.append(i)
            elif i == ')':
                if not lst or lst[-1] != '(':
                    return False
                else:
                    lst.pop(-1)
            elif i == '}':
                if not lst or lst[-1] != '{':
                    return False
                else:
                    lst.pop(-1)
            elif i == ']':
                if not lst or lst[-1] != '[':
                    return False
                else:
                    lst.pop(-1)
            
        return lst == []
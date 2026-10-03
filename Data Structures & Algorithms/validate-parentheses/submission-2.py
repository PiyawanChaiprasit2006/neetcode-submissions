class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pair = {')':'(', '}':'{', ']':'['}

        for c in s:
            if c in pair:
                if len(stack) == 0:
                    return False
                else:
                    check = stack.pop()
                    
                if check != pair[c]:
                    return False
            else:
                stack.append(c)
        if len(stack) == 0:
            return True
        else:
            return False

class Solution:
    def isValid(self, s: str) -> bool:
        lookup = {"(":")", "[":"]", "{":"}"}
        stack = []

        for char in s:
            if char in lookup:
                stack.append(char)
            else:
                if not stack or char != lookup[stack.pop()]:
                    return False

        
        return len(stack) == 0

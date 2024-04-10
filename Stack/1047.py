class Solution:
    def removeDuplicates(self, s: str) -> str:
        #edge case
        if not s:
            return "";
        
        #var define
        stack = []

        for char in s:
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
        
        return "".join(stack)

        
        
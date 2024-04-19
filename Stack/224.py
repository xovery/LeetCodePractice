class Solution:
    def calculate(self, s: str) -> int:

        #var
        stack = []
        
        operators = {"+", "-", "(", ")"}
        sign = 1
        result = 0
        currNum = 0

        nums = set()
        
        #init set
        for i in range(10):
            nums.add(str(i))

        for char in s:
            if char in nums:
                currNum = 10*currNum + (ord(char) - ord('0'))            
            elif char in operators:
                if char == "+":
                    result += sign * currNum
                    sign = 1
                elif char == "-":
                    result += sign * currNum
                    sign = -1
                elif char == "(":
                    stack.append(result)
                    stack.append(sign)
                    result = 0
                    sign = 1
                elif char ==  ")":
                    result += sign * currNum
                    result *= stack.pop()
                    result += stack.pop()
                currNum = 0
            
        return result + sign * currNum


        

        
        
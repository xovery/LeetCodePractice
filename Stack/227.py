class Solution:
    def calculate(self, s: str) -> int:
        
        #edge case
        if not s:
            return 0

        #parameter init        
        stack = []
        curNum = 0
        curOperator = "+"
        operators = {"+", "-", "*", "/"}
        nums = set()


        for i in range (10):
            nums.add(str(i))

        for idx, char in enumerate(s):
            if char in nums:
                curNum = curNum * 10 + (ord(char) - ord("0"))
                                    
            if char in operators or (idx == len(s) - 1):
                if curOperator == "+":
                    stack.append(curNum)
                elif curOperator == "-":
                    stack.append(-curNum)
                elif curOperator == "*":
                    temp = stack.pop()
                    stack.append(temp*curNum)
                elif curOperator == "/":
                     temp = stack.pop()
                     stack.append(int(temp/curNum))
            
                curNum = 0
                curOperator = char
        
        return sum(stack)

        
        
class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []
        operators = {"[", "]"}
        currNum = 0
        currStr = ""

        for char in s:            
            if char in operators:
                if char == "[":
                    stack.append(currStr)
                    stack.append(currNum)
                    currStr = ""
                    currNum = 0
                elif char == "]":
                    num = stack.pop()
                    prevStr = stack.pop()                
                    currStr = prevStr + currStr * num
            elif char.isdigit():
                currNum = currNum * 10 + int(char)
            else:
                currStr += char
                        
        return currStr

        #TC O(n)
        #SC O(n)


                
            


        
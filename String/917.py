class Solution:
    def reverseOnlyLetters(self, s: str) -> str:

        strList = list(s)
        #strList = s
        left = 0
        length = len(s)
        right = length - 1

        while left < right:
            while left < right and not strList[left].isalpha():
                left += 1
            while left < right and not strList[right].isalpha():
                right -= 1
            
            strList[left], strList[right] = strList[right], strList[left]
            
            left += 1
            right -= 1
        
        return "".join(strList)

        
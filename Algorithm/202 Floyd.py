class Solution:
    def isHappy(self, n: int) -> bool:
        def findSquareSum(num:int):
            CurrSum = 0

            while num > 0:
                digit = num % 10
                CurrSum += digit ** 2
                num = num // 10
            return CurrSum

        slow = fast = n 

        while True:
            slow = findSquareSum(slow)
            fast = findSquareSum(findSquareSum(fast))
            if slow == fast:
                break
        
        if slow == 1:
            return True
        return False
                

        
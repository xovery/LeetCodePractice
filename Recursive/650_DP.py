class Solution:
    def minSteps(self, n: int) -> int:
        
        steps = 0
        divisor = 2
        while n > 1:
            while n % divisor == 0:
                print("divisor {}".format(divisor))
                steps += divisor                
                n //= divisor                
                print("steps {}, n {}".format(steps, n))
            divisor += 1
            
        return steps
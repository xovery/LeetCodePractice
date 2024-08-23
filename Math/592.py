from fractions import Fraction

class Solution:
    def fractionAddition(self, expression: str) -> str:
        
        fractions = []
        num = ""
        
        for char in expression:
            if char in "+-":
                if num:
                    print("num append{}".format(num))
                    fractions.append(Fraction(num))
                print("num = {}".format(num))
                num = char
            else:
                print("num += {}".format(num))
                num += char
                
        fractions.append(Fraction(num))  # Add the last fraction
        
        # Sum up all the fractions
        result = sum(fractions)
        #result = sum(fractions, Fraction(0))
        print(result)
        
        # Return the result as a fraction in the form "numerator/denominator"
        return f"{result.numerator}/{result.denominator}"


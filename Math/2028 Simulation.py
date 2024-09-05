class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        
        #TC o(n)
        #SC o(1)
        sizeTotal = len(rolls) + n
        sumRolls = sum(rolls)
        valueNeed = sizeTotal * mean - sumRolls
        MAXDICENUM = 6 # this is a constant. the max number of a dice is 6.
        
        res = []

        if valueNeed < 0 or (valueNeed > n * MAXDICENUM) or n > valueNeed :
            return []

        numPlus = valueNeed % n

        for i in range(n):
            temp = valueNeed//n
            if numPlus > 0: 
                if temp+numPlus > MAXDICENUM:                
                    numPlus = numPlus - (MAXDICENUM-temp)
                    temp = MAXDICENUM
                else:
                    temp += numPlus
                    numPlus = 0                                        
            res.append(temp)                        
        return res






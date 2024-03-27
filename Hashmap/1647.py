class Solution:
    def minDeletions(self, s: str) -> int:
        
        #edge case checking
        if not s:
            return 0
        
        #var define & init
        result = 0
        unique = set()

        #algorithm
        #method 1. build the haspmap by python func
        #lookup = collections.Counter(s)

        #method 2. manually build the hashmap 
        lookup = {}
        for char in s:
            lookup[char] = lookup.get(char, 0) + 1
        
        for count in lookup.values():
            while count and count in unique:
                result +=1
                count -=1
            unique.add(count)
        
        return result
            

            

            
        
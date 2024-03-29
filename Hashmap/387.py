class Solution:
    def firstUniqChar(self, s: str) -> int:
        #edge case
        if not s:
            return -1
        
        #variable init
        lookup = {}
        result = 0
        
        #algorithm
        for char in s:
            lookup[char] = lookup.get(char, 0) + 1
        
        
        for index, char  in enumerate(s):
            if lookup[char] == 1:
                return index
        
        return -1

        